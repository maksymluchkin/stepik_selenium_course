from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

link = "http://suninjuly.github.io/selects1.html"
# link = "http://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("num1")
x = x_element.text
y_element = browser.find_element_by_id("num2")
y = y_element.text
x = int(x)
y = int(y)

result = x + y
result = str(result)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(result)


submit_button = browser.find_element_by_class_name("btn-default")
submit_button.click()

time.sleep(30)
browser.quit()