
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Input, Dense, GRU, Embedding, TimeDistributed
from keras.optimizers import RMSprop, Adam, Adadelta
from keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard, ReduceLROnPlateau

# dataset load
dataset = pd.read_csv("weather_tsutsu_rate.csv", encoding= 'euc-kr', index_col= 0)
locations = list(dataset['location'].unique())

dataset = dataset[dataset['location'] == '인천']
dataset.columns
"""['temp', 'min_temp', 'max_temp', 'rain', 'wind', 'wind_direct',
       'humidity', 'press', 'sunlight_hour', 'snow', 'cloud', 'land_temp',
       'location', 'incidence_patients']"""
dataset = dataset[['temp', 'humidity', 'wind', 'rain', 'snow', 'incidence_patients']]

shift_days = 1
shift_steps = shift_days * 52

# 음수 교차이동으로 새 데이터 프레임 생성
dataset_target = dataset['incidence_patients'].shift(-shift_steps)
dataset_target # 마지막 52개 data NaN

# x data
x_data = dataset.values[0:-shift_steps]
x_data.shape # (313, 9)
# y data
y_data = dataset_target[:-shift_steps]
y_data = y_data.values.flatten()
y_data = y_data.reshape(y_data.shape[0], 1)
y_data.shape # (313, 1)

# data set 관측수
num_data = len(x_data)
num_data # 313
# train
train_split = 0.9

# train set 관측수
num_train = int(train_split * num_data)
num_train # 281
# test set 관측수
num_test = num_data - num_train
num_test # 32

# train / test 입력신호
x_train = x_data[0 : num_train]
x_test = x_data[num_train :]
len(x_train) + len(x_test) # 313

# train / test 출력신호
y_train = y_data[0 : num_train]
y_test = y_data[num_train :]
len(y_train) + len(y_test) # 313

# 입력신호 수
num_x_signals = x_data.shape[1]
num_x_signals # 9
# 출력신호 수
num_y_signals = y_data.shape[1]
num_y_signals # 1


print('min :', np.min(x_train)) # min : -16.60571428571429
print('max :', np.max(x_train)) # max : 1025.397619047619

# scale
scale = MinMaxScaler(feature_range=(0, 1))
x_train_scale = scale.fit_transform(x_train)

print('min :', np.min(x_train_scale)) # min : 0.0
print('max :', np.max(x_train_scale)) # max : 1.000000000000007

x_test_scale = scale.fit_transform(x_test)


y_train_scale = scale.fit_transform(y_train)
y_test_scale = scale.fit_transform(y_test)



def batch_generator(batch_size, sequence_length):
    """
    Generator function for creating random batches of training-data.
    """
    # Infinite loop.
    while True :
        # Allocate a new array for the batch of input-signals.
        x_shape = (batch_size, sequence_length, num_x_signals)
        x_batch = np.zeros(shape=x_shape, dtype=np.float16)
        # Allocate a new array for the batch of output-signals.
        y_shape = (batch_size, sequence_length, num_y_signals)
        y_batch = np.zeros(shape=y_shape, dtype=np.float16)
        # Fill the batch with random sequences of data.
        for i in range(batch_size):
            # Get a random start-index.
            # This points somewhere into the training-data.
            idx = np.random.randint(num_train - sequence_length)
        
            # Copy the sequences of data starting at this index.
            x_batch[i] = x_train_scale[idx:idx+sequence_length]
            y_batch[i] = y_train_scale[idx:idx+sequence_length]

        yield (x_batch, y_batch)


batch_size = 2

sequence_length = shift_steps * 3
sequence_length # 156

# 배치 생성기
generator = batch_generator(batch_size=batch_size,
                            sequence_length=sequence_length)
"""
# 배치 생성기 테스트
x_batch, y_batch = next(generator)

print(x_batch.shape) # (2, 156, 9)
print(y_batch.shape) # (2, 156, 1)


batch = 0; signal = 0
# 입력신호 테스트
seq = x_batch[batch, : , signal]
plt.plot(seq)

# 출력신호 테스트
seq = y_batch[batch, : , signal]
plt.plot(seq)
"""
# 검증 set
validation_data = (np.expand_dims(x_test_scale, axis=0),
                   np.expand_dims(y_test_scale, axis=0))


