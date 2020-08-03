import unittest
from src.main.python.com.home.helper.fileHelper import FileHelperClass
from src.main.python.com.home.helper.reportHelper import HTMLReportHelper
from src.test.python.test_tests import UnitTestClass


class suite12:

    def test_testSuite(self):
        suite1 = unittest.TestSuite()
        suite1.addTest(UnitTestClass('test_TestCase1'))
        suite1.addTest(UnitTestClass('test_TestCase2'))
        return suite1

    def test_runTests(self):
        file = FileHelperClass()
        htmlReport = HTMLReportHelper(file)
        htmlReport.getHTMLReport(suite12().test_testSuite())

if __name__ == '__main__':
    suite12().test_runTests()