from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим все обязательные поля
    name_input = browser.find_element_by_class_name("first_block .first_class input")
    surname_input = browser.find_element_by_class_name("first_block .second_class input")
    email_input = browser.find_element_by_class_name("first_block .third_class input")

    # Отправляем данные в обязательные поля
    name_input.send_keys("my name")
    surname_input.send_keys("my surname")
    email_input.send_keys("my mail")

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

    .first_block .form-group.first_class input.form-control.first 

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()