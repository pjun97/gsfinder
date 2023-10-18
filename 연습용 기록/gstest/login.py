from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import chromedriver_autoinstaller


chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

#1 . GS인증 페이지 접근
driver.get("http://sw.tta.or.kr/@controlby/login.jsp")


#2. 로그인
driver.find_element(By.NAME, 'id').send_keys('')
driver.find_element(By.NAME, 'pw').send_keys('')
driver.find_element(By.XPATH, '//*[@id="boxLogin"]/input').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="box-menu"]/ul/li[2]/dl/dd[1]/a').click()

#3. 존재여부 확인

try:
    element=driver.find_element(By.TAG_NAME,'pdf')
tta = element.text
print("인증서 존재")
print(tta)

except NoSuchElementException:
print("인증서 누락")


input()