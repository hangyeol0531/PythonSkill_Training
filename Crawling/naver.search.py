from bs4 import BeautifulSoup     
from selenium import webdriver
import time ##페이지가 열릴 때까지 기다려 주는 명령을 위해

query_txt = input('네이버에 검색할 키워드는 무엇입니까?: ')
path = "C:\PythonSkill_Training\PythonSkill_Training\Crawling\chromedriver_win32\chromedriver.exe" # 셀레늄path
driver = webdriver.Chrome(path)
driver.get("https://www.naver.com/")
time.sleep(2)
element = driver.find_element_by_id("query")
element.send_keys(query_txt)
driver.find_element_by_id("search_btn").click()