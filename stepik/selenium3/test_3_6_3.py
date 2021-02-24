from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    time.sleep (5)
    browser.quit()

@pytest.mark.parametrize('url', ['236895', '236896', '236897', '236898' ,'236899' ,'236903' ,'236904' ,'236905'])
class TestMainPage1():
	
	def test_parametrize(self, browser, url):
		get_text = ''
		link = f'https://stepik.org/lesson/{url}/step/1'
		browser.get(link)
		option0 = browser.implicitly_wait(10)
		option0 = browser.find_element_by_css_selector("textarea")
		option0.send_keys(str(math.log(int(time.time()))))
		button = browser.find_element_by_css_selector("button.submit-submission")
		button.click()
		x_element = browser.find_element_by_css_selector("pre.smart-hints__hint")
		x = x_element.text
		if x != "Correct!":
			x += get_text
		print(get_text)
		assert x == False

if __name__ == "__main__":

    unittest.main()
