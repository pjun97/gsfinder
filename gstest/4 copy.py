from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys,time
import csv


print("몇 페이지까지 돌지 입력: ")
cnt=int(input())
print("저장할 파일명: ")
filename=input()
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
#3. 인증서 유무 확인
num1=1
num2=2
num3=11
cnt2=1
pgnum = 0


wait = WebDriverWait(driver, 2)

while num1<=11:
  
  num2=2
  if num1<11:
    pgnum += 1
    while num2<6:
      driver.find_element(By.XPATH,f'//*[@id="area-main"]/table/tbody/tr[{num2}]/td[2]/a').click()
      time.sleep(0.1)
      #3-1. 인증서가 없는 업체 뽑아내기
      try:
          driver.find_element(By.XPATH,f'//*[@id="frm1"]/table[1]/tbody/tr[5]/td/input')
          print({num2})
          print({pgnum})
          print({num1})
          driver.get(f"http://sw.tta.or.kr/@controlby/prdC06.jsp?pg={pgnum}")
          while driver.current_url!=f"http://sw.tta.or.kr/@controlby/prdC06.jsp?pg={pgnum}":
            time.sleep(2)
            driver.refresh()
            print("새로고침함")

    

          gsname=driver.find_element(By.CSS_SELECTOR,f'#area-main > table > tbody > tr:nth-child({num2}) > td.aL > a').text
          gsnum=driver.find_element(By.CSS_SELECTOR,f'#area-main > table > tbody > tr:nth-child({num2}) > td:nth-child(3)').text
          #3-2. 인증서가 미업로드된 업체의 GS번호,제품명 엑셀파일 생성
          with open(r'C:/gsgs/' + filename +'.csv', 'a', newline='') as f:
            writer=csv.writer(f)
            writer.writerow(([gsnum, gsname]))
          f.close()
          


          # f(asjhcgasghcsa)
          # (asdasdas + name1 + asdasdasd)
          # (akhdkjashdjksa, format(name1, nam2e))
      except:
          driver.get(f"http://sw.tta.or.kr/@controlby/prdC06.jsp?pg={pgnum}")
          time.sleep(0.1)
          driver.refresh()
          print({num2})
          print({pgnum})
          print({num1})
          while driver.current_url!=f"http://sw.tta.or.kr/@controlby/prdC06.jsp?pg={pgnum}":
            time.sleep(2)
            driver.refresh()
            print("새로고침함")

  
            
              
      num2=num2+1

# 4-1. 첫 페이지 넘어가기
  if num1==11:
   
   if num3==12:
    driver.find_element(By.CSS_SELECTOR,f'#area-main > div.box-page > a:nth-child({num3})').click()
   num1=2
  # 4-2. 두번째 페이지 값이 12로 고정이므로 num3 는 12로 고정 
   num3=12
   
   
  else:
     driver.find_element(By.XPATH,f'//*[@id="area-main"]/div[4]/a[{num1}]').click()
     num1=num1+1
     
# 5. 확인할 페이지 카운트
  if  cnt==cnt2:
    print(cnt2)
    break
 
  cnt2=cnt2+1

  


input()

