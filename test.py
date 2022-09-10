from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest

driver = webdriver.Chrome()

class TestMain(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://google.com/ncr")

    def test_page(self):
        elm = self.browser.find_element(By.NAME, "q")
        elm.send_keys("selenide")
        elm.send_keys(Keys.RETURN)
        site = self.browser.find_elements(By.XPATH, "//cite[@class='iUh30 tjvcx']")
        assert site[0].text == "https://selenide.org", "Wrong site"

        imgs = self.browser.find_elements(By.XPATH, "//div[@class='hdtb-mitem']/a")
        imgs[0].click()

        img_name = self.browser.find_element(By.XPATH, "//div[@jsname='DeysSe']/img")
        img_name.get_attribute("alt")
        assert img_name.get_attribute("alt")[:8] == "Selenide", "This picture doesn`t like selenid"

        return_back = self.browser.find_elements(By.XPATH, "//div[@class='T47uwc']/a")
        return_back[0].click()

        site = self.browser.find_elements(By.XPATH, "//cite[@class='iUh30 tjvcx']")
        assert site[0].text != "https://selenide.org", "Wrong site"



    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()