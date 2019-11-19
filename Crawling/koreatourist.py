from bs4 import BeautifulSoup     
from selenium import webdriver
import time ##페이지가 열릴 때까지 기다려 주는 명령을 위해

query_txt = input('크롤링할 키워드는 무엇입니까?: ')

#Step 1. 크롬 드라이버를 사용해서 웹 브라우저를 실행합니다.
path = "C:\PythonSkill_Training\PythonSkill_Training\Crawling\chromedriver_win32\chromedriver.exe" # 셀레늄path
driver = webdriver.Chrome(path)

driver.get("https://korean.visitkorea.or.kr")
time.sleep(2)  # 위 페이지가 모두 열릴 때 까지 2초 기다립니다.

#Step 2. 검색창의 이름을 찾아서 검색어를 입력합니다
driver.find_element_by_id("btnSearch").click()  #버튼 클릭

element = driver.find_element_by_id("inp_search")

element.send_keys(query_txt)

#Step 3. 검색 버튼을 눌러 실행합니다

driver.find_element_by_link_text("검색").click()
#driver.find_element_by_class_name("btn_search2").click()  # class name 으로도 가능합니다.
#driver.find_element_by_xpath('//*[@id="gnbMain"]/div/div/div[1]/div[1]/a').click()   # xpath 로도 가능합니다.