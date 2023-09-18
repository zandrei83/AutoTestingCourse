import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID,'input_value').text

    y = calc(x)

    text_field = browser.find_element(By.ID, "answer")
    browser.execute_script(" return arguments[0].scrollIntoView(true);",text_field)

    text_field.send_keys(y)

    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
