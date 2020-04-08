
import pandas as pd
import numpy as np
import datetime


# 관측소 code의 16개 지역명으로 변환하기 위한 dict 생성
data = {'108':'서울','116':'서울',
        '159':'부산',
        '143':'대구','176':'대구',
        '201':'인천','102':'인천','112':'인천',
        '156':'광주',
        '133':'대전',
        '152':'울산',
        '98':'경기','119':'경기','202':'경기','203':'경기','99':'경기',
        '105':'강원','100':'강원','106':'강원','104':'강원','93':'강원',
        '214':'강원','90':'강원','121':'강원','114':'강원','211':'강원',
        '217':'강원','95':'강원','101':'강원','216':'강원','212':'강원',
        '226':'충북','221':'충북','131':'충북','135':'충북','127':'충북',
        '238':'충남','235':'충남','236':'충남','129':'충남','232':'충남',
        '177':'충남',
        '172':'전북','251':'전북','140':'전북','247':'전북','243':'전북',
        '254':'전북','244':'전북','248':'전북','146':'전북','245':'전북',
        '259':'전남','262':'전남','266':'전남','165':'전남','164':'전남',
        '258':'전남','174':'전남','168':'전남','252':'전남','170':'전남',
        '260':'전남','256':'전남','175':'전남','268':'전남','261':'전남',
        '169':'전남',
        '283':'경북','279':'경북','273':'경북','271':'경북','137':'경북',
        '136':'경북','277':'경북','272':'경북','281':'경북','115':'경북',
        '130':'경북','278':'경북','276':'경북','138':'경북',
        '294':'경남','284':'경남','253':'경남','295':'경남','288':'경남',
        '255':'경남','289':'경남','257':'경남','263':'경남','192':'경남',
        '155':'경남','162':'경남','264':'경남','285':'경남',
        '185':'제주','189':'제주','188':'제주','187':'제주','265':'제주',
        '184':'제주'}

# 16개 지역명 code화 하기위한 dict 생성
loc_number_dict = {
        '강원':'1001', '경기':'1002', '인천':'1003', '서울':'1004', '경북':'1005',
        '충북':'1006', '충남':'1007', '대전':'1008', '전북':'1009', '대구':'1010',
        '울산':'1011', '경남':'1012', '광주':'1013', '부산':'1014', '전남':'1015',
        '제주':'1016'
        }


# 2012~2018년 기상 data load
weather_data = pd.read_csv("weather_data.csv", encoding='euc-kr')
weather_data.info()
cols = ['code', 'date', 'temp', 'min_temp', 'max_temp', 'rain', 'wind', 'wind_direct', 'humidity', 'press', 'sunlight_hour', 'snow', 'cloud', 'land_temp']
weather_data.columns = cols


# 관측소code별 지역명 삽입 process
loc_name = []
for i in range(len(weather_data)) :
    for key in data.keys() :
        if weather_data.loc[i, 'code'] == int(key) :
            loc_name.append(data[key])
weather_data['지역명'] = loc_name


# 지역별 code화 삽입 process
loc_num = []
for i in range(len(weather_data)) :
    for key in loc_number_dict.keys() :
        if weather_data.loc[i, '지역명'] == key :
            loc_num.append(loc_number_dict[key])
weather_data['loc_code'] = loc_num

# 날짜(2012~2018년) dataset 생성
days = pd.date_range("2012, 01, 01", "2018, 12, 30")


# string type -> date type 변환
weather_data['date'] = pd.to_datetime(weather_data['date'])
# string type -> int type 변환
weather_data['loc_code'] = weather_data['loc_code'].astype('int32')


# 지역명 추출 list
locs = list(weather_data['지역명'].unique())


# 지역명 및 일시(날짜)별 추출
weather = []
for loc in locs :
    for day in days :
        weather.append(weather_data[(weather_data['지역명'] == loc) & (weather_data['date'] == day)])
        

