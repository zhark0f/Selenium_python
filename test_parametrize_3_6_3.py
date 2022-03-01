import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


list_of_links = ["236895", "236896", "236897",
                 "236898", "236899", "236903", "236904", "236905"]


class TestStepik():

    @pytest.mark.parametrize('number', list_of_links)
    def test_stepik_feedback_should_be_correct(self, browser, number):
        browser.implicitly_wait(10)
        link = f"https://stepik.org/lesson/{number}/step/1"
        browser.get(link)
        answer = math.log(int(time.time()))
        browser.find_element(By.TAG_NAME, "textarea").send_keys(str(answer))
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        )
        button.click()
        result = browser.find_element(
            By.CSS_SELECTOR, ".smart-hints__hint").text
        assert result == "Correct!", "Message is not correct!"
