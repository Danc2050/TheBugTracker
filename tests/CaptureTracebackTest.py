from src.AutoBugTracker import AutoBugTracker

"""
    This QA file/program requires:
        - edits on config file (.autobug.ini):
            - change values for preferred delivery method (email, debug, database/github)
        - docker for local machines OR database functionality on google cloud
"""


class testCaptureTraceback:
    def __init__(self):
        print("testing")

    def testRun(self):
        """
        - test if sending issue to database/github repo is successful
        - test if sending issue to debug log file is successful
        - test if sending issue to an email is successful
        """
        test = AutoBugTracker()
        test.run()

    def run(self):
        self.testRun()


if __name__ == '__main__':
    test_run = testCaptureTraceback()
    test_run.run()
