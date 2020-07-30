from os.path import dirname
from src.main.python.com.home.helper.helperInterface import iHelperInterface as HI


"""Constants"""

CONFIG_FILE = "test.ini"
EXCEL_FILE = "googleData.xlsx"
HTML_REPORT_FILE = "HTMLTestReport.html"


"""Global Variables"""

PROJECTROOTDIR = ""


"""This class is for Files"""

class FileHelperClass(HI):

    def dummyMethod(self):
        pass


    def getRootDir(self):
        try:
            global PROJECTROOTDIR
            if PROJECTROOTDIR == "":
                PROJECTROOTDIR = dirname(dirname(dirname(dirname(dirname(__file__)))))
                return PROJECTROOTDIR
            elif PROJECTROOTDIR != "":
                PROJECTROOTDIR = dirname(dirname(dirname(dirname(dirname(__file__)))))
                return PROJECTROOTDIR
        except:
            print(Exception)


    def getConfigFilePath(self):
        try:
            rootPath = self.getRootDir()
            if rootPath == PROJECTROOTDIR:
                configFilePath = rootPath + "/resources/" + CONFIG_FILE
                return configFilePath
            else:
                raise Exception("Path is incorrect")
        except:
            raise FileNotFoundError


    def getExcelFilePath(self):
        try:
            rootPath = self.getRootDir()
            if rootPath == PROJECTROOTDIR:
                configFilePath = rootPath + "/resources/" + EXCEL_FILE
                return configFilePath
            else:
                raise Exception("Path is incorrect")
        except:
            raise FileNotFoundError


    def getHTMLReportPath(self):
        try:
            rootPath = self.getRootDir()
            if rootPath == PROJECTROOTDIR:
                print("This is root path for html file" + rootPath)
                htmlReportPath = rootPath + "/resources/" + HTML_REPORT_FILE
                print("This is root path for html file" + htmlReportPath)
                return htmlReportPath
            else:
                raise Exception("Path is incorrect")
        except:
            raise FileNotFoundError