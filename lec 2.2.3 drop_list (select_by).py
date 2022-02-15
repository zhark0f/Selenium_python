from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    number_1 = browser.find_element_by_id("num1").text
    number_2 = browser.find_element_by_id("num2").text
    summa = str(int(number_1) + int(number_2))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(summa)
    browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(10)
    browser.quit()