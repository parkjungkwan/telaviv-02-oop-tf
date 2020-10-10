from selenium import webdriver
from bs4 import BeautifulSoup
# https://chromedriver.storage.googleapis.com/index.html?path=2.43/

driver = webdriver.Chrome("C:/Users/csein/Desktop/chromedriver") # chromedriver 경로 설저
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login')
# 아이디/비밀번호를 입력해준다.
driver.find_element_by_name('id').send_keys('아이디 입력')
driver.find_element_by_name('pw').send_keys('비밀번호 입력')
driver.implicitly_wait(3)
 
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
driver.implicitly_wait(3)
 
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.p_inr > div.p_info > a > span')
 
for n in notices:
    print(n.text.strip())
