import pandas as pd
import numpy as np



path = 'imsi_boho.csv'
path
df = pd.read_csv(path, encoding='euc-kr')
df.columns
df['노선명'].unique()
df['HubName'].unique()

['HubName'].unique()
# df[df['HubName'] == '밀알베이커리']['HubDist'].describe()
len(geunro_200['HubName'].unique())
geunro_200 = df[df['HubDist'] <= 500]
geunro_200.columns

"""
concat_df = pd.concat([geunro_500, boho_500], ignore_index= True)
concat_df.columns
concat_df.dropna(inplace= True)
"""
concat_df.to_csv('F:/Google 드라이브/빅데이터캠퍼스 공모전/join_dp_facility.csv')



path3 = 'F:/Google 드라이브/빅데이터캠퍼스 공모전/total_dataset/total_with_spop.csv'
path3
df3 = pd.read_csv(path3, engine='python', index_col=0)
df3.columns
del df3['장애인근로사업장_cnt']; del df3['장애인보호작업장_cnt']



path4 = 'F:/Google 드라이브/빅데이터캠퍼스 공모전/join_dp_f_cnt.csv'
path4
df4 = pd.read_csv(path4, engine='python')
df4.columns


df3['직접재활시설_cnt'] = 0
for i in range(len(df3)) :
    for j in range(len(df4)) :
        if df3.iloc[i, 9] == df4.iloc[j, 0]:
            df3.iloc[i, -1] = df4.iloc[j, -1]
            print(df3.iloc[i, -1])



df3['직접재활시설_cnt'].unique()
df3.to_csv('F:/Google 드라이브/빅데이터캠퍼스 공모전/total_dataset/total_dataset_ver003.csv', index=False)




df2 = pd.read_csv('../복지카드 거주지 데이터/disabled_card_spend.csv', engine='python')
df2

df3 = pd.read_csv('../total_dataset/total_dataset_ver003.csv')
df3


df4 = pd.merge(df3, df2, how='left', on='TOT_REG_CD')
df4[]
df4.to_csv('../total_dataset/total_dataset_ver004.csv', index=False, encoding='euc-kr')




