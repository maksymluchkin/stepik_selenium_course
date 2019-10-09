from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим все обязательные поля
    name_input = browser.find_element_by_css_selector("[name = 'firstname']")
    surname_input = browser.find_element_by_css_selector("[name = 'lastname']")
    email_input = browser.find_element_by_css_selector("[name = 'email']")

    # Отправляем данные в обязательные поля
    name_input.send_keys("my name")
    surname_input.send_keys("my surname")
    email_input.send_keys("my mail")

    # Отправляем файл
    my_file = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'yolo.txt')
    my_file.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()