model = Sequential()
model.add(GRU(units=32, return_sequences=True, activation='relu',
              input_shape=(None, num_x_signals,)))
model.add(TimeDistributed(Dense(num_y_signals, activation='sigmoid')))


if False:
    from tensorflow.python.keras.initializers import RandomUniform
    # Maybe use lower init-ranges.
    init = RandomUniform(minval=-0.05, maxval=0.05)
    
    model.add(Dense(num_y_signals, activation='linear',
                    kernel_initializer=init))

# 손실 함수
warmup_steps = 5

def loss_mse_warmup(y_true, y_pred):
    y_true_slice = y_true[:, warmup_steps:, :]
    y_pred_slice = y_pred[:, warmup_steps:, :]
    loss = tf.losses.mean_squared_error(labels=y_true_slice,
    predictions=y_pred_slice)
    loss_mean = tf.reduce_mean(loss)
    return loss_mean


# 모델 컴파일
optimizer = RMSprop(lr=1e-3)

model.compile(loss=loss_mse_warmup, optimizer=optimizer)
model.summary()
"""
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
gru_4 (GRU)                  (None, None, 32)          4032      
_________________________________________________________________
dense_4 (Dense)              (None, None, 1)           33        
=================================================================
Total params: 4,065
Trainable params: 4,065
Non-trainable params: 0
_________________________________________________________________
"""
path_checkpoint = '23_checkpoint.keras'
callback_checkpoint = ModelCheckpoint(filepath=path_checkpoint,
                                      monitor='val_loss',
                                      verbose=1,
                                      save_weights_only=True,
                                      save_best_only=True)

callback_early_stopping = EarlyStopping(monitor='val_loss',
                                        patience=5, verbose=1)

callback_tensorboard = TensorBoard(log_dir='./23_logs/',
                                   histogram_freq=0,
                                   write_graph=False)

callback_reduce_lr = ReduceLROnPlateau(monitor='val_loss',
                                       factor=0.1,
                                       min_lr=1e-4,
                                       patience=0,
                                       verbose=1)

callbacks = [callback_early_stopping,
             callback_checkpoint,
             callback_tensorboard,
             callback_reduce_lr]


# 순환신경망 학습
model.fit_generator(generator=generator,
                    epochs=100,
                    steps_per_epoch=100,
                    validation_data=validation_data,
                    callbacks=callbacks)

# 체크포인트 읽어들이기
try:
    model.load_weights(path_checkpoint)
except Exception as error:
    print("Error trying to load checkpoint.")
    print(error)




######################
## 저장모델 이용하기
######################
    
# 모델 / 가중치 저장 및 불러오기
# 모델 json 형식 저장
model_json = model.to_json()
with open("model.json", "w") as json_file : 
    json_file.write(model_json)
# 가중치 h5 형식 저장
model.save_weights("model.h5")
print("모델 가중치 저장 완료")


# 저장모델 불러오기
from keras.models import model_from_json
json_file = open("model.json", "r")
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# 불러 온 모델에 가중치 적용
loaded_model.load_weights("model.h5")
print("모델 가중치 불러오기 완료")

# 모델 컴파일
optimizer = RMSprop(lr=1e-3)
loaded_model.compile(loss=loss_mse_warmup, optimizer=optimizer)
    



###############
## 분석 검증
###############

# 테스트에 대한 성능
result = model.evaluate(x=np.expand_dims(x_test_scale, axis=0),
                        y=np.expand_dims(y_test_scale, axis=0))

print("loss (test-set):", result)

# 만약 여러가지 측정치를 사용한다면 다음의 방법으로 측정할 수 있습니다.
if False:
    for res, metric in zip(result, model.metrics_names):
        print("{0}: {1:.3e}".format(metric, res))



