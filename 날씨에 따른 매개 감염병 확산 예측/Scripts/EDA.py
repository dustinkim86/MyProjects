
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from sklearn.preprocessing import MinMaxScaler

font_list = font_manager.findSystemFonts()
font_name = font_manager.FontProperties(fname= '/home/jun/.local/share/fonts/NanumGothic.ttf').get_name()
rc('font', family= font_name)

df = pd.read_csv('weather_tsutsu_rate.csv', encoding= 'euc-kr')


scale = MinMaxScaler()
dft = df['temp']
dft = dft.values.flatten()
dft = dft.reshape(dft.shape[0], 1)
dft = scale.fit_transform(dft)
dft.shape
dft = dft.reshape(dft.shape[0])
df['temp'] = dft

df1= df[df['location'] == '서울']
df1 = df1[['date', 'temp', 'humidity', 'wind', 'rain', 'snow', 'incidence_patients']]

df2 = df[df['location'] == '강원']
df2 = df2[['date', 'temp', 'humidity', 'wind', 'rain', 'snow', 'incidence_patients']]


df1['incidence_patients'].mean() # 서울 7년간 평균 0.061945205479452134
df2['incidence_patients'].mean() # 강원 7년간 평균 0.05630136986301368

seoul = []; kangwon = []
for year in range(2012, 2019) :
      seoul.append(df1[df1['date'].str.contains(str(year))]['incidence_patients'].mean())
      kangwon.append(df2[df2['date'].str.contains(str(year))]['incidence_patients'].mean())

# 서울 / 강원 발병률 추이
plt.figure(figsize= (10,5))
plt.plot(seoul, label= '서울', marker= 'o')
plt.plot(kangwon, label= '강원', marker= 'o')
plt.legend(loc= 'best')
plt.xticks(np.arange(0,7), range(2012,2019))
plt.xlabel('연도')
plt.ylabel('발병률')
plt.title('서울 / 강원 발병률 추이')
plt.show()


df['location'].unique()
d1 = []; d2 = []; d3 = []; d4 = []; d5 = []; d6 = []; d7 = []; d8 = []
d9 = []; d10 = []; d11 = []; d12 = []; d13 = []; d14 = []; d15 = []; d16 = []
for year in range(2012, 2019) :
      d1.append(df[df['date'].str.contains(str(year))][df['location']=='서울']['incidence_patients'].mean())
      d2.append(df[df['date'].str.contains(str(year))][df['location']=='강원']['incidence_patients'].mean())
      d3.append(df[df['date'].str.contains(str(year))][df['location']=='경기']['incidence_patients'].mean())
      d4.append(df[df['date'].str.contains(str(year))][df['location']=='인천']['incidence_patients'].mean())
      d5.append(df[df['date'].str.contains(str(year))][df['location']=='경북']['incidence_patients'].mean())
      d6.append(df[df['date'].str.contains(str(year))][df['location']=='충북']['incidence_patients'].mean())
      d7.append(df[df['date'].str.contains(str(year))][df['location']=='충남']['incidence_patients'].mean())
      d8.append(df[df['date'].str.contains(str(year))][df['location']=='대전']['incidence_patients'].mean())
      d9.append(df[df['date'].str.contains(str(year))][df['location']=='전북']['incidence_patients'].mean())
      d10.append(df[df['date'].str.contains(str(year))][df['location']=='대구']['incidence_patients'].mean())
      d11.append(df[df['date'].str.contains(str(year))][df['location']=='울산']['incidence_patients'].mean())
      d12.append(df[df['date'].str.contains(str(year))][df['location']=='경남']['incidence_patients'].mean())
      d13.append(df[df['date'].str.contains(str(year))][df['location']=='광주']['incidence_patients'].mean())
      d14.append(df[df['date'].str.contains(str(year))][df['location']=='부산']['incidence_patients'].mean())
      d15.append(df[df['date'].str.contains(str(year))][df['location']=='전남']['incidence_patients'].mean())
      d16.append(df[df['date'].str.contains(str(year))][df['location']=='제주']['incidence_patients'].mean())
      

# 전국 발병률 추이
plt.figure(figsize= (10,5))
plt.plot(d1, label= '서울'); plt.plot(d2, label= '강원')
plt.plot(d3, label= '경기'); plt.plot(d4, label= '인천')
plt.plot(d5, label= '경북'); plt.plot(d6, label= '충북')
plt.plot(d7, label= '충남'); plt.plot(d8, label= '대전')
plt.plot(d9, label= '전북'); plt.plot(d10, label= '대구')
plt.plot(d11, label= '울산'); plt.plot(d12, label= '경남')
plt.plot(d13, label= '광주'); plt.plot(d14, label= '부산')
plt.plot(d15, label= '전남'); plt.plot(d16, label= '제주')
plt.legend(loc= 'best')
plt.xticks(np.arange(0,7), range(2012,2019))
plt.xlabel('연도')
plt.ylabel('발병률')
plt.title('전국 발병률 추이')
plt.show()





# 지역별 발병률 평균 비교
df['location'].unique()
d1 = []

d1.append(df[df['location']=='서울']['incidence_patients'].mean())
d1.append(df[df['location']=='강원']['incidence_patients'].mean())
d1.append(df[df['location']=='경기']['incidence_patients'].mean())
d1.append(df[df['location']=='인천']['incidence_patients'].mean())
d1.append(df[df['location']=='경북']['incidence_patients'].mean())
d1.append(df[df['location']=='충북']['incidence_patients'].mean())
d1.append(df[df['location']=='충남']['incidence_patients'].mean())
d1.append(df[df['location']=='대전']['incidence_patients'].mean())
d1.append(df[df['location']=='전북']['incidence_patients'].mean())
d1.append(df[df['location']=='대구']['incidence_patients'].mean())
d1.append(df[df['location']=='울산']['incidence_patients'].mean())
d1.append(df[df['location']=='경남']['incidence_patients'].mean())
d1.append(df[df['location']=='광주']['incidence_patients'].mean())
d1.append(df[df['location']=='부산']['incidence_patients'].mean())
d1.append(df[df['location']=='전남']['incidence_patients'].mean())
d1.append(df[df['location']=='제주']['incidence_patients'].mean())


locs = ['서울','강원','경기','인천','경북','충북','충남','대전','전북','대구','울산','경남','광주','부산','전남','제주']      
d1 = pd.Series(d1)

plt.figure(figsize= (11,5))
d1.plot(kind= 'barh')
plt.yticks(np.arange(0,16), locs)
plt.xlabel('발병률')
plt.ylabel('지역')
plt.title('지역별 발병률 평균 비교')
plt.show()



# df['humidity'][df['location']=='광주'].plot(kind= 'hist')
# df['humidity'][df['location']=='대구'].plot(kind= 'hist')
# df['temp'][df['location']=='광주'].plot(kind= 'hist')








