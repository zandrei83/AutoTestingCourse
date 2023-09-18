import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    res = int(browser.find_element(By.ID, 'num1').text) + int(browser.find_element(By.ID, 'num2').text)

    print(res)

    #res = str(res)

    #first
    browser.find_element(By.ID, "dropdown").click()
    browser.find_element(By.CSS_SELECTOR, f"[value='{res}']").click()


    #second
    #select = Select(browser.find_element(By.ID, "dropdown"))
    #select.select_by_value(str(res))


    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
