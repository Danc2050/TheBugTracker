from debugLogFile import *
import os
import io
import sys

message1 = "\n[This is a placeholder for when a new file is created for the debug log file]"
message2 = "\n[append this message to existing file]"
message3 = "\n[This message is to overwrite the existing file]"


class testdebugLogFile():
    def test(self):
        test = debugLogFile()
        test.writeToFile(message2)


if __name__ == '__main__':
    test_run = testdebugLogFile()
    test_run.test()