# 예측값 만들기
def plot_comparison(start_idx, length=100, train=True):
    # 한글 지원 : 한글 깨짐 방지
    from matplotlib import font_manager, rc
    font_name = font_manager.FontProperties(fname= '/home/jun/.local/share/fonts/NanumGothic.ttf').get_name()
    rc('font', family=font_name)
    
    if train:
        # Use training-data.
        x = x_train_scale
        y_true = y_train
    else:
        # Use test-data.
        x = x_test_scale
        y_true = y_test

    # End-index for the sequences.
    end_idx = start_idx + length
    
    # Select the sequences from the given start-index and
    # of the given length.
    x = x[start_idx:end_idx]
    y_true = y_true[start_idx:end_idx]
    
    # Input-signals for the model.
    x = np.expand_dims(x, axis=0)
    # Use the model to predict the output-signals.
    y_pred = model.predict(x)
    y_pred_rescaled = scale.inverse_transform(y_pred[0])

    # For each output-signal.
    for signal in range(0, 1):
        # Get the output-signal predicted by the model.
        signal_pred = y_pred_rescaled[:, signal]
        
        # Get the true output-signal from the data-set.
        signal_true = y_true[:, signal]
        # Make the plotting-canvas bigger.
        plt.figure(figsize=(12,5))
        
        # Plot and compare the two signals.
        plt.plot(signal_true, label='true_data')
        plt.plot(signal_pred, label='predictions')
        
        # Plot grey box for warmup-period.
        p = plt.axvspan(0, warmup_steps, facecolor='black', alpha=0.15)
        
        # Plot labels etc.
        plt.title('발병률 예측 모델 : 쯔쯔가무시증')
        plt.ylabel('incidence_patients')
        plt.legend()
        plt.show()


plot_comparison(start_idx=1, length=1000, train=True)
plot_comparison(start_idx=1, length=1000, train=False)



######################################
### 날씨 API (00:00 ~ 04:59 사용불가)
######################################
def cordinate() :
    import requests
    import pandas as pd
    from datetime import datetime
    
    # 지역별 API 좌표 DataFrame 생성
    x_y = pd.DataFrame({'seoul' : [60, 125], 'busan' : [98, 77], 'daegu' : [90, 91],
                    'incheon' : [55, 124], 'kwangju' : [59, 75], 'daejeon' : [67, 101],
                    'ulsan' : [102, 84], 'kyunggi' : [62, 126], 'kangwon' : [84, 132],
                    'chungbuk' : [73, 107], 'chungnam' : [58, 102], 'jeonbuk' : [61, 84],
                    'jeonnam' : [57, 65], 'kyungbuk' : [94, 106], 'kyungnam' : [85, 77],
                    'jeju' : [56, 33]})
    x_y.index = ['X', 'Y']
    x_y = x_y.T
    
    # url 및 key 생성
    url = 'http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData'
    API = 'your_api_key'
    date = datetime.today().strftime("%Y%m%d%H%M%S")[:8]
    
    # parameter 생성
    queryParams = '?'+'ServiceKey='+ API \
    +'&base_date='+ date \
    +'&base_time='+'0500'\
    +'&nx='+ str(x_y.iloc[0, 0]) \
    +'&ny='+ str(x_y.iloc[0, 1]) \
    +'&numOfRows='+'184'\
    +'&pageNo='+'1'\
    +'&_type='+'json'
    
    # 결과값 저장
    url = url+queryParams
    result = requests.get(url)
    obj = result.json()
    obj1 = obj['response']['body']['items']['item'][9:20]
    obj2 = obj['response']['body']['items']['item'][91:102]
    obj3 = obj['response']['body']['items']['item'][173:184]
    
    # 결과값 -> DataFrame으로 변환
    data1 = []; data2 = []; data3 = []
    for i in obj1:
        data1.append([i['category'],i['fcstValue']] )
    for i in obj2:
        data2.append([i['fcstValue']] )
    for i in obj3:
        data3.append([i['fcstValue']] )
    
    df = pd.DataFrame(data1); d2 = pd.DataFrame(data2); d3 = pd.DataFrame(data3)
    df = pd.concat([df, d2], axis = 1); df = pd.concat([df, d3], axis = 1)
    df.columns = ['a', 'b', 'c', 'd']
    del df['a']; df1 = df.T
    temp1 = df1[2]; temp2 = df1[3]; temp3 = df1[4]; temp4 = df1[6]; temp5 = df1[10]

    df2 = pd.DataFrame(temp1)
    df2 = df2.merge(temp2, 'outer', left_index= True, right_index= True)
    df2 = df2.merge(temp3, 'outer', left_index= True, right_index= True)
    df2 = df2.merge(temp4, 'outer', left_index= True, right_index= True)
    df2 = df2.merge(temp5, 'outer', left_index= True, right_index= True)
    df2.reset_index(inplace= True); del df2['index']
    
    lst = df2
    for i in range(1, len(x_y)):
        url = 'http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData'
        API = 'your_api_key'
        date = datetime.today().strftime("%Y%m%d%H%M%S")[:8]
        
        queryParams = '?'+'ServiceKey='+ API \
        +'&base_date='+ date \
        +'&base_time='+'0500'\
        +'&nx='+ str(x_y.iloc[i, 0]) \
        +'&ny='+ str(x_y.iloc[i, 1]) \
        +'&numOfRows='+'184'\
        +'&pageNo='+'1'\
        +'&_type='+'json'
        
        url = url+queryParams
        result = requests.get(url)
        obj = result.json()
        obj1 = obj['response']['body']['items']['item'][9:20]
        obj2 = obj['response']['body']['items']['item'][91:102]
        obj3 = obj['response']['body']['items']['item'][173:184]
        
        data1 = []; data2 = []; data3 = []
        for i in obj1:
            data1.append([i['category'],i['fcstValue']] )
        for i in obj2:
            data2.append([i['fcstValue']] )
        for i in obj3:
            data3.append([i['fcstValue']] )
        
        df = pd.DataFrame(data1); d2 = pd.DataFrame(data2); d3 = pd.DataFrame(data3)
        df = pd.concat([df, d2], axis = 1); df = pd.concat([df, d3], axis = 1)
        df.columns = ['a', 'b', 'c', 'd']
        del df['a']; df1 = df.T
        temp1 = df1[2]; temp2 = df1[3]; temp3 = df1[4]; temp4 = df1[6]; temp5 = df1[10]
        df2 = pd.DataFrame(temp1)
        df2 = df2.merge(temp2, 'outer', left_index= True, right_index= True)
        df2 = df2.merge(temp3, 'outer', left_index= True, right_index= True)
        df2 = df2.merge(temp4, 'outer', left_index= True, right_index= True)
        df2 = df2.merge(temp5, 'outer', left_index= True, right_index= True)
        df2.reset_index(inplace= True); del df2['index']
        
        lst = pd.concat([lst, df2], axis= 0)
        
    lst.columns = ['rain', 'humidity', 'snow','temp', 'Wind' ]
    lst.reset_index(inplace= True); del lst['index']
    return lst

