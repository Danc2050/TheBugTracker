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
        '''' Return list of traceback if the script did not exist gracefully

            it does sort functions of the class in logical order for execution.
        '''
        scriptName = self.parsingCommandLineArguments()['userscript']
        execute = self.execute.executeScript(scriptName)
        return execute if(type(execute) is list) else None
        # return list of traceback to be included in user email


if __name__ == '__main__':
    execute = autoBugTracker()
    execute.run()
