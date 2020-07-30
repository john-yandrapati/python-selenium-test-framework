from dependency_injector import containers, providers
from src.main.python.com.home.helper.configHelper import ConfigHelperClass
from src.main.python.com.home.helper.excelHelperClass import ExcelHelperClass
from src.main.python.com.home.helper.fileHelper import FileHelperClass
from src.main.python.com.home.helper.reportHelper import HTMLReportHelper
from src.main.python.com.home.setUp.browserSetUp import BrowserSetUp
from src.main.python.com.home.steps.sampleSteps import GoogleSteps
from src.main.python.com.home.pages.homePage import HomePageClass

class HelperModule(containers.DeclarativeContainer):

      file = providers.Singleton(FileHelperClass)
      config = providers.Singleton(ConfigHelperClass, fileHelper=file)
      excel = providers.Singleton(ExcelHelperClass, fileHelper=file, config=config)
      report = providers.Singleton(HTMLReportHelper, fileHelper=file)



class ModuleClass(containers.DeclarativeContainer):

      homePage = providers.Singleton(HomePageClass, config=HelperModule.config)
      googlePage = providers.Singleton(GoogleSteps, config=HelperModule.config, excelHelper=HelperModule.excel, homePage=homePage)
      browerSetUp = providers.Singleton(BrowserSetUp, fileHelper=HelperModule.file, configHelper=HelperModule.config)
