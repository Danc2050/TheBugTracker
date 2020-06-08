import argparse
import src.ExecuteUserScript as ExecuteUserScript
import src.GithubIntegration as githubIntegration
import src.ReadConfig as readConfig
import src.DebugLogFile as debugLogFile


class AutoBugTracker(object):
    def __init__(self):
        print("***Auto Bug Tracker***\n")
        # Gets configuration file, if non existent it will create one
        self.configOptions = readConfig.readConfig()
        self.logs = debugLogFile.DebugLogFile()
        self.execute = ExecuteUserScript.ExecuteUserScript()

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

    def run(self):
        """
        Return list of traceback if the script did not exist gracefully

        it does sort functions of the class in logical order for execution.
        """
        # Initialize project with github
        github = self.githubConfiguration()
        scriptName = self.parsingCommandLineArguments()['userScript']
        traceBackOfParentProgram = self.execute.executeScript(scriptName)
        # return list of traceback to be included in user email
        # return execute if (type(execute) is list) else None


if __name__ == '__main__':
    execute = AutoBugTracker()
    execute.run()
