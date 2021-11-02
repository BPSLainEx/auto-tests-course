from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
url = 'http://suninjuly.github.io/get_attribute.html'
try:
    browser = webdriver.Chrome(executable_path='C:\\Users\\Zero\\PycharmProjects\\selenium\\chromedriver\\chromedriver.exe')
    browser.get(url=url)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input2 = browser.find_element_by_id('answer')
    input2.send_keys(y)
    input3 = browser.find_element_by_css_selector("[type='checkbox']")
    input3.click()
    input4 = browser.find_element_by_css_selector("[value='robots']")
    input4.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

