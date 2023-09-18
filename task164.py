from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.XPATH, "//form/div[@class='first_block']/div[1]/input[1]").send_keys("Ivan")
    browser.find_element(By.XPATH, "//form/div[@class='first_block']/div[2]/input[1]").send_keys("Petrov")
    browser.find_element(By.XPATH, "//form/div[@class='first_block']/div[3]/input[1]").send_keys("ivan@mail.ru")

    browser.find_element(By.XPATH, "//form/div[@class='second_block']/div[1]/input[1]").send_keys("+79005657898")
    browser.find_element(By.XPATH, "//form/div[@class='second_block']/div[2]/input[1]").send_keys("Russia, Moscow, The Kremlin")

    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы

    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()