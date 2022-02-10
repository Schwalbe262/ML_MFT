# module import

import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

from pycaret.regression import *

from sklearn.model_selection import train_test_split 
from sklearn import metrics
from lightgbm import LGBMRegressor
from sklearn.model_selection import KFold

from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error 

import os


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.options.display.max_seq_items = None



# data import

filename = os.path.abspath("")+"/../Data_2021_10_14_v1 (N98923)/Data.csv" # csv file directory and name

#print(filename)

raw_data = pd.read_csv(filename)


# 학습할 파라미터를 제외한 나머지 아웃풋 삭제
output = ["Lmt","Lmr","Llt","Llr","k","Lt","Lr","Lm","Rt","Rr","I1","I2","Zt","Zr","Zm","copperloss_tx","copperloss_rx"]
parameter = "Llt"
output.remove(parameter)

for pam in output :
    raw_data = raw_data.drop(columns=pam)

# NaN 데이터 삭제
raw_data = raw_data.dropna()


# target 변수 제외
col_input = list(raw_data.columns)[:-1]
print(col_input)


print ("OUTLIER START")

# outlier 탐색 및 제거
outlier_index = {}
for i, colName in enumerate(col_input):
    data = raw_data[f'{colName}']
    # column 데이터만 추출, 1/4 분위와 3/4 분위 지점을 np.percentile로 구함. 
    quantile_25 = np.percentile(data.values, 25)  # 1/4 분위
    quantile_75 = np.percentile(data.values, 75)  # 3/4 분위
    # IQR을 구하고, IQR에 1.5를 곱하여 최대값과 최소값 지점 구함. 
    iqr = quantile_75 - quantile_25
    iqr_weight = iqr * weight
    lowest_val = quantile_25 - iqr_weight  # 이상치 최소 기준
    highest_val = quantile_75 + iqr_weight # 이상치 최대 기준
    # 최대값 보다 크거나, 최소값 보다 작은 값을 아웃라이어로 설정하고 DataFrame index 반환. 
    outlier_index[i] = data[(data < lowest_val) | (data > highest_val)].index

print ("OUTLIER END")

# 각각의 숫자들 리스트 안에 넣기
outlier_list = []
for i in range(len(outlier_index)):
    if list(outlier_index[i].values) == []:
        continue
    outlier_list.append(list(outlier_index[i].values))

# 리스트 안의 리스트들을 하나로 합치기
outlier_list = sum(outlier_list , [])
print('개수:', len(outlier_list))

# 중복 숫자 제거
outlier_list = set(outlier_list)
print('개수:', len(outlier_list))

# 다시 리스트 타입으로 변환
outlier_list = list(outlier_list)
print(type(outlier_list))

# 리스트 숫자 정렬
outlier_list.sort()

# outlier를 갖는 index에 해당하는 data drop
for i in outlier_list:
    raw_data.drop(i, axis=0, inplace=True)
raw_data.shape



X = raw_data.drop(columns=parameter)
Y = raw_data[parameter]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state = 765)


# minmax normalize
scaler = MinMaxScaler()
for colName in col_input:
    X_train[colName] = scaler.fit_transform(X_train[colName].values.reshape(-1, 1))
    X_test[colName] = scaler.fit_transform(X_test[colName].values.reshape(-1, 1))


model = LGBMRegressor(random_state=765)
model.fit(X_train,Y_train)

print(model)



# 교차 검증용 데이터셋 구성
df_trains = []
df_valids = []

# MAPE 정의
def def_MAPE(y_test, y_pred):
	return np.mean(np.abs((y_test - y_pred) / y_test)) * 100 

# MPE 정의
def def_MPE(y_test, y_pred): 
	return np.mean((y_test - y_pred) / y_test) * 100


from sklearn.model_selection import GridSearchCV

parameters = {
    "n_estimators" : [1000,3000,10000],
    'n_jobs' : [-1],
    'learning_rate': [0.05],
    'max_depth' : [-1,2,3,4,5,10,20,30,50],
    'num_leaves' : [31,60,80,100,127],
    }

kfold = KFold(n_splits=5, random_state=765, shuffle=True)

#cv=5 5번의 교차검증.
grid = GridSearchCV(LGBMRegressor(random_state=0), verbose=2, param_grid = parameters, cv=kfold)
grid.fit(X_train, Y_train)



print(grid.best_params_)












