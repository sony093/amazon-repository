import time
import logging
from lib2to3.pgen2 import driver
import self

import utilities.customlogger as cl
from base.seleniumdriver import SeleniumDriver


def def__init__():
    pass


class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def__init__()
    self.driver = driver

    def getTitle(self):
        return self.driver.title

    # Locators
    _amazon = 'a-section a-spacing-medium a-text-center'     #class  'a-icon a-icon-logo'
    _login_link = 'nav-link-accountList'  # id          #class  nav-line-1      nav-action-inner
    _mail_id = 'ap_email'
    _continue = 'continue'
    _password = 'ap_password'
    _submit = 'signInSubmit'
    _cart = 'nav-cart'
    _buy = 'sc-buy-box-ptc-button'  # name 'proceedToRetailCheckout'  #class 'a-button-input'  #id 'sc-buy-box-ptc-button'

    def clickAmazon(self):
        self.elementClick(locator=self._amazon)

    def clickLoginLink(self):
        self.elementClick(locator=self._login_link)

    def enterMailId(self, mail):
        self.sendKeys(mail, locator=self._mail_id)

    def clickContinue(self):
        self.elementClick(locator=self._continue)

    def enterPassword(self, password):
        self.sendKeys(password, locator=self._password)

    def clickSubmit(self):
        self.elementClick(locator=self._submit)

    def clickCart(self):
        self.elementClick(locator=self._cart)

    def clickBuy(self):
        self.elementClick(locator=self._buy)

    def login(self, mail="", password=""):
        self.elementClick()
        self.enterMailId(mail)
        self.clickContinue()
        self.enterPassword(password)
        self.clickSubmit()
        time.sleep(2)
        self.clickCart()
        self.clickBuy()

    def VerifyTitle(self):
        return self.VerifyPageTitle("Google")

    # auth-error-message-box
    def verifyLoginFailed(self):
        result = self.isElementPresent("auth-error-message-box", locatorType="id")
        return result

    def VerifyPageTitle(self, param):
        pass

