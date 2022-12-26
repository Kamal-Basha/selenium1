from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
        driver = webdriver.Chrome(executable_path="C:\\projects\\pythonselenium\\browser\\chromedriver.exe")
        driver.maximize_window()
        return driver

