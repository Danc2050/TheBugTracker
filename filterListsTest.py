from filterLists import *
import os


WHITE_TESTFILE = "whitelist.txt"
BLACK_TESTFILE = "blacklist.txt"
BUG_TESTFILE = "bug_report.txt"


class testFilterBugReport():
	def __init__(self):
		print("Testing Filter Bug Report")

	def removeTestFiles(self):
		try:
			os.remove(WHITE_TESTFILE)
			os.remove(BLACK_TESTFILE)
			os.remove(BUG_TESTFILE)
		except Exception:
			print()
	def testInit(self):
		"""
        Test Case 1: Test files are not present, no files should be loaded or create during init
		"""
		print("Begin testInit")
		self.removeTestFiles()
		fil = filterBugReport()
		try:
			f1 = open(WHITE_TESTFILE,'r')
			f2 = open(BLACK_TESTFILE,'r')
			f3 = open(BUG_TESTFILE,'r')
		except Exception:
			print("Test Case 1 Pass")
			print("End testInit")
			return
		print("Test Case 1 Fail")
		raise Exception
		print("End testInit")

	def testCheckInBoth(self):
		"""
    Test Case 1: White and Black lists share subset, exception should be raised
    Test Case 2: White and Black lists do not share a subset, no exception should be raised
    """
		print("Begin testCheckInBoth")
		self.removeTestFiles()
		f1 = open(WHITE_TESTFILE,"w")
		f2 = open(BLACK_TESTFILE,"w")
		f1.write("Same1\n\n")
		print("Adding item White1 to white list file")
		f2.write("Same1\n\n")
		print("Adding item Black1 to black list file")
		f1.close()
		f2.close()
		fil = filterBugReport()
		try:
			fil.check_in_both()
		except Exception:
			print("Test Case 1 Pass")
			self.removeTestFiles()
			f1 = open(WHITE_TESTFILE,"w")
			f2 = open(BLACK_TESTFILE,"w")
			f1.write("WHITE1\n\n")
			print("Adding item White1 to white list file")
			f2.write("BLACK1\n\n")
			print("Adding item Black1 to black list file")
			f1.close()
			f2.close()
			fil = filterBugReport()
			try:
				fil.check_in_both()
			except Exception:
				print("Test Case 2 Fail")
				raise Exception
				return
			print("Test Case 2 Pass")
			print("End testCheckInBoth")
			return
		print("Test Case 1 Fail")
		print("End testCheckInBoth")
		raise Exception
		return

	def testFilterProcess(self):
		"""
    Test Case 1: Bug report does contain an item that appears in the black list
		"""
		print("Begin testFilterProcess")
		self.removeTestFiles()
		f1 = open(WHITE_TESTFILE,"w")
		f2 = open(BLACK_TESTFILE,"w")
		f3 = open(BUG_TESTFILE, "w")
		f1.write("Same1\n\n")
		print("Adding item BAD1 to black list file")
		f2.write("BAD1\n\n")
		print("Adding item BAD1 to bug file")
		f3.write("BAD1\n\n")
		f1.close()
		f2.close()
		f3.close()
		fil = filterBugReport()
		fil.filter_process()
		fil.create_new_report()
		found = False
		with open(BUG_TESTFILE,"r") as f4:
			for line in f4:
				if "BAD1" in line:
					found = True
					print(line)
		if found is False:
			print("Test Case 1 PASS")
		else:
			print("Test Case 1 Fail")
			raise Exception
		print("End testFilterProcess")

	def testCreateNewReport(self):
		"""
    Test Case 1: Test files present, bug report should get new white list items and no black list items,
    it should create new bug report file with the white list items
		"""
		print("Begin testCreateNewReport")
		f1 = open(WHITE_TESTFILE,"w")
		f2 = open(BLACK_TESTFILE,"w")
		f3 = open(BUG_TESTFILE,"w")
		f1.write("White1\n\n")
		print("Adding item White1 to white list file")
		f2.write("Black1\n\n")
		print("Adding item Black1 to black list file")
		f3.write("FG\n\n")
		print("Adding item FG to bug report file")
		f1.close()
		f2.close()
		f3.close()
		fil = filterBugReport()
		fil.run()
		found = False
		with open(BUG_TESTFILE,"r") as f4:
			for line in f4:
				if "White" in line:
					found = True
					print(line)
		if found is False:
			print("Test Fail")
			raise Exception
		else:
			print("Test Case 1 Pass")
		print("End testCreateNewReport\n\n\n\n")

if __name__ == '__main__':
	test = testFilterBugReport()
	t = False
	try:
		test.testInit()
		test.testCheckInBoth()
		test.testFilterProcess()
		test.testCreateNewReport()
	except Exception:
		t = True
	if t is False:
		print("All tests passed")