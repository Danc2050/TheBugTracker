from src.ReadConfig import readConfig
from pathlib import Path
import os
import io
import sys

BUGTRACKER = ".autobug.ini"


class testReadConfig:
    def __init__(self):
        print("testing")

    def testInit(self):
        """
        CASES:
            When file DOES NOT EXIST:
                test PASSES if default file is created
                test FAILS if we encounter an exception
                    -- FAIL occurs if unable to load config file
            When file EXISTS:
                test PASSES if config path and config valid
                test FAILS if we encounter an exception
                    -- FAIL occurs if unable to load config file
        """
        readConfig()
        test = os.path.join(Path.home(), BUGTRACKER)
        if Path(test).is_file() is True:
            print("TEST SUCCESS: Executed successfully. Created init/default file successfully. Config variables "
                  "initialized. \n")
        else:
            print("TEST FAILED: Encountered an error/exception. \n")

        test = os.path.join(Path.home(), BUGTRACKER)
        if Path(test).is_file() is True:
            print("TEST SUCCESS: Executed successfully. Config variables initialized. \n")
            # os.remove(Path(test))
        else:
            print("TEST FAILED: Encountered an error/exception. \n")
            # os.remove(Path(test))

    def testGetConfig(self):
        """
        CASES:
            When key is VALID:
                test PASSES if configuration value returned
                test FAILS if None returned
            When key is INVALID:
                test PASSES if None returned
                test FAILS if configuration value returned
        """
        configClass = readConfig(user_info=None)
        test = configClass.getConfig(key='first')
        print("KEY RETURNS: " + str(test))
        if test is not None:
            print("TEST SUCCESS: Config found successfully. Key is valid. \n")
            # os.remove(Path(os.path.join(Path.home(), BUGTRACKER)))
        else:
            print("TEST FAILED: Config not found. Given key is invalid. \n")
            # os.remove(Path(os.path.join(Path.home(), BUGTRACKER)))

        test = configClass.getConfig(key='invalid')
        print("KEY RETURNS: " + str(test))
        if test is None:
            print("TEST SUCCESS: Config not found. Key is invalid. \n")
        else:
            print("TEST FAILED: Config found successfully. Key is valid. \n")
            # os.remove(Path(os.path.join(Path.home(), BUGTRACKER)))

    def testShowConfig(self):
        """
        CASES:
            Test PASSES if captured stdout matches expected output
            Test FAILS if captured stdout does not match expected output
        """
        configClass = readConfig(user_info=None)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        configClass.showConfig()
        sys.stdout = sys.__stdout__

        expectedOutput = "{'first': 'John', 'last': 'Doe', 'email': 'johndoe@doe.com', 'create_debug_log': True, " \
                         "'overwrite_previous_entry': False, 'log_file': 'log.txt', 'placeholder4': '', " \
                         "'placeholder5': ''}"

        if capturedOutput.getvalue().strip("\n") is expectedOutput:
            print("TEST SUCCESS: Print valid. \n")
            # os.remove(Path(os.path.join(Path.home(), BUGTRACKER)))
        else:
            print("TEST FAILED: Print invalid. \n")
            # os.remove(Path(os.path.join(Path.home(), BUGTRACKER)))

    def run(self):
        self.testInit()
        self.testGetConfig()
        self.testShowConfig()


if __name__ == '__main__':
    test_run = testReadConfig()
    test_run.run()
