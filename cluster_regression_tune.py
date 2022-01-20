#import module (library)

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from pycaret.regression import *
import time
from datetime import datetime

import os
import argparse

# import module (user defined function)

from py_module.load_data import load_data
from py_module.plot_data import plot_histogram
from py_module.regression import *
from py_module.pre_processing import *
from py_module.verify import *


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-al', '--algorithm', type=str, nargs='+', metavar='N', help='algorithm name')
parser.add_argument('-n', '--n_iter', type=int, nargs='+', metavar='N', help='tuning iteration')

args = parser.parse_args()



start_time_e = time.time() # total execution time





# === import raw_data (from csv file) ===

filename = os.path.abspath("")+"/../Data_2021_10_14_v1 (N98923)/Data.csv" # csv file directory and name

#print(filename)

raw_data = load_data(fn=filename, pp=1)

print(f'raw_data size : {raw_data.shape}')
print("\n======== raw_data ========\n")
print(raw_data)
print("\n======== raw_data ========\n")




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

print(f'processed_data size : {processed_data.shape}')
print("\n======== processed_data ========\n")
print(processed_data)
print("\n======== processed_data ========\n")





# === regression ===
# 여러 regression 알고리즘 중 가장 높은 성능을 내는 알고리즘 탐색 (모든 알고리즘 탐색)

result = []

start_time_t = time.time()
start_time = time.time()

[model, data_seen, data_unseen] = regression_basic(processed_data, parameter, algorithm=args.algorithm, new_feature_names=new_feature_names)
[R2, MAE, MSE, RMSE, MPE] = verify_model(model, data_seen, data_unseen, parameter)

end_time= time.time()
timetime = end_time - start_time

result.append([args.algorithm, R2, MAE, MSE, RMSE, MPE, timetime])

end_time_t = time.time()
timetime_t = end_time_t - start_time_t
print(f'regression total time : {timetime_t}')


# compare model result
result = pd.DataFrame(result,columns = ["algorithm","R2","MAE","MSE","RMSE","MPE(%)","time(s)"]).sort_values(by='R2' ,ascending=False).reset_index(drop=True)

print(result)



# === tune ===

result = []

start_time_t = time.time()

tuned_model = tune_model(model, n_iter=args.n_iter, optimize="MAE")
[R2, MAE, MSE, RMSE, MPE] = verify_model(tuned_model, data_seen, data_unseen, parameter)
end_time= time.time()
timetime = end_time - start_time
result.append([args.algorithm, R2, MAE, MSE, RMSE, MPE, timetime])


end_time_t = time.time()
timetime_t = end_time_t - start_time_t
print(f'algorithm tuning total time : {timetime_t}')
    
# compare model result
tune_result = pd.DataFrame(result,columns = ["algorithm","R2","MAE","MSE","RMSE","MPE(%)","time(s)"]).sort_values(by='R2' ,ascending=False).reset_index(drop=True)

print(tune_result)




end_time_e = time.time() # total execution time
timetime_e = end_time_e - start_time_e
print(f'total time : {timetime_e}')

"""

"""


print("\n\n\n\n\n")
print("Summary")
print("\n\n")
print(f'algorithm : {args.algorithm}')
print(f'iteration : {args.n_iter}')
print("\n\n")
print(f'algorithm retression total time : {timetime_t}')
print(result)
print("\n\n")
print(f'algorithm tuning total time : {timetime_t}')
print(tune_result)
print("\n\n")
print(f'total time : {timetime_e}')









