from selenium import webdriver

class BrowserSetUp:

    driver  = ""

    def __init__(self, fileHelper, configHelper):
        self.fileHelper = fileHelper
        self.configHelper = configHelper


    def setup(self, section, browser):

        mapData = self.configHelper.getConfigSectionMap(section)
        path = ""
        for i in mapData.keys():
            if i == browser:
                path = mapData[browser]

        newPath = self.fileHelper.getRootDir() + path.lower()
        if browser == "chromedriverpath".lower():
            self.driver = webdriver.Chrome(executable_path=newPath)
                #"/Users/johnyandrapati/PycharmProjects/testFrameworks/tox_test/src/main/scripts/drivers/chromedriver")
        else:
            self.driver = webdriver.Firefox
            print("Driver dows not exist")

        return self.driver

    def tearDown(self):
        self.driver.quit()