from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_value = browser.find_element_by_id("input_value")
    x = input_value.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    check = browser.find_element_by_id("robotCheckbox")
    check.click()

    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
