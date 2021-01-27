from selenium import webdriver
import time
import math
  
def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
	
try: 
	link = "http://suninjuly.github.io/get_attribute.html"
	browser = webdriver.Chrome()
	browser.get(link)
	image = browser.find_element_by_id("treasure")
	x = image.get_attribute('valuex')
	y = calc(x)
	option0 = browser.find_element_by_css_selector("input#answer")
	option0.send_keys(y)
	option1 = browser.find_element_by_id("robotCheckbox")
	option1.click()
	option2 = browser.find_element_by_id("robotsRule")
	option2.click()
	button = browser.find_element_by_css_selector("button.btn.btn-default")
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
	