from selenium import webdriver
import unittest
import time
import HtmlTestRunner
/*nhbhj*/

class GoogleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
        cls.driver.implicitly_wait(1)
        cls.driver.maximize_window()

    def test_CaseGoogle(self):
        self.driver.get("https://google.com")
        # self.print(driver.title)
        self.driver.find_element_by_name("q").send_keys("Selenium WebDriver Interview questions")
        self.driver.find_element_by_name("q").submit()

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()
        print("Test is completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/chandrashekarbasavaraj/Pom2/Reports"))
