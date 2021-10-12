from selenium import webdriver
from fake_useragent import UserAgent
import time

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("start-maximized")
driver = webdriver.Chrome(
    executable_path=r"D:\Програмування\Python\Парсинг\Selenium\Загрузка видео\chromedriver\chromedriver.exe",
        options=options
)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {
    "userAgent": UserAgent().random}
)
driver.get('https://accounts.google.com')
email = driver.find_element_by_id('identifierId')
email.send_keys('hahaha')
next = driver.find_element_by_id('identifierNext')
next.click()
time.sleep(5)
passwd = driver.find_element_by_name('password')
passwd.send_keys('*bzZ%tEDsFF6PKBP')