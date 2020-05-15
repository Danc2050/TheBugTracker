import pandas as pd
import re
from os import path

class filterBugReport():
    def __init__(self):
        """
            put contents of blackfile, whitefile, and bug report into arrays/columns according to delimiter (???)
            does not do anything if there is no files that exist
        """
        print("***Filtering bug reports with white/black lists***\n")
        delimiter = '\n'
        if path.exists("blacklist.txt"):
            self.black_data = pd.read_csv('blacklist.txt', sep=delimiter,
                                          header=None, engine='python')
        if path.exists("whitelist.txt"):
            self.white_data = pd.read_csv('whitelist.txt', sep=delimiter,
                                          header=None, engine='python')
        if path.exists("bug_report.txt"):
            self.bugs = pd.read_csv('bug_report.txt', sep=delimiter,
                                    header=None, engine='python')

    def check_in_both(self):
        """
            check if item in whitelist appears in blacklist before any filtering process
            raise exception if subset is found
        """
        if set(self.white_data).issubset(self.black_data):
            raise Exception("WARNING: Whitelist content also appears in Blacklist content")

    def filter_process(self):
        """
            remove item in bug report that appears in blacklist
            add item in whitelist to bug report (NO DUPLICATES)
        """
        self.bugs = [item for item in self.bugs if item not in self.black_data]
        for item in self.white_data:
            if item not in self.bugs:
                self.bugs.append(item)

    def create_new_report(self):
        """
            create a new bug report array after filtering process
        """
        if path.exists("bug_report.txt"):
            with open("bug_report.txt", 'w') as newBugReport:
                for line in self.bugs:
                    newBugReport.write(" ".join(line) + "\n")

    def run(self):
        """
            executes functions in logical order
        """
        self.check_in_both()
        self.filter_process()
        self.create_new_report()


if __name__ == '__main__':
    execute = filterBugReport()
    execute.run()