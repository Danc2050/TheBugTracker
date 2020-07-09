import sys
import traceback
from src.FilterLists import filterBugReport
import subprocess

FILE_NOT_FOUND_RETURN_CODE = 127
CHILD_PROCESS_OUT_TIMEOUT = 60

class ExecuteUserScript(object):
    def __init__(self, configOptions, logs):
        self.configOptions = configOptions
        self.logs = logs
        self.filterBugReport = filterBugReport()

    def captureTraceback(self):
        """Display the exception that just occurred.

        return:
            list with the traceback

        """
        try:
            type, value, tb = sys.exc_info()
            sys.last_type = type
            sys.last_value = value
            sys.last_traceback = tb
            tblist = traceback.extract_tb(tb)
            del tblist[:1]  # removing AutoBugTracker stack line
            tracebackList = traceback.format_list(tblist)
            if tracebackList:
                tracebackList.insert(0, "Traceback (most recent call last):\n")
            tracebackList[len(tracebackList):] = traceback.format_exception_only(type, value)
        finally:
            tblist = tb = None
        return tracebackList

    def executeScript(self, scriptName):
        """ Execute parent program

            execute user script, takes script to execute as an argument
            either graceful execution or bug information such as capturing traceback

        Return:
             list of traceback stack if user program crash

        """
        try:
            exec(open(scriptName).read())
            self.filterBugReport.appendFile("white.list", scriptName)
        except FileNotFoundError:
            print(f'{scriptName} script is not found!')
            self.logs.writeToFile(message=self.captureTraceback())
            return 'script is not found!'
        except ModuleNotFoundError as e:
            print(f'{e}, module is not found!')
            self.logs.writeToFile(message=self.captureTraceback())
            self.filterBugReport.appendFile("black.list", scriptName)
            return 'module is not found!'
        except:
            print(f'{scriptName} did not exit gracefully, Submit a Bug!"')
            return self.captureTraceback()

    def listenExecuteScript(self, scriptName):
        """
        returns the script as a child process
        """
        p = subprocess.Popen([scriptName],
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             shell=True)
        try:
            out, err = p.communicate(timeout=CHILD_PROCESS_OUT_TIMEOUT)
        except Exception as e:
            raise e
        errors = str(err).split('\\n')  # err is raw string
        if str(err).find("ModuleNotFoundError:") != -1:
            print(f'{scriptName}, module is not found!')
            self.logs.writeToFile(message=errors)
            return 'module is not found!', errors, None
        elif p.returncode == FILE_NOT_FOUND_RETURN_CODE:
            print(f'{scriptName} script is not found!')
            self.logs.writeToFile(message=errors)
            return 'script is not found!', errors, None
        elif FILE_NOT_FOUND_RETURN_CODE > p.returncode > 0:
            print(f'{scriptName} did not exit gracefully, Submit a Bug!"')
            return out, errors, None
        return out, None, p
