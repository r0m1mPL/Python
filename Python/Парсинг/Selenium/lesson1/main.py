# -*- coding: cp1251 -*-
from seleniumwire import webdriver
from fake_useragent import UserAgent
from proxy_auth_data import login, password
import time, random

user_agent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agent.random}")
options.add_argument(f"--proxy-server=138.128.91.65:8000")
# proxy_options = {
#     "proxy": {
#         "https": f"http://{login}:{password}@138.128.91.65:8000"
#     }
# }
driver = webdriver.Chrome(executable_path=r"D:\Програмування\Python\Парсинг\Selenium\chromedriver\chromedriver.exe",
                          # seleniumwire_options=proxy_options,
                          options=options,
                          )

# url = 'https://nz.ua/'

try:
    driver.get(url='https://2ip.ru')
    time.sleep(20)
except Exception as error:
    print(error)
finally:
    driver.close()
    driver.quit()