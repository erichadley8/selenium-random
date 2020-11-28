from selenium import webdriver
import random

while True:

	driver = webdriver.Firefox()
	driver.get('http://www.porngifs.xyz/')

	elements = driver.find_elements_by_tag_name('iframe')

	for element in elements:
		if "jads" in element.get_attribute("src"):
			element.click()

	handle=driver.window_handles
	
	for tab in driver.window_handles:
		driver.switch_to.window(tab)
		driver.close()
	
	