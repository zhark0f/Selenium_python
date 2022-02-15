from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x_element = browser.find_element_by_id("treasure")
    x_value = int(x_element.get_attribute("valuex"))
    browser.find_element_by_id("answer").send_keys(calc(x_value))
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector("button").click()
finally:
    time.sleep(10)
    browser.quit()