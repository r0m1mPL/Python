# -*- coding: cp1251 -*-
from selenium import webdriver
from random import randrange
from selenium.webdriver.common.keys import Keys
import time

user_agents = [
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "user-agent=Mozilla/4.0 (Windows NT 8.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "user-agent=Mozilla/4.0 (Windows NT 7.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.43 Safari/537.36",
]

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\ADMIN\AppData\Local\Google\Chrome\User Data\Default")
options.add_argument("profile-directory=Profile 1")
options.add_argument(f"user-agent={user_agents[randrange(0, 3)]}")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(executable_path=r"D:\Програмування\Python\Парсинг\Selenium\Загрузка видео\chromedriver\chromedriver.exe",
                          options=options,)

url = "https://accounts.google.com/signin/oauth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3ABBC%2C16%3A9b15b0994c6df9fc%2C10%3A1591711286%2C16%3A66b338ce162d6599%2Ca78a0c663f0beb12c0559379b61a9f5d62868c4fbd2f00e46a86ac26796507a1%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22921f8f04441041069683cc2377152422%22%7D&response_type=code&o2v=1&as=NCQvtBXI4prkLLDbn4Re0w&flowName=GeneralOAuthFlow"
# url = "https://youtube.com/"

try:
    driver.get(url)
    time.sleep(3)
    email = driver.find_element_by_id('identifierId')
    email.send_keys('simachenko.roma@gmail.com')
    nextBtn = driver.find_element_by_id('identifierNext')
    nextBtn.click()
    time.sleep(2)
    nextBtn = driver.find_element_by_css_selector("button")
    nextBtn.click()
    time.sleep(5)
    email = driver.find_element_by_id('identifierId')
    email.send_keys('simachenko.roma@gmail.com')
    nextBtn = driver.find_element_by_id('identifierNext')
    nextBtn.click()
    time.sleep(1000)
    passwd = driver.find_element_by_name('password')
    passwd.send_keys('PASSWORD')
    nextBtn = driver.find_element_by_id('passwordNext')
    nextBtn.click()
    time.sleep(1000)
except Exception as error:
    print(f"[-] {error}")
finally:
    driver.close()
    driver.quit()