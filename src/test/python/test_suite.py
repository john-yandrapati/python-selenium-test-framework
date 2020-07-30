from unittest import TestSuite
import unittest
from src.main.python.com.home.helper.fileHelper import FileHelperClass
from src.main.python.com.home.helper.reportHelper import HTMLReportHelper
from src.test.python.test_tests import UnitTestClass


class suite(TestSuite):

    def test_testSuite(self):
        suite1 = TestSuite()
        x = UnitTestClass('test_TestCase1')
        print(x)
        suite1.addTest(x)
        suite1.addTest(UnitTestClass('test_TestCase2'))
        return suite1

    def test_runTests(self):
        file = FileHelperClass()
        htmlReport = HTMLReportHelper(file)
        htmlReport.getHTMLReport(suite().test_testSuite())

if __name__ == '__main__':
    unittest.main()
    suite().test_runTests()