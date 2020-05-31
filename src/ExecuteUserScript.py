import sys
import argparse
import traceback


class executeUserScript:
    def __init__(self):
        print("***Execute User Script***\n")

    def parsingCommandLineArguments(self):
        """'
        capture command line arguments.
        :return
        dictionary
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('-S', '--userscript', help='User script Required!', required=True)
        arguments = parser.parse_args()
        return vars(arguments)

    def executeScript(self, scriptName):
        """
        execute user script, takes one argument
        :param scriptName:
        :return:
        either graceful execution or bug information such as capturing traceback
        """
        try:
            return exec(open(scriptName).read())
        except Exception:
            print("{} did not exist gracefully, Submit a Bug!".format(self.scriptName))
            traceback.print_exc(file=sys.stdout)
            # need to capture as much as helpful information about the issue
            # for example: traceback to the triage team

    def run(self):
        """
        it does sort functions of the class in logical order for execution.
        """
        self.args = self.parsingCommandLineArguments()
        self.scriptName = self.args['userscript']
        self.executeScript(self.scriptName)


if __name__ == '__main__':
    execute = executeUserScript()
    execute.run()
