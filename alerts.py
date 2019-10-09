from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

journey_button = browser.find_element_by_class_name("btn-primary")
journey_button.click()

alert = browser.switch_to.alert
alert.accept()

x_element = browser.find_element_by_id("input_value")
x = x_element.text

result = calc(x)

answer = browser.find_element_by_id("answer")
answer.send_keys(result)

submit_button = browser.find_element_by_class_name("btn-primary")
submit_button.click()