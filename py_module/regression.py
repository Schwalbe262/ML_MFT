from pycaret.regression import *

def regression_basic(dataset, parameter, frac_ratio=0.9, silent=True, save_en=False, save_model_name="model") :


    # split data for ML (train set / test set)
    data_seen = dataset.sample(frac=frac_ratio, random_state=765).reset_index(drop=True)
    data_unseen = dataset.drop(data_seen.index).reset_index(drop=True)

    # regresion setting
    exp_reg101 = setup(data = data_seen, target = parameter, session_id=123, silent=silent, use_gpu=False, remove_perfect_collinearity=False) 


    # create model
    #lgbm = create_model('lightgbm',num_leaves=60, max_depth=20)
    model = create_model('lightgbm')


    # save model
    if save_en == True :
        save_model(model, save_model_name)

    return [model, data_seen, data_unseen]


def test() :
    
    return 1