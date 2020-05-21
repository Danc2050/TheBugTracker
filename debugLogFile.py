import os
import read_config as readConfig
import logging
from datetime import date


class debugLogFile:
    def __init__(self):
        self.newFile = str(date.today()) + "_debugLogFile.txt"

    def writeToFile(self, message):
        try:
            createDebugFlag = readConfig.readConfig().getConfig("create_debug_log")
            overwriteFileFlag = readConfig.readConfig().getConfig("overwrite_previous_entry")
            fileToWrite = readConfig.readConfig().getConfig("log_file")
            if createDebugFlag.upper() == "TRUE":
                if overwriteFileFlag.upper() == "TRUE":
                    if os.path.isfile(self.newFile):
                        debugLogFile.logMessage(message, self.newFile, 'a')
                    else:
                        debugLogFile.logMessage(message, self.newFile, 'w')
                else:
                    if fileToWrite is None:
                        raise Exception("Configuration Missing Logs File Name")
                    if os.path.isfile(fileToWrite):
                        debugLogFile.logMessage(message, fileToWrite, 'a')
                    else:
                        debugLogFile.logMessage(message, fileToWrite, 'w')
        except Exception as e:
            raise Exception("Error: " + str(e))

    @staticmethod
    def logMessage(message, file, writeMode):
        logging.basicConfig(
            filename=file,
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.DEBUG,
            filemode=writeMode,
            datefmt='%Y-%m-%d %H:%M:%S')
        logging.debug(message)