from read_config import *
import os
import io
import sys

BUGTRACKER = ".autobug.ini"

class testReadConfig():
    def __init__(self):
        print("testing")

    def testInit(self):
        configClass = readConfig(user_info=None)
        test = os.path.join(Path.home(), BUGTRACKER)
        if Path(test).is_file() is True:
            print("TEST SUCCESS: Executed successfully. Created init/default file successfully. \n")
            os.remove(Path(test))
        else:
            print("TEST FAILED: Encountered an error/exception. \n")
            os.remove(Path(test))

    def testGetConfig(self):
        configClass = readConfig(user_info=None)
        test = configClass.getConfig(key='name')
        print("KEY RETURNS: " + str(test))
        if not test is None:
            print("TEST SUCCESS: Config found successfully. Key is valid. \n")
            os.remove(Path(os.path.join(Path.home(), BUGTRACKER)))
        else:
            print("TEST FAILED: Config not found. Given key is invalid. \n")
            os.remove(Path(os.path.join(Path.home(), BUGTRACKER)))

        test = configClass.getConfig(key='invalid')
        print("KEY RETURNS: " + str(test))
        if test is None:
            print("TEST SUCCESS: Config not found. Key is invalid. \n")
        else:
            print("TEST FAILED: Config found successfully. Key is valid. \n")
            os.remove(Path(os.path.join(Path.home(), BUGTRACKER)))


    def testShowConfig(self):
        configClass = readConfig(user_info=None)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        configClass.showConfig()
        sys.stdout = sys.__stdout__

        expectedOutput = "{'name': {'first': 'John', 'last': 'Doe'}, 'email': 'johndoe@doe.com', 'placeholder1': '', " \
                         "'placeholder2': '', 'placeholder3': '', 'placeholder4': '', 'placeholder5': ''}\n"
        if capturedOutput.getvalue() == expectedOutput:
            print("TEST SUCCESS: Print valid. \n")
            os.remove(Path(os.path.join(Path.home(), BUGTRACKER)))
        else:
            print("TEST FAILED: Print invalid. \n")
            os.remove(Path(os.path.join(Path.home(), BUGTRACKER)))


    def run(self):
        self.testInit()
        self.testGetConfig()
        self.testShowConfig()


if __name__ == '__main__':
    test_run = testReadConfig()
    test_run.run()
