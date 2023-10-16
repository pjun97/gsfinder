from selenium import webdriver
from selenium.webdriver.common.by import By
import sys,os,time



driver = webdriver.Chrome()

#1 . GS인증 페이지 접근
driver.get("http://sw.tta.or.kr/@controlby/login.jsp")



#2. 로그인
driver.find_element(By.NAME, 'id').send_keys('gs_admin')
driver.find_element(By.NAME, 'pw').send_keys('12sqec34%')
driver.find_element(By.XPATH, '//*[@id="boxLogin"]/input').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="box-menu"]/ul/li[2]/dl/dd[1]/a').click()
time.sleep(1)
num1=1
num2=2



while num1<10:    
  driver.find_element(By.XPATH,f'//*[@id="area-main"]/div[4]/a[{num1}]').click()
  while num2<22:
    driver.find_element(By.XPATH,f'//*[@id="area-main"]/table/tbody/tr[{num2}]/td[2]/a').click()
    try:
        driver.find_element(By.XPATH,f'//*[@id="frm1"]/table[1]/tbody/tr[5]/td/input')
        driver.back()
        gsname=driver.find_element(By.CSS_SELECTOR,f'#area-main > table > tbody > tr:nth-child({num2}) > td.aL > a').text
        print('인증서 누락 업체:',gsname)
 
    except:
            driver.back()
    num2=num2+1
  
  num1=num1+1
  
  

# for 1~10


input()


