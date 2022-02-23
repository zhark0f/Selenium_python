from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def my_func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = browser.find_element(By.ID, "book")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    my_text_find_100 = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()
    button_2 = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_2)
    x = browser.find_element(By.ID, "input_value").text
    browser.find_element_by_id("answer").send_keys(my_func(x))
    button_2.click()
    browser.switch_to.alert
finally:
    time.sleep(10)
    browser.quit()
