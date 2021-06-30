from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/wait1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    message = browser.find_element_by_id("verify_message")

    assert "Verification was successful!" == message.text, "Wrong message"

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
