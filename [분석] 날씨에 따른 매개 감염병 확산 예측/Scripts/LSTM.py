# -*- coding: utf-8 -*-
"""
상태유지 스택 순환신경망 모델
"""

# 0. 사용할 패키지 불러오기
import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

def create_dataset(signal_data, look_back=1):
    dataX, dataY = [], []
    for i in range(len(signal_data)-look_back):
        dataX.append(signal_data[i:(i+look_back), 0])
        dataY.append(signal_data[i + look_back, 0])
    return np.array(dataX), np.array(dataY)

class CustomHistory(keras.callbacks.Callback):
    def init(self):
        self.train_loss = []
        self.val_loss = []
        
    def on_epoch_end(self, batch, logs={}):
        self.train_loss.append(logs.get('loss'))
        self.val_loss.append(logs.get('val_loss'))

look_back = 13

# 1. 데이터셋 생성하기


dataset = pd.read_csv("tsutsu_winter_rate.csv", encoding='euc-kr', index_col=0)
#dataset = dataset[dataset['location'] == '전북']
dataset = dataset[['temp', 'humidity', 'wind', 'rain', 'snow', 'incidence_patients']]
dataset

x_cols = dataset
x_cols.shape # (365, 6)

y_cols = dataset['incidence_patients']
y_cols.shape # (365,)
signal_data = dataset

signal_data = pd.concat([x_cols, y_cols], axis = 1)
#signal_data = signal_data.fillna(0)
signal_data.shape # (365, 7)

# 데이터 전처리
scaler = MinMaxScaler(feature_range=(0, 1))
signal_data = scaler.fit_transform(signal_data)
signal_data.shape

# 데이터 분리
#train = signal_data[:261]
#val = signal_data[261:313]
#test = signal_data[313:]

#train = signal_data[:900]
#val = signal_data[900:1200]
#test = signal_data[1200:]

train, temp = train_test_split(signal_data, test_size= 0.4)
val, test = train_test_split(temp, test_size= 0.5)


# 데이터셋 생성
x_train, y_train = create_dataset(train, look_back)
x_val, y_val = create_dataset(val, look_back)
x_test, y_test = create_dataset(test, look_back)

# 데이터셋 전처리
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_val = np.reshape(x_val, (x_val.shape[0], x_val.shape[1], 1))
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
x_train.shape # (221, 40, 1)
x_val.shape # (12, 40, 1)
x_test.shape # (12, 40, 1)
# 2. 모델 구성하기
model = Sequential()
for i in range(2):
    model.add(LSTM(32, batch_input_shape=(1, look_back, 1), stateful=True, return_sequences=True))
    model.add(Dropout(0.3))
model.add(LSTM(32, batch_input_shape=(1, look_back, 1), stateful=True))
#model.add(Dropout(0.3))
model.add(Dense(1, activation='sigmoid'))

# 3. 모델 학습과정 설정하기
model.compile(loss='mean_squared_error', optimizer='rmsprop')

# 4. 모델 학습시키기
custom_hist = CustomHistory()
custom_hist.init()

for i in range(10):
    model.fit(x_train, y_train, epochs=1, batch_size=1, shuffle=False, callbacks=[custom_hist], validation_data=(x_val, y_val))
    model.reset_states()

# 5. 학습과정 살펴보기
plt.figure(figsize=(12,5))
plt.plot(custom_hist.train_loss)
plt.plot(custom_hist.val_loss)
plt.ylim(0.0, 0.15)
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train_data', 'val_data'], loc='upper left')
plt.show()

# 6. 모델 평가하기
trainScore = model.evaluate(x_train, y_train, batch_size=1, verbose=0)
model.reset_states()
print('Train Score: ', trainScore)
valScore = model.evaluate(x_val, y_val, batch_size=1, verbose=0)
model.reset_states()
print('Validataion Score: ', valScore)
testScore = model.evaluate(x_test, y_test, batch_size=1, verbose=0)
model.reset_states()
print('Test Score: ', testScore)

# 7. 모델 사용하기
look_ahead = 91
xhat = x_test[0]
predictions = np.zeros((look_ahead,1))
for i in range(look_ahead):
    prediction = model.predict(np.array([xhat]), batch_size=1)
    predictions[i] = prediction
    xhat = np.vstack([xhat[1:],prediction])
    
plt.figure(figsize=(12,5))
plt.plot(np.arange(look_ahead),predictions,'r',label="prediction")
plt.plot(np.arange(look_ahead),y_test[:look_ahead],label="true_data")
plt.legend(loc= 'best')
plt.title('말라리아 : 발병률 data와 예측 data 비교 graph')
plt.show()










