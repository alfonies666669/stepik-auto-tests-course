from selenium import webdriver
import time
import os 

try: 
	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)
	elements = browser.find_elements_by_css_selector ("input.form-control")
	for element in elements:
		element.send_keys("My answer")
	current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
	file_name = "text.txt"
	file_path = os.path.join(current_dir, 'text.txt')           # добавляем к этому пути имя файла 
	element = browser.find_element_by_css_selector("input#file")
	element.send_keys(file_path)	
	button = browser.find_element_by_css_selector("button.btn")
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
	