from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome("../chromedriver.exe")
driver.implicitly_wait(3)

driver.get("https://www.istarbucks.co.kr/store/store_map.do")

search = "동성로"
searchInput = driver.find_element_by_id("quickSearchText")
searchInput.send_keys(search)
time.sleep(1)
driver.find_element_by_xpath(
    """//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[1]/div[1]/div/a"""
    ).click()

source = driver.page_source

soup = BeautifulSoup(source, "html.parser")

data1 = soup.find("ul", {"class" : "quickSearchResultBox"})

data2 = data1.find_all("strong")

for d in data2:
    print(d.text)
    
# result:
# 대구중앙로
# 동성로광장
# 동성로중앙
# 동성로로데오