from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys,time
import csv


print("몇 페이지까지 돌지 입력: ")
cnt=int(input()) # 확인하고자하는 페이지 수를 입력받음
print("저장할 파일명: ")
filename=input() # 저장할 파일명을 입력받음
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
pg=1 # 페이지 번호 
content=2 #게시물 번호 
num=11 # 10페이지  selector 값 
cnt2=1 # 입력받은 페이지값과 비교될 cnt 값 




while pg<=11:
  content=2
  if pg<11:
    while content<22:
      driver.find_element(By.XPATH,f'//*[@id="area-main"]/table/tbody/tr[{content}]/td[2]/a').click()
      time.sleep(0.1)
      driver.refresh()
      #3-1. 인증서가 없는 업체 뽑아내기
      try:
          driver.find_element(By.XPATH,f'//*[@id="frm1"]/table[1]/tbody/tr[5]/td/input')
          driver.back()
          time.sleep(0.1)
          driver.refresh()
          
    

          gsname=driver.find_element(By.CSS_SELECTOR,f'#area-main > table > tbody > tr:nth-child({content}) > td.aL > a').text # 인증서의 이름 
          gsnum=driver.find_element(By.CSS_SELECTOR,f'#area-main > table > tbody > tr:nth-child({content}) > td:nth-child(3)').text # 인증서의 gs번호
          #3-2. 인증서가 미업로드된 업체의 GS번호,제품명 엑셀파일 생성
          with open(r'C:/gsgs/' + filename +'.csv', 'a', newline='') as f: 
            writer=csv.writer(f)
            writer.writerow(([gsnum, gsname]))
          f.close()
          


          
      except:
          driver.back()
          time.sleep(0.1)
          driver.refresh()
          

  
            
              
      content=content+1

# 4-1. 첫 페이지 넘어가기
  if pg==11:
   if num==12:
    driver.find_element(By.CSS_SELECTOR,f'#area-main > div.box-page > a:nth-child({num})').click()
   pg=2
  # 4-2. 두번째 페이지 값이 12로 고정이므로 num3 는 12로 고정 
   num=12
   
   
  else:
     
     driver.find_element(By.XPATH,f'//*[@id="area-main"]/div[4]/a[{pg}]').click()
     pg=pg+1
# 5. 확인할 페이지 카운트
  if  cnt==cnt2:
    break
 
  cnt2=cnt2+1

  


input()

