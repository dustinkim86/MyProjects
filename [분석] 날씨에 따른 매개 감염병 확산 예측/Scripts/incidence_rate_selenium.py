import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import datetime
import pandas as pd
from dateutil.relativedelta import relativedelta



DRIVER_DIR = 'chromedriver.exe'
driver = webdriver.Chrome(DRIVER_DIR)

# 감염병 포털 url
driver.get("http://www.cdc.go.kr/npt/biz/npp/ist/bass/bassAreaStatsMain.do")
time.sleep(3)

# 감염병명 선택(군)
driver.find_element_by_xpath('//*[@id="areaDissFrm"]/div/ul[2]/li[2]/div[1]/button/div').click()
driver.find_element_by_xpath('//*[@id="areaDissFrm"]/div/ul[2]/li[2]/div[1]/div/ul/li[4]/label/input').click()
# 3군 : //*[@id="areaDissFrm"]/div/ul[2]/li[2]/div[1]/div/ul/li[4]/label/input
# 4군 : //*[@id="areaDissFrm"]/div/ul[2]/li[2]/div[1]/div/ul/li[5]/label/input


# 감염병명 선택(병명)
driver.find_element_by_xpath('//*[@id="areaDissFrm"]/div/ul[2]/li[2]/div[2]/button/div').click()
#driver.find_element_by_xpath('//*[@id="areaDissFrm"]/div/ul[2]/li[2]/div[2]/div/ul/li[20]/label/input').click()
time.sleep(8)
# 말라리아 : //*[@id="areaDissFrm"]/div/ul[2]/li[2]/div[2]/div/ul/li[3]/label/input
# 중증열성혈소판감소증후군 : //*[@id="areaDissFrm"]/div/ul[2]/li[2]/div[2]/div/ul/li[20]/label/input


# 발병률 체크박스 클릭
driver.find_element_by_xpath('//*[@id="areaDissFrm_searchType2"]').click()

# 시작일 종료일 설정
start = datetime.datetime.strptime("2012-01-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2018-12-30", "%Y-%m-%d")
# 시작일부터 종료일까지의 전체 날짜 list
dates = [ start + datetime.timedelta(n) for n in range(int ((end - start).days))]


message = []
day = 0
while day < len(dates) :
    # 검색 시작일 Box
    driver.find_element_by_xpath('//*[@id="areaDissFrmStartDt"]').clear()
    time.sleep(0.3)
    driver.find_element_by_xpath('//*[@id="areaDissFrmStartDt"]').send_keys(dates[day].strftime("%Y-%m-%d"))
    time.sleep(0.3)
    # 검색 종료일 Box
    driver.find_element_by_xpath('//*[@id="areaDissFrmEndDt"]').clear()
    time.sleep(0.3)
    driver.find_element_by_xpath('//*[@id="areaDissFrmEndDt"]').send_keys(dates[day+6].strftime("%Y-%m-%d"))
    time.sleep(0.3)
    # 검색
    driver.find_element_by_xpath('//*[@id="areaDissFrm"]/input[2]').click()
    time.sleep(1)

    # 검색기간의 전국 발병률 데이터 수집
    for idx in range(2,18) :
        temp = []
        for i in range(1,3) :
            xpath = '//*[@id="table"]/tbody/tr[' + str(idx) + ']/td[' + str(i) + ']'
            user_text = driver.find_element_by_xpath(xpath).text
            temp.append(user_text)
        message.append(temp)

    day += 7

####################### End selenium #####################


df = pd.DataFrame(message)
idx = pd.RangeIndex(365)
incidence = pd.DataFrame(df[df[0] == '서울'][1])
incidence.index = idx
locs = list(df[0].unique())
for i in range(1,len(locs)) :
    temp = pd.DataFrame(df[df[0] == locs[i]][1])
    temp.index = idx
    incidence = pd.concat([incidence, temp], axis= 1)

incidence.columns = locs


m_day = []
day = 0
while day < len(dates) :
    m_day.append(dates[day+3].strftime("%Y-%m-%d"))
    day += 7


incidence['date'] = m_day
incidence.set_index(incidence['date'], inplace= True)
del incidence['date']


incidence.to_csv("tsutsu_incidence_rate.csv")

