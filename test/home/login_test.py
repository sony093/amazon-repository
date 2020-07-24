import time
from selenium import webdriver
import unittest
from page.home.login_page import LoginPage


class LoginTest(unittest.TestCase):
    baseUrl = "https://www.amazon.in/"
    driver = webdriver.Chrome(executable_path="C:\\Users\\Abinash\\Desktop\\DRIVER\\chrome"
                                                       "\\chromedriver.exe")
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get(baseUrl)
    lp = LoginPage(driver)

    def test_ValidLogin(self):
        #self.lp.clickAmazon()
        self.lp.clickLoginLink()
        time.sleep(2)
        self.lp.enterMailId("sonybiswal093@gmail.com")
        time.sleep(2)
        self.lp.clickContinue()
        self.lp.enterPassword("090093")
        time.sleep(2)
        self.lp.clickSubmit()
        time.sleep(2)
        self.lp.clickCart()
        self.lp.clickBuy()
        time.sleep(2)
        #self.driver.quit()

    # @pytest.mark.run(order=1)
    # def test_InvalidLogin(self):
    #     self.lp.clickLoginLink()
    #     time.sleep(2)
    #     self.lp.enterMailId("sonybiswal093@gmail.com")
    #     time.sleep(2)
    #     self.lp.clickContinue()
    #     self.lp.enterPassword("93")
    #     time.sleep(2)
    #     self.lp.clickSubmit()
    #     time.sleep(1)
    #     result = self.lp.verifyLoginFailed()
    #     assert result == True


        #  pytest -v -s test/home/login_test.py
