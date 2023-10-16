from selenium import webdriver
import time

driver = webdriver.Chrome()

#1-1 페이지 이동
driver.get("https://www.naver.com/")
time.sleep(1)
driver.get("https://www.google.com/?&bih=963&biw=1920&hl=ko")
time.sleep(1)
#1-2 뒤로가기
driver.back()
time.sleep(1)
#1-3 forward 앞으로 가기
driver.forward()
time.sleep(1)
#1-4 새로고침
driver.refresh()
time.sleep(1)
print("동작 끝")
input()