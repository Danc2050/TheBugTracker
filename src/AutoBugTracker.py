import argparse
import os
import selectors
import sys
import subprocess
from time import sleep

import src.GithubIntegration as githubIntegration
import src.GithubIssue as githubIssue
import src.ReadConfig as readConfig
import src.DebugLogFile as debugLogFile
import src.DatabaseScript as initializeDatabaseScript
import src.EmailUsers as emailUsers
import src.BugRecordDTO as bugRecordDTO
from src.FilterLists import filterBugReport


class AutoBugTracker(object):
    def __init__(self):
        print("***Auto Bug Tracker***\n")
        # Gets configuration file, if non existent it will create one
        self.configOptions = readConfig.readConfig()
        self.logs = debugLogFile.DebugLogFile(self.configOptions)
        # Initialize database
        self.database = initializeDatabaseScript.Database(self.logs)
        self.databaseConfiguration()
        self.github = self.githubConfiguration()
        self.email = self.emailConfiguration()
        self.filterBugReport = filterBugReport()

    def parsingCommandLineArguments(self):
        """
        Return dictionary

        capture command line arguments.
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('-S', '--userScript', help='User script Required!', required=True)
        arguments = parser.parse_args()
        return vars(arguments)

    def githubConfiguration(self):
        """
        Gets the necessary config keys to initialize github

        :return: Github initialized
        """
        githubFlag = self.configOptions.getConfig(key="github_integration")
        githubAccessToken = self.configOptions.getConfig(key="github_access_token")
        githubRepoName = self.configOptions.getConfig(key="github_repo_name")
        if githubFlag is True:
            if (not githubAccessToken) or (not githubRepoName):
                # Stop the execution of the program
                raise Exception("Github_Integration is set to True but configure file is "
                                "missing github access token and/or repo name")
            else:
                try:
                    return githubIntegration.GithubIntegration(githubAccessToken, githubRepoName)
                except Exception as e:
                    self.logs.writeToFile(str(e))

    def databaseConfiguration(self):
        """
        Connects to the postgres server that has the projects database. Then connects to that database.

        :return: Database initialized
        """
        try:
            self.database.connect(server_params="postgres_server")
            self.database.create_database(database_params="postgres_db")
            self.database.create_table(table_name="Bugs")
        except Exception as e:
            self.logs.writeToFile(str(e))

    def emailConfiguration(self):
        """
        Initializes data to email specified user(s). body of report passed to this function.

        :return: email sent
        """
        try:
            username = os.environ["USERNAME"]
            password = os.environ["PASSWORD"]
        except KeyError as e:
            raise KeyError("Please add your email and password to your environment variables file " + str(e))
        try:
            return emailUsers.EmailUsers(username, password)
        except Exception as e:
            raise Exception(str(e))

    def sendEmail(self, body):
        first = self.configOptions.getConfig(key='first')
        last = self.configOptions.getConfig(key='last')
        email = self.configOptions.getConfig(key='email')
        subject = ("AutoBugTracker Report: " + str(first) + str(last))
        try:
            self.email.send_email(body, subject, email)
        except Exception as e:
            self.logs.writeToFile(str(e))

    def run(self):
        """
        Listen to invoked script for any bugs to report
        """
        scriptName = self.parsingCommandLineArguments()['userScript']
        self.filterBugReport.appendFile("white.list", scriptName)
        p = subprocess.Popen([scriptName],
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             shell=True)

        sel = selectors.DefaultSelector()
        sel.register(p.stderr, selectors.EVENT_READ)

        while True:
            for key, _ in sel.select():
                sleep(1.5)
                traceback = key.fileobj.read1().decode()
                if not traceback:
                    exit()
                parsedTraceback = str(traceback).split("\n")

                # Visual / Demo purposes
                print(parsedTraceback)
                print(traceback, end="", file=sys.stderr)

                if str(traceback).find("ModuleNotFoundError:") != -1:
                    self.filterBugReport.appendFile("black.list", scriptName)
                    raise Exception(f'{scriptName}, module is not found!')
                elif str(traceback).find("No such file or directory") != -1:
                    raise Exception(f'{scriptName} script is not found!')

                self.issueBugReport(traceback=traceback, parsedError=parsedTraceback)

    def issueBugReport(self, traceback, parsedError):
        """
        issues bug report according to config file
        """
        if str(parsedError[0]).__contains__("Traceback (most recent call last)"):
            title = "location -- " + str(parsedError[1])
        else:
            title = "location -- " + str(parsedError[0])
        bugReport = bugRecordDTO.BugRecordDTO(title=title,
                                              tracebackInfo=traceback, resolved=False)
        githubIssueToSend = githubIssue.GithubIssue(title=title, body=traceback, labels="bug")
        self.database.list_insert(bugRecordDTO=bugReport)
        if self.configOptions.getConfig(key="send_github_issue"):
            self.github.createIssue(githubIssueToSend)
        if self.configOptions.getConfig(key="send_email"):
            self.sendEmail(str(bugReport))


if __name__ == '__main__':
    execute = AutoBugTracker()
    execute.run()
