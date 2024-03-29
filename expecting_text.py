from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = browser.find_element_by_id("book")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID,"price"), "$100")
    )
button.click()

#скролим страницу и определяем кнопку submit
submit_button = browser.find_element_by_id("solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

result = browser.find_element_by_id("answer")
result.send_keys(y)

submit_button.click()
