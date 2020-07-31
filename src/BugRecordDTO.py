class BugRecordDTO:
    def __init__(self, title=None, tracebackInfo=None, resolved=None, version=None):
        self.title = title
        self.tracebackInfo = tracebackInfo
        self.resolved = resolved
        self.version = version

    def __repr__(self):
        return "Bug Title: " + self.title + "\n" + "Bug TracebackInfo: " + str(
            self.tracebackInfo) + "\n" + "Bug Resolved: " + str(self.resolved) + "\n" + "Version: " + str(self.version)
