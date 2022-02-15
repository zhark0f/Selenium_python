import math
from selenium import webdriver
import time 

link = "http://suninjuly.github.io/find_link_text"
formula = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    new_link = browser.find_element_by_link_text(formula)
    new_link.click()
    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Yauheni")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Zharkou")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Gomel")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Belarus")
    button = browser.find_element_by_class_name("btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла