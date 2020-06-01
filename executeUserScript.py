import sys
import traceback


class executeUserScript(object):

    def executeScript(self, scriptName):
        ''' Return a null

            execute user script, takes one argument
            either graceful execution or bug information such as capturing traceback
        '''
        try:
            return exec(open(scriptName).read())
        except FileNotFoundError:
            print(f'{scriptName} script is not found!')
        except ModuleNotFoundError as e:
            print(f'{e}, module is not found!')
            #we can blacklist the script with missing module and notify user.
        except:
            print(f'{scriptName} did not exit gracefully, Submit a Bug!"')
            traceback.print_exc(file=sys.stdout)
            # need to capture as much as helpful information about the issue
            # for example: traceback to the triage team
