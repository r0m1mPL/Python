# -*- coding: cp1251 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random, pickle
from auth_data import login, password

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                     f"Chrome/91.0.4472.124 Safari/537.36")
driver = webdriver.Chrome(executable_path=r"D:\Програмування\Python\Парсинг\chromedriver\chromedriver.exe",
                          options=options,)

url = 'https://nz.ua/'

try:
    # driver.get(url=url)
    # time.sleep(3)
    #
    # login_input = driver.find_element_by_id("loginform-login")
    # login_input.clear()
    # login_input.send_keys(login)
    # time.sleep(2)
    #
    # remember = driver.find_element_by_id("loginform-rememberme")
    # if not remember.is_selected():
    #     remember.click()
    # time.sleep(2)
    #
    # password_input = driver.find_element_by_id("loginform-password")
    # password_input.clear()
    # password_input.send_keys(password)
    # time.sleep(2)
    # password_input.send_keys(Keys.ENTER)
    # time.sleep(5)
    #
    # driver.get(url=url+'menu/')
    # time.sleep(3)
    #
    # pickle.dump(driver.get_cookies(), open(f"{login}_cookies", 'wb'))

    driver.get(url=url)
    time.sleep(3)
    for cookie in pickle.load(open(f"{login}_cookies", 'rb')):
        driver.add_cookie(cookie)
    time.sleep(3)
    driver.refresh()
    time.sleep(10)

except Exception as error:
    print(error)
finally:
    driver.close()
    driver.quit()