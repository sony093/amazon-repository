from lib2to3.pgen2 import driver
import self
from base.seleniumdriver import SeleniumDriver
import utilities.customlogger as cl
import logging
import time


def def__init__():
    pass


class PaymentPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def__init__()
    self.driver = driver

    def getTitle(self):
        return self.driver.title

    # LOCATORS
    _login_link = 'nav-link-accountList'  # id          #class  nav-line-1      nav-action-inner
    _mail_id = 'ap_email'
    _continue = 'continue'
    _password = 'ap_password'
    _submit = 'signInSubmit'
    _search = 'twotabsearchtextbox'   #"//input[@id='twotabsearchtextbox']"         #'twotabsearchtextbox'   id
    _search_icon = 'nav-search-submit-text'              #id   #'nav-input'  # class
    _atta = 's-image'  # class
    _add_to_cart = 'add-to-cart-button'  # id
    _proceed_to_buy = 'hlb-ptc-btn-native'  # id
    _buy = 'sc-buy-box-ptc-button'  # class
    _delivery = 'a-declarative a-button-text'  # class
    _continue_payment = 'a-button-text'  # class
    _radio_check = 'pp-HiR0bm-91'  # id
    _cvv = 'pp-HiR0bm-98'  # id
    _final_continue = 'pp-HiR0bm-172-announce'  # id
    _place_order = 'placeYourOrder'  # id

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

    def enterKeyword(self, grocery):
        self.sendKeys(grocery, locatorType=self._search)
        self.elementClick(locatorType=self._search_icon)

    def clickItem(self):
        self.elementClick(locatorType=self._atta)             #.format("")

    def clickAddToCart(self):
        self.elementClick(locator=self._add_to_cart)

    def clickProceedToBuy(self):
        self.elementClick(locator=self._proceed_to_buy)

    def clickBuy(self):
        self.elementClick(locator=self._buy)

    def clickDelivery(self):
        self.elementClick(locator=self._delivery)

    def clickContinuePayment(self):
        self.elementClick(locator=self._continue_payment)

    def clickRadioButton(self):
        self.elementClick(locator=self._radio_check)

    def enterCVV(self, cvv):
        self.sendKeys(cvv, locator=self._cvv)

    def clickFinalContinue(self):
        self.elementClick(locator=self._final_continue)

    def clickPlaceOrder(self):
        self.elementClick(locator=self._place_order)

    def login(self, mail="", password="", grocery="", cvv=""):
        self.elementClick()
        self.enterMailId(mail)
        self.clickContinue()
        self.enterPassword(password)
        self.clickSubmit()
        time.sleep(2)
        self.enterKeyword(grocery)
        self.enterCVV(cvv)
