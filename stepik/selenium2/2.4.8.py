from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:

	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")
	button = WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "$100")
		)
	button = browser.find_element_by_id("book")
	button.click()
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()
	x_element = browser.find_element_by_css_selector("span#input_value")
	x = x_element.text
	y = calc(x)
	option0 = browser.find_element_by_css_selector("input#answer")
	option0.send_keys(y)
	button = browser.find_element_by_css_selector("button#solve.btn")
	button.click()
	
finally:
	time.sleep(10)
	browser.quit()
	