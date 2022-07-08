from pycaret.regression import *
import time
import pandas as pd

import os
import sys

from .regression import *
from .compare import *
from .verify import *
from .etc import *


# compare algorithm (tuned case)
# 여러 regression 알고리즘 중 가장 높은 성능을 내는 알고리즘 탐색 (모든 알고리즘 탐색)
# 각각의 algorithm은 auto tune을 이용하여 튜닝


def compare_algorithm(parameter=None, data=None, algorithm_list=[], low_list=[], new_feature_names=[], tune_en=False, n_h=100, n_l=50, optimize="MAE", search_library="scikit-learn", search_algorithm="random"):

    result = []
    error_list = []

    # activate logger
    [model, data_seen, data_unseen] = regression_basic(data, parameter, algorithm="lightgbm", frac_ratio=0.9, save_en=False, save_model_name="model", new_feature_names=new_feature_names)

    
    # train each algorithm
    for al_name in algorithm_list :

        start_time = time.time()

        [model, data_seen, data_unseen] = regression_basic(data, parameter, algorithm=al_name, new_feature_names=new_feature_names)

        # tuning

        if tune_en == True :
        
            try :
                if find_element(low_list,[al_name]) == False :
                    tuned_model = tune_model(model, n_iter=n_h, optimize=optimize, early_stopping=False, choose_better=True, verbose=True, search_library=search_library, search_algorithm=search_algorithm)
                elif find_element(low_list,[al_name]) == True :
                    tuned_model = tune_model(model, n_iter=n_l, optimize=optimize, early_stopping=False, choose_better=True, verbose=False, search_library=search_library, search_algorithm=search_algorithm)
            except :
                error_list.append([al_name])

            [R2, MAE, MSE, RMSE, MPE] = verify_model(tuned_model, data_seen, data_unseen, parameter)
            save_model(tuned_model, f'./model_temp/{al_name}')

        elif tune_en == False :

            [R2, MAE, MSE, RMSE, MPE] = verify_model(model, data_seen, data_unseen, parameter)
            save_model(model, f'./model_temp/{al_name}')

        end_time= time.time()
        timetime = end_time - start_time

        result.append([al_name, R2, MAE, MSE, RMSE, MPE, timetime])


    # compare model result
    result = pd.DataFrame(result,columns = ["algorithm","R2","MAE","MSE","RMSE","MPE(%)","time(s)"]).sort_values(by='R2' ,ascending=False).reset_index(drop=True)

    return result
