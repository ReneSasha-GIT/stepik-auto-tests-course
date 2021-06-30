from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num1_text = num1.text
    num2 = browser.find_element_by_id("num2")
    num2_text = num2.text
    sum1 = str(int(num1_text) + int(num2_text))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum1)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
