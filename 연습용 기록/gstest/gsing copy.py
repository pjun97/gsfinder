from selenium import webdriver
from selenium.webdriver.common.by import By
import sys,os,time
import csv



driver = webdriver.Chrome()

#1 . GS인증 페이지 접근
driver.get("http://sw.tta.or.kr/@controlby/login.jsp")




#2. 로그인
driver.find_element(By.NAME, 'id').send_keys('')
driver.find_element(By.NAME, 'pw').send_keys('')
driver.find_element(By.XPATH, '//*[@id="boxLogin"]/input').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="box-menu"]/ul/li[2]/dl/dd[1]/a').click()
time.sleep(1)
#3. 인증서 유무 확인
num1=1
num2=2
while num1<11:
  num2=2
  while num2<22:
    driver.find_element(By.XPATH,f'//*[@id="area-main"]/table/tbody/tr[{num2}]/td[2]/a').click()
    #3-1. 인증서가 없는 업체 뽑아내기
    try:
        driver.find_element(By.XPATH,f'//*[@id="frm1"]/table[1]/tbody/tr[5]/td/input')
        driver.back()
        gsname=driver.find_element(By.CSS_SELECTOR,f'#area-main > table > tbody > tr:nth-child({num2}) > td.aL > a').text
        gsnum=driver.find_element(By.CSS_SELECTOR,f'#area-main > table > tbody > tr:nth-child({num2}) > td:nth-child(3)').text
        #3-2. 인증서가 미업로드된 업체의 GS번호,제품명 엑셀파일 생성
        with open(r'C:/gsgs/gs3.csv', 'a', newline='') as f:
          writer=csv.writer(f)
          writer.writerow(([gsnum, gsname]))
        f.close()
        
    except:
            driver.back()
    num2=num2+1

  driver.find_element(By.XPATH,f'//*[@id="area-main"]/div[4]/a[{num1}]').click()
  num1=num1+1



input()


