# 1. import module

import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
from datetime import datetime

from pycaret.regression import *

from sklearn.model_selection import train_test_split 
from sklearn import metrics
from lightgbm import LGBMRegressor
from sklearn.model_selection import KFold

from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error 


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.options.display.max_seq_items = None

import os
import argparse




parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-rn', '--result_name', type=str, nargs='+', metavar='N', help='rseult_file name')
parser.add_argument('-ln', '--log_name', type=str, nargs='+', metavar='N', help='log_file name')

args = parser.parse_args()

args.rn = args.result_name[0]
args.ln = args.log_name[0]

f = open(args.ln, 'w')
f.write(f'START : {datetime.now()}')
f.close()

# 2. data import

filename = os.path.abspath("")+"/../Data_2021_10_14_v1 (N98923)/Data.csv" # csv file directory and name

raw_data = pd.read_csv(filename)


# 학습할 파라미터를 제외한 나머지 아웃풋 삭제
output = ["Lmt","Lmr","Llt","Llr","k","Lt","Lr","Lm","Rt","Rr","I1","I2","Zt","Zr","Zm","copperloss_tx","copperloss_rx"]
parameter = "Llt"
output.remove(parameter)

for pam in output :
    raw_data = raw_data.drop(columns=pam)

# NaN 데이터 삭제
raw_data = raw_data.dropna()


# 3. define outlier search function
def get_outlier(df=None, column=None, weight=1.5):
    
    # column 데이터만 추출, 1/4 분위와 3/4 분위 지점을 np.percentile로 구함. 
    data = df[column]
    quantile_25 = np.percentile(data.values, 25)  # 1/4 분위
    quantile_75 = np.percentile(data.values, 75)  # 3/4 분위
    
    # IQR을 구하고, IQR에 1.5를 곱하여 최대값과 최소값 지점 구함. 
    iqr = quantile_75 - quantile_25
    iqr_weight = iqr * weight
    lowest_val = quantile_25 - iqr_weight  # 이상치 최소 기준
    highest_val = quantile_75 + iqr_weight # 이상치 최대 기준
    
    # 최대값 보다 크거나, 최소값 보다 작은 값을 아웃라이어로 설정하고 DataFrame index 반환. 
    outlier_index = data[(data < lowest_val) | (data > highest_val)].index
    
    return outlier_index



# 4. data pre-processing

# target 변수 제외
col_input = list(raw_data.columns)[:-1]
print(col_input)

# outlier 탐색 및 제거
outlier_index = {}
for i, colName in enumerate(col_input):
     outlier_index[i] = get_outlier(df=raw_data, column=f'{colName}', weight=1.5)
outlier_index

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



# 5. split input/output

X = raw_data.drop(columns=parameter)
Y = raw_data[parameter]

#raw_data.to_csv("raw_data.csv", mode='w')

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state = 765)


# minmax normalize
scaler = MinMaxScaler()
for colName in col_input:
    X_train[colName] = scaler.fit_transform(X_train[colName].values.reshape(-1, 1))
    X_test[colName] = scaler.fit_transform(X_test[colName].values.reshape(-1, 1))




import time

# 교차 검증용 데이터셋 구성
df_trains = []
df_valids = []

# MAPE 정의
def def_MAPE(y_test, y_pred):
	return np.mean(np.abs((y_test - y_pred) / y_test)) * 100 

# MPE 정의
def def_MPE(y_test, y_pred): 
	return np.mean((y_test - y_pred) / y_test) * 100

# KFold 검증
kfold = KFold(n_splits=5, random_state=765, shuffle=True)



result = pd.DataFrame([],columns=["n_estimators","learning_rate","max_depth","num_leaves","R2","MAE","MSE","RMSE","MAPE","MPE"])


hyper_parameters = {
    'n_jobs' : -1
    }

for n_estimators in [10,30,100,300,1000,3000,10000] :
    for max_depth in [-1,1,2,3,4,5,10,20,30,50] :    
        for num_leaves in [31,60,80,100,127] :
            for learning_rate in [0.001,0.01,0.05,0.1] :
                f = open(args.ln, 'w')
                f.write(f'n_est/max_d/num_leaves/learning_rate : {n_estimators}/{max_depth}/{num_leaves}/{learning_rate} : {datetime.now()}')
                f.close()
                model = LGBMRegressor(random_state=765, n_estimators=n_estimators, max_depth=max_depth, num_leaves=num_leaves, learning_rate=learning_rate, **hyper_parameters)
                model.fit(X_train,Y_train)

                

                R2 = []
                MAE = []
                MSE = []
                RMSE = []
                MAPE = []
                MPE = []

        
            
                for train_idx, test_idx in kfold.split(X[col_input]):

                    start_t = time.time()

                    # fold 후 train, test set 분할
                    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
                    Y_train, Y_test = Y.iloc[train_idx], Y.iloc[test_idx]

                    # regression model 생성
                    start = time.time()
                    model.fit(X_train, Y_train)
                    end = time.time()
                    #print(f'model time : {end-start}')

                    # 예측
                
                    start = time.time()
                    fold_pred = model.predict(X_test)
                    end = time.time()
                    #print(f'predict time : {end-start}')
                    

                    # 성능계산
                    start = time.time()
                    R2.append(r2_score(Y_test, fold_pred))
                    end = time.time()
                    #print(f'R2 time : {end-start}')
                    MAE.append(mean_absolute_error(Y_test, fold_pred))
                    MSE.append(mean_squared_error(Y_test, fold_pred))
                    RMSE.append(np.sqrt(mean_squared_error(Y_test, fold_pred)))
                    MAPE.append(def_MAPE(Y_test, fold_pred))
                    MPE.append(def_MPE(Y_test, fold_pred))
                    
                    end_t = time.time()
                    #print(f'loop time : {end_t-start_t}')

                temp = {"n_estimators":n_estimators,"learning_rate":learning_rate,"max_depth":max_depth,"num_leaves":num_leaves,"R2":np.mean(R2),"MAE":np.mean(MAE),"MSE":np.mean(MSE),"RMSE":np.mean(RMSE),"MAPE":np.mean(MAPE),"MPE":np.mean(MPE)}
                result = result.append(temp, ignore_index=True)

result.to_csv(args.rn, mode="w")



