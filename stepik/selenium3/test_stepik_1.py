from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
	Prime = ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1', 
	'https://stepik.org/lesson/236897/step/1' 'https://stepik.org/lesson/236898/step/1', 
	'https://stepik.org/lesson/236899/step/1' 'https://stepik.org/lesson/236903/step/1', 
	'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1]']
	link = Prime
	browser = webdriver.Chrome()
	browser.get('https://stepik.org/lesson/236895/step/1')
	browser.implicitly_wait(10) # seconds
	option0 = browser.find_element_by_css_selector("textarea")
	option0.send_keys(str(math.log(int(time.time()))))
	button = browser.find_element_by_css_selector("button.submit-submission")
	button.click()
	x_element = browser.find_element_by_css_selector("pre.smart-hints__hint")
	x = x_element.text
	S = "Correcct"
	if x != S:
		print (x)
finally:
	time.sleep(15)
	browser.quit()
	#pre.smart-hints__hint