#запуск в консоле: pytest --language=es --browser_name=chrome/firefox test_items.py
import unittest
import pytest
import time
	
def test_items(browser):
	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
	browser.get(link)
	time.sleep(30)
	button = browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button")
	assert button is not None