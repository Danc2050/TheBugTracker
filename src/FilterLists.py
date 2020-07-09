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
        # print("***Filtering bug reports with white/black lists***\n")
        if path.exists("black.list"):
            self.blackfile = open("black.list", 'r')
            self.black_data = self.blackfile.read().split(DELIMITER)
            # blackfile.close()
        else:
            self.createBlackList()
        if path.exists("white.list"):
            self.whitefile = open("white.list", 'r')
            self.white_data = self.whitefile.read().split(DELIMITER)
            # whitefile.close()
        else:
            self.createWhiteList()
        if path.exists("bugs.list"):
            bugfile = open("bugs.list", 'r')
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
        if path.exists("bugs.list"):
            with open("bugs.list", 'w') as newBugReport:
                writer = csv.writer(newBugReport, delimiter='\n')
                writer.writerow(self.bugs)

    def createWhiteList(self):
        '''
        Return the data in the white list

        create a new white list
        '''
        if not path.exists("white.list"):
            self.whitefile = open("white.list", 'w+')
            self.white_data = self.whitefile.read().split(DELIMITER)
            return self.white_data

    def createBlackList(self):
        '''
        Return the data in the black list

        create a new black list
        '''
        if not path.exists("black.list"):
            self.blackfile = open("black.list", 'w+')
            self.black_data = self.blackfile.read().split(DELIMITER)
            return self.black_data

    def isScriptBlackedOrWhited(self, fileType, userScript):
        '''
        Return boolean

        Does check for the existence of script being execute in either of the white or black list
        '''
        fileType = ''.join(fileType)
        if userScript in fileType:
            return True
        return False

    def appendFile(self, files, data):
        '''
        Does append the lists according to the file type passed
        '''
        if files == "black.list":
            if not (self.isScriptBlackedOrWhited(self.black_data, data)):
                with open("black.list", 'a+') as blackFile:
                    blackFile.write(data + "\n")
        elif files == "white.list":
            if not (self.isScriptBlackedOrWhited(self.white_data, data)):
                with open("white.list", 'a+') as whitefile:
                    whitefile.write(data + "\n")
