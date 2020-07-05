import subprocess
from src.ExecuteUserScript import ExecuteUserScript
import src.ReadConfig as readConfig
import src.DebugLogFile as debugLogFile


class testScript:
    def __init__(self):
        print("testing")

    def testWorkingScript(self, tClass):
        print("Test executing executeScript with a working script")
        out = tClass.executeScript(scriptName="../tests/WorkingTestScript.py")
        if type(out) != list and type(out) != str:
            print("testWorkingScript: PASS")
            return
        print("testWorkingScript: FAILED")

    def testMissingModule(self, tClass):
        print("Test executing executeScript with a script that is missing a module.")
        out = tClass.executeScript(scriptName="../tests/MissingModuleTestScript.py")
        if type(out) == str:
            if out == 'module is not found!':
                print("testMissingModule: PASS")
                return
        print("testMissingModule: FAILED")

    def testMissingFile(self, tClass):
        print("Test executing executeScript with a missing script file")
        out = tClass.executeScript(scriptName="../tests/Nada.py")
        if type(out) == str:
            if out == 'script is not found!':
                print("testMissingFile: PASS")
                return
        print("testMissingFile: FAILED")

    def testListenWorkingScript(self, tClass):
        print("Test executing workingUserScript with a working script file")
        out = tClass.listenExecuteScript(scriptName="../tests/WorkingTestScript.py")
        if type(out) is subprocess.Popen:
            if out.poll() is not None:
                out.kill()
            print("testListenWorkingScript: PASS")
            return
        print("testListenWorkingScript: FAIL")

    def testListenMissingModuleScript(self, tClass):
        print("Test executing listenExecuteScript with a missing module in script")
        out = tClass.listenExecuteScript(scriptName="../tests/MissingModuleTestScript.py")
        if type(out) is str:
            if out == 'module is not found!':
                print("testListenMissingModuleScript: PASS")
                return
        print("testListenMissingModuleScript: FAIL")

    def testListenMissingFileScript(self, tClass):
        print("Test executing listenExecuteScript with a missing script file")
        out = tClass.listenExecuteScript(scriptName="../tests/Nada.py")
        if type(out) is str:
            if out == 'script is not found!':
                print("testListenMissingFileScript: PASS")
                return
        print("testListenMissingFileScript: FAIL")

    def run(self, tClass):
        self.testWorkingScript(tClass=tClass)
        self.testMissingModule(tClass=tClass)
        self.testMissingFile(tClass=tClass)
        self.testListenWorkingScript(tClass=tClass)
        self.testListenMissingModuleScript(tClass=tClass)
        self.testListenMissingFileScript(tClass=tClass)


if __name__ == '__main__':
    configOptions = readConfig.readConfig()
    logs = debugLogFile.DebugLogFile(configOptions)
    test_run = testScript()
    test_run.run(tClass=ExecuteUserScript(configOptions=configOptions, logs=logs))

