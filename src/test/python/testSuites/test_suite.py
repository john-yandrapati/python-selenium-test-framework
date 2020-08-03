import unittest
from src.main.python.com.home.helper.fileHelper import FileHelperClass
from src.main.python.com.home.helper.reportHelper import HTMLReportHelper
from src.test.python.testCases.test_tests import UnitTestClass

file = FileHelperClass()

testCase = unittest.TestLoader().loadTestsFromTestCase(UnitTestClass)
testSuite = unittest.TestSuite([testCase])
htmlReport = HTMLReportHelper(file)
htmlReport.getHTMLReport(testSuite)