from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x,y): 
	return str(int(x)+int(y))
try: 
	link = "http://suninjuly.github.io/selects2.html"
	browser = webdriver.Chrome()
	browser.get(link)
	number1 = browser.find_element_by_css_selector("span#num1")
	number2 = browser.find_element_by_css_selector("span#num2")
	x = number1.text
	y = number2.text
	c = calc(x,y)
	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(c)
	button = browser.find_element_by_css_selector("button.btn.btn-default")
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
	