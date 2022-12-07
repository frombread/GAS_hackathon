from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
#from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException

df = pd.read_csv(r'C:\Users\user\Desktop\관광지.csv',encoding='cp949')


options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True) # 브라우저 종료 되고 싶지 않을때
options.add_experimental_option("excludeSwitches", ['enable-logging']) # 불필요한 에러메세지 없애기
url = "https://www.visitjeju.net/u/94i"

browser = webdriver.Chrome(chrome_options=options, executable_path=r"C:\Users\user\Desktop\chromedriver_win32\chromedriver.exe")
browser.get(url)
browser.set_window_size(1024, 600)

WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div[2]/div[4]/div[1]/button"))).click()
#WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div[2]/div[4]/div[2]/div[1]/label[3]"))).click()

first_index = 1
for i in range(1,93):
    url="https://www.visitjeju.net/kr/detail/list?menuId=DOM_000001718000000000&cate1cd=cate0000000002#p{}&pageSize=12&sortListType=reviewcnt&viewType=list&isShowBtag&tag".format(str(i))
    browser.implicitly_wait(30)
    browser.get(url)
    for j in range(1,13):
        title = browser.find_element(By.XPATH,".//*[@id='content']/div/div[2]/div[5]/ul/li[{}]/dl/dt/a/p[1]".format(str(j))).get_attribute("textContent").replace('\t','').replace('\n','')
        department = browser.find_element(By.XPATH,".//*[@id='content']/div/div[2]/div[5]/ul/li[{}]/dl/dt/a/p[2]".format(str(j))).get_attribute("textContent").replace('\t','').replace('\n','')
        df.loc[first_index,'이름'] = title
        df.loc[first_index,'주소'] = department 
        first_index +=1
            
    browser.back()

