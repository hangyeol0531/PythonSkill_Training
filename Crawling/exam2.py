#Step 1. 필요한 모듈과 라이브러리를 로딩하고 검색어를 입력 받습니다
from bs4 import BeautifulSoup     
from selenium import webdriver
import time
import sys
##C:\PythonSkill_Training\PythonSkill_Training\crtesttxtall\test1_1.txt
query_txt = input('크롤링할 키워드는 무엇입니까?: ')
f_name = input('검색 결과를 저장할 파일경로와 이름을 지정하세요(예:c:\\data\\test.txt): ')

#Step 2. 크롬 드라이버를 사용해서 웹 브라우저를 실행합니다.
path = "C:\PythonSkill_Training\PythonSkill_Training\Crawling\chromedriver_win32\chromedriver.exe" # 셀레늄path
driver = webdriver.Chrome(path)
driver.get("https://korean.visitkorea.or.kr/main/main.html")
time.sleep(2)  #  창이 모두 열릴 때 까지 2초 기다립니다.

#Step 3. 검색창의 이름을 찾아서 검색어를 입력하고 검색을 실행합니다
driver.find_element_by_id("btnSearch").click()
element = driver.find_element_by_id("inp_search")
element.send_keys(query_txt)

driver.find_element_by_link_text("검색").click()
# 학습목표 1: 텍스트를 추출하여 화면에 출력하기
# Step 4. 현재 페이지에 있는 내용을 화면에 출력하기

time.sleep(1)

full_html = driver.page_source ## 전체 소스를 가져옴

soup = BeautifulSoup(full_html, 'html.parser') ## bs가 분석을 하게함

content_list = soup.find('ul','list_thumType flnon') ## class list_thumType flnon 인 부분에서 ul 

for i in content_list:
    print(i.text.strip()) ## 양쪽 끝 공백제거 출력 
    print("\n")
  
# 학습목표 2: 텍스트를 추출하여 txt 형식으로 저장하기
# Step 5. 현재 페이지에 있는 내용을 txt 형식으로 파일에 저장하기
orig_stdout = sys.stdout
f = open(f_name , 'a' , encoding='UTF-8')
sys.stdout = f ##출력 방향을 윗줄로 바꿈
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
content_list = soup.find('ul',class_='list_thumType flnon')

for i in content_list:
    print(i.text.strip())
    print("\n")

sys.stdout = orig_stdout
f.close()

print(" 요청하신 데이터 수집 작업이 정상적으로 완료되었습니다")