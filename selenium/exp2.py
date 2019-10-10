from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome("../chromedriver.exe")
driver.implicitly_wait(3)

driver.get("https://nid.naver.com/nidlogin.login")

id=""
pw=""

driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'")
# driver.find_element_by_name(id).send_keys(id)
# driver.find_element_by_name(pw).send_keys(pw)
time.sleep(0.5)
#element창 로그인버튼 소스 선택된 상태에서 마우스 오른쪽 버튼 클릭 copy
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/span[1]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="login_maintain"]/span[1]').click()
time.sleep(1)


# # Naver 페이 들어가기
# driver.get('https://order.pay.naver.com/home')
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# notices = soup.select('div.p_inr > div.p_info > a > span')
# point = soup.select_one('.my_npoint strong')
# print(point.string)

# time.sleep(15)
# driver.close()
