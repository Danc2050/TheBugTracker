import traceback


class ExecuteUserScript(object):

    def executeScript(self, scriptName):
        ''' Return list of traceback stack

            execute user script, takes script to be execute as an argument
            either graceful execution or bug information such as capturing traceback
        '''
        try:
            return exec(open(scriptName).read())
        except FileNotFoundError:
            print(f'{scriptName} script is not found!')
        except ModuleNotFoundError as e:
            print(f'{e}, module is not found!')
            #Blacklist the script with missing module and notify user. Do not submit Bug!
        except:
            print(f'{scriptName} did not exit gracefully, Submit a Bug!"')
            #traceback.print_exc(file=sys.stdout)
            return list(traceback.extract_stack())