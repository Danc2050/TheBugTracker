import os
import logging
from datetime import date


class DebugLogFile:
    def __init__(self, configOptions):
        self.createDebugFlag = configOptions.getConfig("create_debug_log")
        self.overwriteFileFlag = configOptions.getConfig("overwrite_previous_entry")
        self.fileToWrite = configOptions.getConfig("log_file")
        self.newFile = str(date.today()) + "_debugLogFile.txt"

    def writeToFile(self, message):
        try:
            if self.createDebugFlag is True:
                if self.overwriteFileFlag is True:
                    if os.path.isfile(self.newFile):
                        DebugLogFile.__logMessage__(message, self.newFile, 'a')
                    else:
                        DebugLogFile.__logMessage__(message, self.newFile, 'w')
                else:
                    if self.fileToWrite is None:
                        raise Exception("Configuration Missing Logs File Name")
                    if os.path.isfile(self.fileToWrite):
                        DebugLogFile.__logMessage__(message, self.fileToWrite, 'a')
                    else:
                        DebugLogFile.__logMessage__(message, self.fileToWrite, 'w')
        except Exception as e:
            raise Exception("Error: " + str(e))

    @staticmethod
    def __logMessage__(message, file, writeMode):
        logging.basicConfig(
            filename=file,
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.DEBUG,
            filemode=writeMode,
            datefmt='%Y-%m-%d %H:%M:%S')
        logging.debug(message)
