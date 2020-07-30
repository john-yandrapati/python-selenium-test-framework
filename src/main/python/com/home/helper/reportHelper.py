import errno
from src.main.scripts.htmlReport.HTMLTestRunner import HTMLTestRunner
from src.main.python.com.home.helper.helperInterface import iHelperInterface as HI
import os
from os.path import dirname


class HTMLReportHelper(HI):

    def __init__(self, fileHelper):
        self.fileHelper = fileHelper

    def dummyMethod(self):
        pass

    def getHTMLReport(self, testSuite):
        try:
            filepath = self.fileHelper.getHTMLReportPath()
            dirPath = "/Users/johnyandrapati/PycharmProjects/testFrameworks/tox_test/target"
                #dirname(dirname(dirname(dirname(dirname(dirname(__file__))))))+"target"
            try:
                os.makedirs(dirPath)
                file = "/Users/johnyandrapati/PycharmProjects/testFrameworks/tox_test/target/HTMLTestReport.html"

                mode = 'a' if os.path.exists(file) else 'w+'
                with open(file, mode) as f:
                    f.write("Test Report File")
                    runner = HTMLTestRunner(stream=f, title=u'Test Report for Google Test',
                                            description=u'Test Results for Sample Tests')
                    runner.run(testSuite)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise


            # if filepath == "":
            #     fp = open(filepath, 'w+')
            #     # Define the title and description of the test report
            #     runner = HTMLTestRunner(stream=fp, title=u'Test Report for Google Test',
            #                             description=u'Test Results for Sample Tests')
            #     runner.run(testSuite)
            # else:
            #     fp = open(filepath, 'w+')
            #     # Define the title and description of the test report
            #     runner = HTMLTestRunner(stream=fp, title=u'Test Report for Google Test',
            #                             description=u'Test Results for Sample Tests')
            #     runner.run(testSuite)
        except:
            print(Exception)