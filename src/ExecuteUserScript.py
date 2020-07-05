import sys
import traceback
import subprocess


class ExecuteUserScript(object):
    def __init__(self, configOptions, logs):
        self.configOptions = configOptions
        self.logs = logs

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
            return exec(open(scriptName).read())
        except FileNotFoundError:
            print(f'{scriptName} script is not found!')
            self.logs.writeToFile(message=self.captureTraceback())
            return 'script is not found!'
        except ModuleNotFoundError as e:
            print(f'{e}, module is not found!')
            self.logs.writeToFile(message=self.captureTraceback())
            # Blacklist the script with missing module and notify user. Do not submit Bug!
            return 'module is not found!'
        except:
            print(f'{scriptName} did not exit gracefully, Submit a Bug!"')
            return self.captureTraceback()

    def listenExecuteScript(self, scriptName):
        """
        returns the script as a child process
        """
        p = subprocess.Popen([scriptName], stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                             shell=True)
        _, err = p.communicate()
        errors = str(err).split('\\n')  # err is raw string
        if str(err).find("ModuleNotFoundError:") != -1:
            print(f'{scriptName}, module is not found!')
            self.logs.writeToFile(message=errors)
            return 'module is not found!'
        elif p.returncode == 127:
            print(f'{scriptName} script is not found!')
            self.logs.writeToFile(message=errors)
            return 'script is not found!'
        elif p.returncode == 1:
            print(f'{scriptName} did not exit gracefully, Submit a Bug!"')
            return errors
        return p
