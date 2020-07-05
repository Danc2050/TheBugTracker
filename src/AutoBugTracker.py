import argparse
import src.ExecuteUserScript as executeUserScript
import src.GithubIntegration as githubIntegration
import src.ReadConfig as readConfig
import src.DebugLogFile as debugLogFile
import src.DatabaseScript as initializeDatabaseScript
import src.EmailUsers as emailUsers


class AutoBugTracker(object):
    def __init__(self):
        print("***Auto Bug Tracker***\n")
        # Initialize database
        self.database = initializeDatabaseScript.Database()
        self.dbInitialized = False
        # Gets configuration file, if non existent it will create one
        self.configOptions = readConfig.readConfig()
        self.logs = debugLogFile.DebugLogFile(self.configOptions)
        self.execute = executeUserScript.ExecuteUserScript(self.configOptions, self.logs)
        self.github = None
        self.email = None

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
        if not self.dbInitialized:
            try:
                self.database.connect(server_params="postgres_server")
                self.database.create_database(database_params="postgres_db")
                self.database.create_table(table_name="Bugs")
            except Exception as e:
                self.logs.writeToFile(str(e))
                return False

            return True

    def emailConfiguration(self):
        """
        Initializes data to email specified user(s). body of report passed to this function.

        :return: email sent
        """
        username = config('USER')
        password = config('KEY')
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

    def initialization(self):
        # Initialize and connect to database
        self.dbInitialized = self.databaseConfiguration()
        # Initialize project with github
        self.github = self.githubConfiguration()
        # Initialize email information
        self.email = self.emailConfiguration()

    def run(self):
        """
        Return list of traceback if the script did not exist gracefully

        it does sort functions of the class in logical order for execution.
        """
        github = self.githubConfiguration()
        scriptName = self.parsingCommandLineArguments()['userScript']
        traceBackOfParentProgram = self.execute.executeScript(scriptName)
        if (type(traceBackOfParentProgram) is list):
            self.database.list_insert(("", "", traceBackOfParentProgram, False))
            self.sendEmail(traceBackOfParentProgram)


if __name__ == '__main__':
    execute = AutoBugTracker()
    execute.initialization()
    execute.run()
