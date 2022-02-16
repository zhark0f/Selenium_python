from selenium import webdriver
import time
import math


def my_func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element_by_tag_name("button").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element_by_id("input_value").text
    browser.find_element_by_id("answer").send_keys(my_func(x))
    browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(5)
    browser.quit()
