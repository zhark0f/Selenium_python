from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class Test_2test(unittest.TestCase):

    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(3)
        browser.get(link)
        browser.find_element(By.XPATH,
                             "//label[text()='First name*']/following::input[1]").send_keys("Test")
        browser.find_element(By.XPATH,
                             "//label[text()='Last name*']/following::input[1]").send_keys("Test")
        browser.find_element(By.XPATH,
                             "//label[text()='Email*']/following::input[1]").send_keys("Test@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "welcome_text != Congratulations! You have successfully registered!")

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(3)
        browser.get(link)
        browser.find_element(By.XPATH,
                             "//label[text()='First name*']/following::input[1]").send_keys("Test")
        browser.find_element(By.XPATH,
                             "//label[text()='Last name*']/following::input[1]").send_keys("Test")
        browser.find_element(By.XPATH,
                             "//label[text()='Email*']/following::input[1]").send_keys("Test@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "welcome_text != Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()
