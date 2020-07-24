from selenium import webdriver


class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):

        baseURL = "https://www.amazon.in/"
        if self.browser == "iexplore":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome(executable_path="C:\\Users\\Abinash\\Desktop\\DRIVER\\chrome"
                                                      "\\chromedriver.exe")
        else:
            driver = webdriver.Chrome(executable_path="C:\\Users\\Abinash\\Desktop\\DRIVER\\chrome"
                                                      "\\chromedriver.exe")
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)
        return driver
