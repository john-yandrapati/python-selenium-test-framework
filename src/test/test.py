import errno
import os
from os.path import dirname

class Test:

    def getHTMLReport(self):
        try:
            dirPath = "/Users/johnyandrapati/PycharmProjects/testFrameworks/tox_test/target"
            try:
                os.makedirs(dirPath)
                file = "/Users/johnyandrapati/PycharmProjects/testFrameworks/tox_test/target/HTMLTestReport.html"

                mode = 'a' if os.path.exists(file) else 'w+'
                with open(file, mode) as f:
                    f.write("Test Report File")
            except:
                raise  Exception
        except:
            print("done")


x = Test()
x.getHTMLReport()