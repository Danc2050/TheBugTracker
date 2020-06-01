import argparse
import executeUserScript


class autoBugTracker(object):
    def __init__(self):
        print("***Auto Bug Tracker***\n")
        self.execute = executeUserScript.executeUserScript()


    def parsingCommandLineArguments(self):
        '''' Return dictionary

            capture command line arguments.
        '''
        parser = argparse.ArgumentParser()
        parser.add_argument('-S', '--userscript', help='User script Required!', required=True)
        arguments = parser.parse_args()
        return vars(arguments)

    def run(self):
        '''' Return null

            it does sort functions of the class in logical order for execution.
        '''
        scriptName = self.parsingCommandLineArguments()['userscript']
        self.execute.executeScript(scriptName)


if __name__ == '__main__':
    execute = autoBugTracker()
    execute.run()
