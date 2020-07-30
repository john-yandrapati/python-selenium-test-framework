from selenium.webdriver.common.keys import Keys

class GoogleSteps:

    def __init__(self, config, excelHelper, homePage):
        self.config = config
        self.excelHelper = excelHelper
        self.homePage = homePage

    def getNewListData(self):
        testData = self.excelHelper.getTestData('Sheet2')
        testData.pop(0)
        return testData


    def step1(self, driver):
        for i in self.getNewListData():
            driver.get(self.homePage.returnBrowserURL())
            search = driver.find_element_by_name(self.homePage.returnSearchBoxElement())
            search.send_keys(i)
            search.send_keys(Keys.RETURN)


    def step2(self, driver):
        for i in self.getNewListData():
            driver.get(self.homePage.returnBrowserURL())
            search = driver.find_element_by_name(self.homePage.returnSearchBoxElement())
            search.send_keys(i)
            search.send_keys(Keys.RETURN)