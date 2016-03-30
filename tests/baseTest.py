import unittest
from selenium import webdriver
from testData.urls import HTMLTable

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.inteval_time = 20

        self.driver=webdriver.Chrome("/Users/suxiaoyin/PycharmProjects/untitled1/chromedriver")

        """
        driver_location = "/Users/suxiaoyin/PycharmProjects/DejaCredits/chromedriver"
        #driver_location = "/Users/jerryzhao/node_modules/appium/node_modules/appium-android-driver/node_modules/appium-chromedriver/chromedriver/mac/chromedriver"
        mobile_emulation = {"deviceName": "Google Nexus 5"}
        options = webdriver.ChromeOptions()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(executable_path=driver_location, chrome_options=options)"""
        self.driver.maximize_window()
        self.driver.implicitly_wait(self.inteval_time)
        self.driver.get(HTMLTable.table_url)


    def tearDown(self):
        self.driver.close()
        #pass
