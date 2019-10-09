from selenium import webdriver
import math


def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

treasure = browser.find_element_by_id("treasure")
x = treasure.get_attribute("valuex")
y = calc(x)

result = browser.find_element_by_id("answer")
result.send_keys(y)

robot_checkbox = browser.find_element_by_id("robotCheckbox")
robot_checkbox.click()

robot_radiobutton =	browser.find_element_by_id("robotsRule")
robot_radiobutton.click()

submit_button = browser.find_element_by_class_name("btn-default")
submit_button.click()

time.sleep(30)
browser.quit()