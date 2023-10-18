from selenium import webdriver

import time
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()


driver.get("http://sw.tta.or.kr/@controlby/login.jsp")
time.sleep(1)


input()