import subprocess


# Test script broken with Error : src/ExecuteUserScript.py: No such file or directory
class testScript():
    def __init__(self):
        print("testing")

    def testWorkingScript(self):
        check = subprocess.check_output('src/ExecuteUserScript.py -S tests/WorkingTestScript.py', shell=True, text=True)
        test = check.find('Traceback')
        if test == -1:
            print("Executed workingUserScript successfully. TEST PASSED")
        else:
            print("workingUserScript did not execute. TEST FAILED.")

    def testBrokenScript(self):
        check = subprocess.check_output('src/ExecuteUserScript.py -S tests/BrokenTestScript.py', shell=True, text=True)
        test = check.find('Traceback')
        if test != -1:
            print("Executed brokenTestScript and Traceback was found. TEST PASSED")
        else:
            print("Executed brokenTestScript and Traceback was not found. TEST FAILED.")

    def testCommandLine(self):
        try:
            print("Test executing workingUserScript without -S, should fail.")
            subprocess.check_output('src/ExecuteUserScript.py tests/WorkingTestScript.py', shell=True, text=True,
                                    stderr=True)
        except:
            print("test did fail without -S. TEST PASSED")
            return
        print("Test passed without -S in command line arguments. TEST FAILED")

    def run(self):
        self.testWorkingScript()
        self.testBrokenScript()
        self.testCommandLine()


if __name__ == '__main__':
    test_run = testScript()
    test_run.run()
