from bs4 import BeautifulSoup     
from selenium import webdriver
import time ##페이지가 열릴 때까지 기다려 주는 명령을 위해

query_txt = input('구글에 검색할 키워드는 무엇입니까?: ')
print(type(query_txt))
path = "C:\PythonSkill_Training\PythonSkill_Training\Crawling\chromedriver_win32\chromedriver.exe" # 셀레늄path
driver = webdriver.Chrome(path)
driver.get("https://www.google.co.kr")
time.sleep(2)
element = driver.find_elements_by_name("q")
element.send_keys(query_txt)
driver.find_elements_by_link_text("Google 검색").click()