from selenium import webdriver
import time
import math


def calc(x1):
    return str(math.log(abs(12*math.sin(int(x1)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    input_value = browser.find_element_by_id("input_value")
    x = input_value.text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