weather_API = cordinate()


#############################
#### API data로 발병률 예측
#############################
def plot_API(weather_API) :
    import datetime
    from sklearn.preprocessing import MinMaxScaler
    # 한글 지원 : 한글 깨짐 방지
    from matplotlib import font_manager, rc
    font_name = font_manager.FontProperties(fname= '/home/jun/.local/share/fonts/NanumGothic.ttf').get_name()
    rc('font', family=font_name)
    # 음수 기호 깨짐 방지
    import matplotlib
    matplotlib.rcParams['axes.unicode_minus'] = False
    
    # 오늘, 내일, 모레 날짜 load
    today = datetime.datetime.today()
    tomorrow = today + datetime.timedelta(days = 1)
    da_tomorrow = today + datetime.timedelta(days = 2)
    tod = today.isoformat("#","hours").split('#')[0]
    tom = tomorrow.isoformat("#","hours").split('#')[0]
    da_tom = da_tomorrow.isoformat("#","hours").split('#')[0]
    date = [tod, tom, da_tom]
    
    locations = ['서울','부산','대구','인천','광주','대전','울산','경기',
                 '강원','충북','충남','전북','전남','경북','경남','제주']

    # API load
    temp_df = weather_API.iloc[0:3, :]
    temp_df['patients'] = [0.0, 0.0, 0.0]
    x = temp_df.values

    scale = MinMaxScaler(feature_range=(0, 1))
    x = scale.fit_transform(x)
    x = np.expand_dims(x, axis=0)
    
    y = temp_df['patients']
    y = y.values.flatten()
    y = y.reshape(y.shape[0], 1)
    y = scale.fit_transform(y)
    y_true = y
    
    y_pred = model.predict(x)
    y_pred.shape
    y_pred_rescaled = scale.inverse_transform(y_pred[0])
    y_pred_rescaled.shape
    
    # 예측 발병률 graph
    fig, ax = plt.subplots()
    plt.plot_date(date, y_pred_rescaled, '-')
    plt.title(f'{locations[0]}의 {tod} ~ {da_tom} 예상 발병률')
    plt.xlabel('Date')
    plt.ylabel('incidence_patients')
    ax.xaxis.set_tick_params(labelsize=10)
    plt.show()
    fig.savefig(r'images\predict_서울.png', format='png')
    
    predict_data = pd.DataFrame(y_pred_rescaled)
    loc_num = 1
    idx = 3
    while idx < 48 :

        temp_df = weather_API.iloc[idx:idx+3, :]
        temp_df['patients'] = [0.0, 0.0, 0.0]
        x = temp_df.values
    
        scale = MinMaxScaler(feature_range=(0, 1))
        x = scale.fit_transform(x)
        x = np.expand_dims(x, axis=0)
        
        y = temp_df['patients']
        y = y.values.flatten()
        y = y.reshape(y.shape[0], 1)
        y = scale.fit_transform(y)
        y_true = y
        
        y_pred = model.predict(x)
        y_pred.shape
        y_pred_rescaled = scale.inverse_transform(y_pred[0])
        y_pred_rescaled.shape
        
        predict_data = pd.concat(
                [predict_data, pd.DataFrame(y_pred_rescaled)], axis= 1)
        
        # 예측 발병률 graph
        fig, ax = plt.subplots()
        plt.plot_date(date, y_pred_rescaled, '-')
        plt.title(f'{locations[loc_num]}의 예상 발병률')
        plt.xlabel('Date')
        plt.ylabel('incidence_patients')
        ax.xaxis.set_tick_params(labelsize=10)
        plt.show()
        fig.savefig(f'images\predict_{locations[loc_num]}.png', format='png')
        
        idx += 3
        loc_num += 1
    
    predict_data.reset_index(inplace= True); del predict_data['index']
    predict_data.columns = locations
    predict_data = predict_data.T
    predict_data.columns = ['today', 'tomorrow', 'day_after_tomorrow']
    predict_data = predict_data.T
    return predict_data


