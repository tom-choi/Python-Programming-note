from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
import xlwt
import pandas as pd
import openpyxl
from torch import prelu

PATH = "F:/爬蟲/chromedriver.exe"
option = webdriver.ChromeOptions()
#option.add_experimental_option("excludeSwitches",['enable-automation','enable'])
driver = webdriver.Chrome(PATH)

driver.get("https://www.ssm.gov.mo/pubssmweb/Utlap/frmUtlapLic.aspx?a_type=AL")
print(driver.title)

LicnoM = []
NameM = []
AddrM = []
TelM = []
Office_TimeM = []

#網站頁數
for i in range(1,5):
    try:
        # 定位到要懸停的元素
        for k in range(2,13):
            print(k+(i >= 2 if 1 else 0))
            above = driver.find_element_by_xpath(f'/html/body/form/div[3]/a[{k+(i >= 2 if 1 else 0)}]')
            ActionChains(driver).click(above).perform()
            #time.sleep(3)
            for j in range(2,60):
                try:
                    Licno = driver.find_element_by_xpath(f"//*[@id='MainGrid']/tbody/tr[{j}]/td[2]").text
                    Name = driver.find_element_by_xpath(f"//*[@id='MainGrid']/tbody/tr[{j}]/td[3]").text
                    Addr = driver.find_element_by_xpath(f"//*[@id='MainGrid']/tbody/tr[{j}]/td[4]").text
                    Tel = driver.find_element_by_xpath(f"//*[@id='MainGrid']/tbody/tr[{j}]/td[5]").text
                    Office_Time = driver.find_element_by_xpath(f"//*[@id='MainGrid']/tbody/tr[{j}]/td[6]").text
                    
                    LicnoM.append(Licno if Licno else '無')
                    NameM.append(Name if Name else '無')
                    AddrM.append(Addr if Addr else '無')
                    TelM.append(Tel if Tel else '無')
                    Office_TimeM.append(Office_Time if Office_Time else '無')
                    #print(f"\n准照編號: {Licno}\n\n名稱: {Name}\n\n地址: {Addr}\n\n電話:{Tel}\n\n診症時間:{Office_Time}")
                except:
                    #print("前往下一頁\n")
                    break
    except:
        #結束搜索
        print("結束!")
        break

df = pd.DataFrame({'准照編號':LicnoM,'名稱':NameM,'地址':AddrM,'電話':TelM,'診症時間':Office_TimeM})
df.to_excel("診所data.xlsx",sheet_name="Sheet_name_1")
    
    
    #for n in range(2,50):
        #try:
            #N_num = driver.find_element_by_xpath(f"//*[@id='MainGrid']/tbody/tr[{n}]/td[1]").text
            #NL_num = driver.find_element_by_xpath(f"//*[@id='MainGrid']/tbody/tr[{n}]/td[2]").text
            #CP = driver.find_element_by_xpath(f"//*[@id='MainGrid']/tbody/tr[{n}]/td[3]").text
            #Name = driver.find_element_by_xpath(f"//*[@id='MainGrid']/tbody/tr[{n}]/td[4]").text
            #HOC_time = driver.find_element_by_xpath(f"//*[@id='MainGrid']/tbody/tr[{n}]/td[5]").text
            #print(f"序號: {N_num} 准照編號: {NL_num} 專業: {CP} 名稱: {Name} 駐診時間: {HOC_time} \n")
        #except:
            #print(f"共有醫療人員數目: {n-2}")
            #break

#Name = driver.find_elements_by_xpath('//td[3]')
#address = driver.find_elements_by_xpath('//td[4]')
#telephone = driver.find_elements_by_xpath('//td[5]')
#office_hour = driver.find_elements_by_xpath('//td[6]')

#for name in Name:
    #print(name.text)
#for x in telephone:
    #print(x.text)








time.sleep(5)
driver.quit()