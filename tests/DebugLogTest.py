from src.DebugLogFile import *

message1 = "\n[This is a placeholder for when a new file is created for the debug log file]"
message2 = "\n[append this message to existing file]"
message3 = "\n[This message is to overwrite the existing file]"


class DebugLogTest:
    def test(self):
        test = debugLogFile()
        test.writeToFile(message1)


if __name__ == '__main__':
    test_run = DebugLogTest()
    test_run.test()

