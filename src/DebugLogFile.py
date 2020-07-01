import os
import logging
from datetime import date


class DebugLogFile:
    def __init__(self, configOptions):
        """
        Initializes the debug log file with the needed configs from the configurations file
        :param configOptions: The configurations from user supplies settings in
        ".autobug.ini"
        """
        self.createDebugFlag = configOptions.getConfig("create_debug_log")
        self.overwriteFileFlag = configOptions.getConfig("overwrite_previous_entry")
        self.fileToWrite = configOptions.getConfig("log_file")
        self.newFile = str(date.today()) + "_debugLogFile.txt"

    def writeToFile(self, message):
        """
        Writes the message to the log file, will either append to the current days
        logs or create a new file. The behavior is all dependent on the configurations
        :param message: message to be logged
        :return: raises an exception if any error occur while writing to log file
        """
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
        """
        Formats information to log

        :param message: message to be logged
        :param file: file to be logged at
        :param writeMode: append or write
        :return: message in logging format
        """
        logging.basicConfig(
            filename=file,
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.DEBUG,
            filemode=writeMode,
            datefmt='%Y-%m-%d %H:%M:%S')
        logging.debug(message)