pred_data = plot_API(weather_API)


#################################
## 전국 3일간 발병률 예측 그래프
#################################
import seaborn as sns

sns.set(style="white", context="talk")

# Set up the matplotlib figure
f, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(15, 8), sharex=True)

# 한글 지원 : 한글 깨짐 방지
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname= '/home/jun/.local/share/fonts/NanumGothic.ttf').get_name()
rc('font', family=font_name)

sns.barplot(x=pred_data.columns, y=pred_data.loc['today',:], palette="rocket", ax=ax1)
for p in ax1.patches:
    ax1.annotate(format(p.get_height(), '.2f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha = 'center', va = 'center', xytext = (0, 10),
                   textcoords = 'offset points')
ax1.axhline(0, color="k", clip_on=False)
#ax1.set_ylabel("오늘")
ax1.set_title('예측 발병률(오늘)')

sns.barplot(x=pred_data.columns, y=pred_data.loc['tomorrow',:], palette="vlag", ax=ax2)
for p in ax2.patches:
    ax2.annotate(format(p.get_height(), '.2f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha = 'center', va = 'center', xytext = (0, 10),
                   textcoords = 'offset points')
ax2.axhline(0, color="k", clip_on=False)
#ax2.set_ylabel("내일")
ax2.set_title('예측 발병률(내일)')


sns.barplot(x=pred_data.columns, y=pred_data.loc['day_after_tomorrow',:], palette="deep", ax=ax3)
for p in ax3.patches:
    ax3.annotate(format(p.get_height(), '.2f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha = 'center', va = 'center', xytext = (0, 10),
                   textcoords = 'offset points')
ax3.axhline(0, color="k", clip_on=False)
#ax3.set_ylabel("모레")
ax3.set_title('예측 발병률(모레)')

# Finalize the plot
sns.despine(bottom=True)
plt.setp(f.axes, yticks=[])
plt.tight_layout(h_pad=2)


