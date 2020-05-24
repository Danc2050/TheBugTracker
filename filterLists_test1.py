from filterLists import *
import os



WHITE_TESTFILE = "whitelist.txt"
BLACK_TESTFILE = "blacklist.txt"
BUG_TESTFILE = "bug_report.txt"


class testFilterBugReport():
	def	__init__(self):
		print("Testing Filter Bug Report")

	def testInit(self):
		print("Test Case 1")
		try:
			os.remove(WHITE_TESTFILE)
			os.remove(BLACK_TESTFILE)
			os.remove(BUG_TESTFILE)
		except Exception:
			print("Test files do not exist in current dir")
		fil = filterBugReport()
		fil.create_new_report()
		try:
			f1 = open(WHITE_TESTFILE,'r')
			f2 = open(BLACK_TESTFILE,'r')
			f3 = open(BUG_TESTFILE,'r')
		except IOError:
			print("Test Case 1 Pass, test files does not exists")
		print('Test Case 2')
		f1 = open(WHITE_TESTFILE,"w")
		f2 = open(BLACK_TESTFILE,"w")
		f3 = open(BUG_TESTFILE,"w")
		f1.write("White1\n\n")
		f2.write("Black1\n\n")
		f3.write("FG\n\n")
		f1.close()
		f2.close()
		f3.close()
		fil = filterBugReport()
		fil.filter_process()
		fil.create_new_report()
		#f3 = open(BUG_TESTFILE,'r')
		#st = f3.read(1)
		#print(st)
		#f3.close()

if __name__ == '__main__':
	test = testFilterBugReport()
	test.testInit()