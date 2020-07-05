import argparse
import os
from datetime import time

import src.ExecuteUserScript as ExecuteUserScript
import src.GithubIntegration as githubIntegration
import src.GithubIssue as githubIssue
import src.ReadConfig as readConfig
import src.DebugLogFile as debugLogFile
import src.DatabaseScript as initializeDatabaseScript
import src.EmailUsers as emailUsers
import src.BugRecordDTO as bugRecordDTO


class AutoBugTracker(object):
    def __init__(self):
        print("***Auto Bug Tracker***\n")
        # Gets configuration file, if non existent it will create one
        self.configOptions = readConfig.readConfig()
        self.logs = debugLogFile.DebugLogFile(self.configOptions)
        # Initialize database
        self.database = initializeDatabaseScript.Database(self.logs)
        self.databaseConfiguration()
        self.execute = ExecuteUserScript.ExecuteUserScript(self.configOptions, self.logs)
        self.github = self.githubConfiguration()
        self.email = self.emailConfiguration()

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
        Return list of traceback if the script did not exist gracefully

        it does sort functions of the class in logical order for execution.
        """
        scriptName = self.parsingCommandLineArguments()['userScript']
        traceBackOfParentProgram = self.execute.executeScript(scriptName)
        if type(traceBackOfParentProgram) is list:
            self.issueBugreport(traceBackOfParentProgram)

    def listenRun(self):
        """
        Listen to invoke script for any bugs to report
        """
        scriptName = self.parsingCommandLineArguments()['userScript']
        process = self.execute.liveExecuteScript(scriptName)
        if type(process) is not list and type(process) is not str(process):
            while process.poll is None:
                _, err = process.communicate()
                if err:
                    errors = str(err).split('\\n')
                    self.issueBugreport(traceBack=errors)
                    time.sleep(.5)

    def issueBugreport(self, traceBack):
        """
        issues bug report according to config file
        """
        title = "Bug location" + traceBack[0]
        description = "Bug Error" + traceBack[1]
        bugReport = bugRecordDTO.BugRecordDTO(title=title, description=description,
                                              tracebackInfo=traceBack, resolved=False)
        githubIssueToSend = githubIssue.GithubIssue(title=title, body=str(bugReport), labels="bug")
        self.database.list_insert(bugRecordDTO=bugReport)
        if self.configOptions.getConfig(key="send_github_issue"):
            self.github.createIssue(githubIssueToSend)
        if self.configOptions.getConfig(key="send_email"):
            self.sendEmail(str(bugReport))


if __name__ == '__main__':
    execute = AutoBugTracker()
    execute.run()
