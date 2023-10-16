import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

# 1. 웹 브라우저 주소창을 컨트롤하기 드라이버 get
driver.get("https://www.naver.com")
time.sleep(3)

# 2-1. 요소를 찾아서 copy 해옴 
css_selector = "#account > div > a"

# 2-2, 찾아온 요소를 find_element로 가져오기 - > 상자에 담기
group_navigation = driver.find_element(By.CSS_SELECTOR,css_selector)

# 3-1. 데이터 가져오기
print(group_navigation.text)

# 3-2. 요소를 클릭하기 (액션)

group_navigation.click()

input()
