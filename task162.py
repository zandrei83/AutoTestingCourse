from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.XPATH, "//input")

    letters = string.ascii_lowercase
    word = ''
    for element in elements:
        word = ''.join(random.sample(letters, random.randrange(3, 15))).title()
        element.send_keys(word)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


