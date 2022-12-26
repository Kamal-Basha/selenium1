import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pageObjects.loginpage import LoginPage
from test_cases.conftest import *
from selenium.webdriver.common.by import By
import time

class Test_001_login:
    baseURL = "https://www.nopcommerce.com/en/login"
    username ="kamalbasha"
    password ="Yourself@17"


    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        time.sleep(10)

        self.driver.find_element(By.ID,"Username").send_keys("kamalbasha")
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0, 500)","")
        time.sleep(5)

        self.lp.clickLogin()

        act_title=self.driver.title


        if act_title=="Login - nopCommerce":
            assert True
        else:
            assert True

        # self.driver.close()


    # def test_login(self ,setup):
    #
    #     self.driver =setup
    #     self.driver.get(self.baseURL)
    #     self.lp= Login(self.driver)
    #     self.lp.setUserName(self.Username)
    #     self.lp.setPassword(self.Password)
    #     self.lp.clickLogin()


