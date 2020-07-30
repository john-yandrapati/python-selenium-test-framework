from unittest import TestCase
import src.main.python.com.home.di.module as m


class UnitTestClass(TestCase):

    d = m.ModuleClass.googlePage()
    browserType = m.ModuleClass.browerSetUp()


    def open(self):
        return self.browserType.setup('weddriverPaths','chromedriverpath')


    def tearDown(self):
        self.browserType.tearDown()


    def test_TestCase1(self):
        self.d.step1(self.open())

    def test_TestCase2(self):
        self.d.step2(self.open())