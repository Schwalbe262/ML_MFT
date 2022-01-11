from pycaret.regression import *
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