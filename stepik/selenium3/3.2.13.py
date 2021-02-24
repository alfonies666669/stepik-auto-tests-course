import unittest
from selenium import webdriver
import time

class TestAbs(unittest.TestCase):
	def test_abs1(self):
		link = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)
		input1 = browser.find_element_by_css_selector('div.first_block input.form-control.first')
		input1.send_keys("Ivan")
		input2 = browser.find_element_by_css_selector('div.first_block input.form-control.second')
		input2.send_keys("Petrov")
		input3 = browser.find_element_by_css_selector('div.first_block input.form-control.third')
		input3.send_keys("Smolensk")
		button = browser.find_element_by_css_selector("button.btn")
		button.click()

		# Отправляем заполненную форму

		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
		time.sleep(1)

		# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'OK')
	def test_abs2(self):
		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)
		input1 = browser.find_element_by_css_selector('div.first_block input.form-control.first')
		input1.send_keys("Ivan")
		input2 = browser.find_element_by_css_selector('div.first_block input.form-control.second')
		input2.send_keys("Petrov")
		input3 = browser.find_element_by_css_selector('div.first_block input.form-control.third')
		input3.send_keys("Smolensk")
		button = browser.find_element_by_css_selector("button.btn")
		button.click()

		# Отправляем заполненную форму
		button = browser.find_element_by_css_selector("button.btn")
		button.click()

		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
		time.sleep(1)

		# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'OK')
#assert expected_result == actual_result, \
        #f"expected {expected_result}, got {actual_result}"
if __name__ == "__main__": unittest.main()
