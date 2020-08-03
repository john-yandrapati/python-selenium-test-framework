from src.main.scripts.htmlReport.HTMLTestRunner import HTMLTestRunner
from src.main.python.com.home.helper.helperInterface import iHelperInterface as HI
from os.path import dirname
from pathlib import Path


class HTMLReportHelper(HI):

    def __init__(self, fileHelper):
        self.fileHelper = fileHelper

    def dummyMethod(self):
        pass

    def getHTMLReport(self, testSuite):
       try:
            dirPath = dirname(dirname(dirname(dirname(dirname(dirname(dirname(__file__)))))))+"/target"

            Path(dirPath).mkdir(parents=True, exist_ok=True)
            file = "HTMLTestReport.html"
            filePath = dirPath + "/" + file

            filename = Path(filePath)
            filename.touch(exist_ok=True)

            if filePath == "":
                fp = open(filename, 'wb')
                # Define the title and description of the test report
                runner = HTMLTestRunner(stream=fp, title=u'Test Report for Google Test',
                                        description=u'Test Results for Sample Tests')
                runner.run(testSuite)
                fp.close()
            else:
                fp = open(filename, 'wb')
                # Define the title and description of the test report
                runner = HTMLTestRunner(stream=fp, title=u'Test Report for Google Test',
                                        description=u'Test Results for Sample Tests')
                runner.run(testSuite)
                fp.close()
       except:
           raise Exception