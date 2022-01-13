from pycaret.regression import *
import numpy as np
import math
import matplotlib.pyplot as plt


from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error


def verify_model(model, data_seen, data_unseen, parameter) :

    data_unseen_input = data_unseen.drop(parameter,axis=1)
    data_unseen_result = model.predict(data_unseen_input)

    number2 = len(data_unseen)
    error_sum2 = sum(abs((data_unseen[parameter]-data_unseen_result)/data_unseen[parameter]))

    R2_data_unseen = r2_score(data_unseen[parameter],data_unseen_result)
    MAE_data_unseen = mean_absolute_error(data_unseen[parameter],data_unseen_result)
    MSE_data_unseen = mean_squared_error(data_unseen[parameter],data_unseen_result)
    RMSE_data_unseen = mean_squared_error(data_unseen[parameter],data_unseen_result, squared=False)
    MPE_data_unseen = error_sum2/number2 * 100 # unit : percent

    return np.array([R2_data_unseen, MAE_data_unseen, MSE_data_unseen, RMSE_data_unseen, MPE_data_unseen])




def verify_plot(model, data_seen, data_unseen, parameter, xlim=[0,20], ylim=[0,20], legend=True) :


    data_seen_input = data_seen.drop(parameter,axis=1)
    data_seen_result = model.predict(data_seen_input)
    data_unseen_input = data_unseen.drop(parameter,axis=1)
    data_unseen_result = model.predict(data_unseen_input)

    fts = 20

    plt.rc('xtick', labelsize=fts)
    plt.rc('ytick', labelsize=fts)

    plt.rc('font', size=40)
    plt.rcParams["figure.figsize"] = (21,10)
    if legend == 1 :
        plt.rcParams["figure.figsize"] = (20,10)

    plt.subplot(121)
    plt.scatter(data_seen[parameter], data_seen_result)
    plt.xlabel("y", fontsize=fts)
    plt.ylabel("ý", fontsize=fts)
    plt.grid(True)
    R2_data = r2_score(data_seen[parameter],data_seen_result)
    MAE_data = mean_absolute_error(data_seen[parameter],data_seen_result)
    MSE_data = mean_squared_error(data_seen[parameter],data_seen_result)
    RMSE_data = mean_squared_error(data_seen[parameter],data_seen_result, squared=False)

    number1 = len(data_seen)
    number2 = len(data_unseen)
    error_sum1 = sum(abs((data_seen[parameter]-data_seen_result)/data_seen[parameter]))
    error_sum2 = sum(abs((data_unseen[parameter]-data_unseen_result)/data_unseen[parameter]))

    error_avg1 = error_sum1/number1
    error_avg2 = error_sum2/number2

    if legend == True :
        plt.legend(["R² : " + str(round(R2_data,5)) + "\nMAE : " + str(round(MAE_data,5)) + "\nMSE : " 
        + str(round(MSE_data,5)) + "\nRMSE : " + str(round(RMSE_data,5))+ "\nMPE : " + str(round(error_avg1*100,2))+"%"],fontsize=20)
    plt.plot([xlim[0], xlim[1]], [ylim[0], ylim[1]], linestyle=':', linewidth=3, color='black')
    plt.xlim(xlim[0], xlim[1])
    plt.ylim(ylim[0], ylim[1])

    plt.subplot(122)
    plt.scatter(data_unseen[parameter], data_unseen_result)
    plt.xlabel("y", fontsize=fts)
    plt.ylabel("ý", fontsize=fts)
    plt.grid(True)
    R2_data_unseen = r2_score(data_unseen[parameter],data_unseen_result)
    MAE_data_unseen = mean_absolute_error(data_unseen[parameter],data_unseen_result)
    MSE_data_unseen = mean_squared_error(data_unseen[parameter],data_unseen_result)
    RMSE_data_unseen = mean_squared_error(data_unseen[parameter],data_unseen_result, squared=False)

    
    if legend == 1 :
        plt.legend(["R² : " + str(round(R2_data_unseen,5)) + "\nMAE : " + str(round(MAE_data_unseen,5)) + "\nMSE : " 
        + str(round(MSE_data_unseen,5)) + "\nRMSE : " + str(round(RMSE_data_unseen,5))+ "\nMPE : " + str(round(error_avg2*100,2))+"%"],fontsize=20)
    plt.plot([xlim[0], xlim[1]], [ylim[0], ylim[1]], linestyle=':', linewidth=3, color='black')
    plt.xlim(xlim[0], xlim[1])
    plt.ylim(ylim[0], ylim[1])

    plt.rc('font', size=40)

    


    return np.array([R2_data_unseen,MAE_data_unseen,MSE_data_unseen,RMSE_data_unseen,error_avg2*100])