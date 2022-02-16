from selenium import webdriver
import time
import os


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element_by_name("firstname").send_keys("Test_first_name")
    browser.find_element_by_name("lastname").send_keys("Test_last_name")
    browser.find_element_by_name("email").send_keys("Test_email_name")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file_for_2.2.8.txt')
    browser.find_element_by_id("file").send_keys(file_path)
    browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(5)
    browser.quit()
