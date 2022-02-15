from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_xpath("//label[text()='First name*']/following::input[1]").send_keys("Test")
    browser.find_element_by_xpath("//label[text()='Last name*']/following::input[1]").send_keys("Test")
    browser.find_element_by_xpath("//label[text()='Email*']/following::input[1]").send_keys("Test@mail.ru")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()