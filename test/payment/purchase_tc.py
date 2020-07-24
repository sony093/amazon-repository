import time
from selenium import webdriver
import unittest
from page.payment.purchase_page import PaymentPage


class LoginTest(unittest.TestCase):
    baseUrl = "https://www.amazon.in/"
    driver = webdriver.Chrome(executable_path="C:\\Users\\Abinash\\Desktop\\DRIVER\\chrome"
                                                       "\\chromedriver.exe")
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get(baseUrl)
    lp = PaymentPage(driver)

    def test_ValidLogin(self):
        #self.lp.clickAmazon()
        self.lp.clickLoginLink()
        time.sleep(3)
        self.lp.enterMailId("sonybiswal093@gmail.com")
        time.sleep(3)
        self.lp.clickContinue()
        self.lp.enterPassword("090093")
        time.sleep(3)
        self.lp.clickSubmit()
        time.sleep(3)
        # self.lp.enterKeyword("Grocery")
        # self.lp.clickItem()
        # time.sleep(2)
        # self.lp.clickAddToCart()
        # self.lp.clickBuy()
        # time.sleep(2)
        # self.lp.clickProceedToBuy()
        # self.lp.clickBuy()
        # time.sleep(2)
        # self.lp.clickDelivery()
        # self.lp.clickContinuePayment()
        # time.sleep(2)
        # self.lp.clickRadioButton()
        # self.lp.enterCVV("230")
        # time.sleep(2)
        # self.lp.clickFinalContinue()
        # self.lp.clickPlaceOrder()
        self.driver.quit()




        #  pytest -v -s test/payment/purchase_tc.py
