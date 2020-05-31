from os import path
import csv

# individual bugs in each file would need to be separated by two new lines [YOU CAN CHANGE DELIMITER IF YOU WANT]

DELIMITER = '\n\n'


class filterBugReport:
    def __init__(self):
        """
        put contents of blackfile, whitefile, and bug report into arrays/columns according to delimiter (???)
        does not do anything if there is no files that exist
        """
        print("***Filtering bug reports with white/black lists***\n")
        if path.exists("blacklist.txt"):
            blackfile = open("blacklist.txt", 'r')
            self.black_data = blackfile.read().split(DELIMITER)
            blackfile.close()
        if path.exists("whitelist.txt"):
            whitefile = open("whitelist.txt", 'r')
            self.white_data = whitefile.read().split(DELIMITER)
            whitefile.close()
        if path.exists("bug_report.txt"):
            bugfile = open("bug_report.txt", 'r')
            self.bugs = bugfile.read().split(DELIMITER)
            bugfile.close()

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
                writer = csv.writer(newBugReport, delimiter='\n')
                writer.writerow(self.bugs)

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
