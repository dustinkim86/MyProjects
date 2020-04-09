
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import minmax_scale, MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor, export_graphviz

df = pd.read_csv('weather_tsutsu_rate.csv', encoding= 'euc-kr')
font_list = font_manager.findSystemFonts()
font_name = font_manager.FontProperties(fname= '/home/jun/.local/share/fonts/NanumGothic.ttf').get_name()
rc('font', family= font_name)

df_fure = df.fillna(0)


scale = MinMaxScaler()
dft = df_fure['temp']
dft = dft.values.flatten()
dft = dft.reshape(dft.shape[0], 1)
dft = scale.fit_transform(dft)
dft.shape
dft = dft.reshape(dft.shape[0])
df['temp'] = dft

df1= df[df['location'] == '서울']

x = df1[['temp', 'humidity', 'wind', 'rain', 'snow']]
x.shape
cols = x.columns

y = df1[[ 'incidence_patients']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state= 42)


# 최적의 하이퍼 파라미터 계산
from sklearn.model_selection import GridSearchCV

param_grid = [
        {'n_estimators': [3, 10, 30, 50, 100, 200], 'max_features': [1,2,3,4, 'auto'], 'random_state': [42]},
        {'bootstrap': [False], 'n_estimators': [3, 5, 10], 'max_features': [2, 3, 4, 5], 'random_state': [42]},
    ]

forest_reg = RandomForestRegressor()
 
grid_search = GridSearchCV(forest_reg, param_grid, cv=5,
                           scoring='neg_mean_squared_error',
                           return_train_score=True)
 
grid_search.fit(x_train, y_train)

grid_search.best_params_

forestbest_reg = grid_search.best_estimator_
forestbest_reg

forestbest_reg.fit(x_train, y_train)

# 그래프
plt.figure(figsize=(10,5))
plt.title('서울 기상기후 변수 중요도')
plt.barh(range(5), forestbest_reg.feature_importances_)
plt.yticks(range(5), cols)
plt.show()







