from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://www.naver.com/")

# 3. Driver.wait
try:
 셀렉터="#account > div > a"
 WebDriverWait(driver,10).until(EC.presence_of_all_elements_located(
     By.CSS_SELECTOR, 셀렉터
))
except:
    print("예외발생")
print("다음코드 실행")

# time.sleep(1)
# # 2-1 title 웹 사이트의 타이틀 가지고옴
# title = driver.title
# print(title,"이 타이틀")
# time.sleep(1)
# # 2-1 current_url 주소창을 그대로 가지고 옴
# 현재주소=driver.current_url
# print(현재주소,"가 현재 주소이다")


input()
