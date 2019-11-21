from bs4 import BeautifulSoup     
from selenium import webdriver
import time ##페이지가 열릴 때까지 기다려 주는 명령을 위해
import sys
#C:\PythonSkill_Training\PythonSkill_Training\crtesttxtall\naverblogsection.txt
query_txt = input('네이버에 검색할 키워드는 무엇입니까?: ')
f_name = input('검색 결과를 저장할 파일경로와 이름을 지정하세요(예:c:\\data\\test.txt): ')

path = "C:\PythonSkill_Training\PythonSkill_Training\Crawling\chromedriver_win32\chromedriver.exe" # 셀레늄path
driver = webdriver.Chrome(path)
driver.get("https://www.naver.com/")
time.sleep(2)
element = driver.find_element_by_id("query")
element.send_keys(query_txt)
driver.find_element_by_id("search_btn").click()
#######분석
time.sleep(1)
full_html = driver.page_source 
soup = BeautifulSoup(full_html, 'html.parser') 
content_list = soup.find('ul', class_='type01') 
#######
for i in content_list:
    print(i.text.strip())
    print("\n")
  
orig_stdout = sys.stdout
f = open(f_name , 'a' , encoding='UTF-8')
sys.stdout = f ##출력 방향을 윗줄로 바꿈
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
content_list = soup.find('ul',class_='type01')

for i in content_list:
    print(i.text.strip())
    print("\n")

sys.stdout = orig_stdout
f.close()

print(" 요청하신 데이터 수집 작업이 정상적으로 완료되었습니다")