# 추출data list -> dataframe 변환
df = weather[0]
for i in range(1, len(weather)) :
    temp = pd.DataFrame(weather[i])
    df = pd.concat([df, temp], axis= 0)
    

# string -> date type으로 변환
df['date'] = pd.to_datetime(df['date'])
# string -> numeric type으로 변환
df['loc_code'] = pd.to_numeric(df['loc_code'])


# 지역코드 추출 list
num_locs = list(df['loc_code'].unique())


# 일시(날짜) 및 지역코드별 추출
daily_and_code = []
for num_loc in num_locs :
    for day in days :
        #print(day)
        daily_and_code.append(df[(df['date'] == day) & (df['loc_code'] == num_loc)].mean())


# 추출data list -> dataframe 변환
daily_df = pd.DataFrame(daily_and_code)
daily_df = daily_df[daily_df['loc_code'].isna() == False]

# float -> int type 변환
daily_df['loc_code'] = daily_df['loc_code'].astype('int32')


# daily weather 중간 저장
daily_df.to_csv("daily_weather.csv", index=False)
weather = daily_df

# daily weather csv 읽어오기
# weather = pd.read_csv('daily_weather.csv')
del weather['date']; del weather['지역명']


# loc_code 고유data list저장
num_locs = list(weather['loc_code'].unique())

# loc_code별 그룹화
weather_g = weather.groupby('loc_code')

# 그룹별 daily -> week로 평균계산(7일 -> 1주)
week = []
for i in weather_g.groups :
    idx = 0
    while idx <= 2555 :
        week.append(weather[weather['loc_code'] == i][idx:idx+7].mean())
        idx += 7

# list -> dataframe 변환
week_df = pd.DataFrame(week)

# code 컬럼에 nan값이 있을 경우 해당 row 삭제
week_df = week_df[week_df['code'].isna() == False]

# float -> int type 변환
week_df['loc_code'] = week_df['loc_code'].astype('int32')


week_df['rain'].fillna(0, inplace= True)
week_df['snow'].fillna(0, inplace= True)

week_df[week_df['loc_code'] == 1004]
week_df.info()
week_df.reset_index(inplace= True)
del week_df['index']


loc_name = []
for i in range(len(week_df)) :
    for key, val in loc_number_dict.items() :
        if week_df.loc[i, 'loc_code'] == int(val) :
            loc_name.append(key)
## loc_name
week_df['location'] = loc_name
week_df[week_df['location'] == '서울']

locs = list(week_df['location'].unique())
data = []
for loc in locs :
    temp = []
    for i in range(len(week_df)) :
        if week_df.iloc[i, -1] == loc :
            temp.append(week_df.iloc[i, :])
    data.append(temp)

data2 = sum(data, [])
df = pd.DataFrame(data2)
del df['loc_code']; del df['code']

# 날짜 index 부여
start = datetime.datetime.strptime("2012-01-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2018-12-30", "%Y-%m-%d")
dates = [ start + datetime.timedelta(n) for n in range(int ((end - start).days))]

m_day = []
day = 0
while day < len(dates) :
    m_day.append(dates[day+3].strftime("%Y-%m-%d"))
    day += 7
len(m_day)


df['date'] = m_day * 16
df.index = df['date']
del df['date']
df.reset_index(inplace= True)


# week weather 중간 저장
df.to_csv("week_weather.csv", index=False)
df = pd.read_csv("week_weather.csv", index_col= 0)




"""disease data load"""
disease = pd.read_csv("malaria_incidence_rate.csv", index_col= 0, encoding='euc-kr')
disease_arr = np.array(disease)

temp_df = pd.DataFrame(disease_arr[:,0])
for i in range(1,16) :
    temp = pd.DataFrame(disease_arr[:,i])
    temp_df = pd.concat([temp_df, temp], axis= 0)

temp_df = list(temp_df[0])
len(temp_df)

df['incidence_patients'] = temp_df

# week weather dataset csv 저장
df.to_csv('weather_malaria_rate.csv', encoding= 'euc-kr')
