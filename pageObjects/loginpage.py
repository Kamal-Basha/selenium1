from selenium import webdriver
from selenium.webdriver.common.by import By
class LoginPage:
    textbox_username_id="Username"
    textbox_password_id='Password'
    button_login_xpath="//input[@value='Log in']"
    icon_logout='navigation-top-menu-label navigation-top-menu-label-arrow'


    def __init__(self, driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element(By.ID("Username")).clear()
        self.driver.find_element(By.ID("Username")).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.CLASS_NAME, self.icon_logout).click()



