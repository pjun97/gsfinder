from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()

url="https://www.naver.com/"

driver.get("url")
time.sleep(1)

driver.find_element(By.CLASS_NAME,"input_text").send_keys("블랙핑크")
time.sleep(1)

driver.find_element(By.ID,"query").send_keys("뉴진스")
time.sleep(1)

driver.find_element(By.NAME,"query").send_keys("뉴진스")
time.sleep(1)



input()