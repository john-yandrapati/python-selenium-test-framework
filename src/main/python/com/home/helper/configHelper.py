"""This class is for Config Files"""
from src.main.python.com.home.helper.helperInterface import iHelperInterface as HI
import configparser


class ConfigHelperClass(HI):

    def __init__(self, fileHelper):
        self.fileHelper = fileHelper

    def dummyMethod(self):
        pass

    def getConfigProperties(self):
        config = configparser.ConfigParser()
        config.read(self.fileHelper.getConfigFilePath())
        return config


    def getConfigSectionMap(self, section):
        dict1 = {}
        Config = self.getConfigProperties()
        options = Config.options(section)
        for option in options:
            try:
                dict1[option] = Config.get(section, option).upper()
                if dict1[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1


    def getValue(self, section, key):
        dictionary = self.getConfigSectionMap(section)
        for i in dictionary.keys():
            if i.upper() == key.upper():
                keyValue = dictionary[i].lower()
        return keyValue