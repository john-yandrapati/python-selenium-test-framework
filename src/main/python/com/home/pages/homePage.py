class HomePageClass:

    def __init__(self, config):
        self.config = config

    SEARCHBOX = ""
    BROWSERURL = ""

    def returnSearchBoxElement(self):
        self.SEARCHBOX = self.config.getValue('googleSearchPageElements', 'mainsearchboxclassname')
        return self.SEARCHBOX

    def returnBrowserURL(self):
        self.BROWSERURL = self.config.getValue('urls', 'google')
        return self.BROWSERURL