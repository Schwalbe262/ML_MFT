#import module (library)

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from pycaret.regression import *
import time
from datetime import datetime

import os

# import module (user defined function)

from py_module.load_data import load_data
from py_module.plot_data import plot_histogram
from py_module.regression import *
from py_module.pre_processing import *
from py_module.verify import *





# === import raw_data (from csv file) ===

filename = os.path.abspath("")+"../Data_2021_10_14_v1 (N98923)/Data.csv" # csv file directory and name

print(filename)

raw_data = load_data(fn=filename, pp=1)

"""


## === dataset pre-processing ===

# drop output data except for target output

parameter = "Llt" # target output pamareter
processed_data = drop_output(raw_data, parameter)



# cut data
## - opt
# lo : lower bound value (default : -inf)
# hi : upper bound value (default : inf)

processed_data = cut_data(processed_data, parameter="Llt", lo=0.1, hi=40)



# add feature
# 기존에 존재하는 input parameter들을 이용해서 물리적인 의미를 갖는 새로운 파라미터를 만들어 낼 시 모델의 성능을 증가시킬 수 있음
# ex> 변압기 자화 인덕턴스는 턴수의 제곱에 비례하므로 턴수의 제곱에 해당하는 파라미터를 새로 만들어 자화인덕터 regression 모델을 만들 경우 모델 성능 증가

new_feature_names = []

processed_data = add_feature(processed_data, parameter, new_feature_names = new_feature_names)

processed_data





# === compare algorithm ===
# 여러 regression 알고리즘 중 가장 높은 성능을 내는 알고리즘 탐색 (모든 알고리즘 탐색)

start_time_t = time.time()

# activate logger
[model, data_seen, data_unseen] = regression_basic(processed_data, parameter, algorithm="lightgbm", frac_ratio=0.9, save_en=False, save_model_name="model", new_feature_names=new_feature_names)


# variable
algorithm_list = models().index
except_list = [] # algorithm list to exclude from train
result = []


# eleminate algorithm in exception list
for al_name in except_list :

    algorithm_list = algorithm_list[algorithm_list!=al_name]

    
# train each algorithm
for al_name in algorithm_list :

    start_time = time.time()

    [model, data_seen, data_unseen] = regression_basic(processed_data, parameter, algorithm=al_name, new_feature_names=new_feature_names)
    [R2, MAE, MSE, RMSE, MPE] = verify_model(model, data_seen, data_unseen, parameter)

    end_time= time.time()
    timetime = end_time - start_time

    result.append([al_name, R2, MAE, MSE, RMSE, MPE, timetime])

end_time_t = time.time()
timetime_t = end_time_t - start_time_t
print(f'total time : {timetime_t}')


# compare model result
pd.DataFrame(result,columns = ["algorithm","R2","MAE","MSE","RMSE","MPE(%)","time(s)"]).sort_values(by='R2' ,ascending=False).reset_index(drop=True)



"""




