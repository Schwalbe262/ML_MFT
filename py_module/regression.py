from pycaret.regression import *

def regression_basic(dataset, parameter, algorithm="ligthgbm", frac_ratio=0.9, silent=True, save_en=False, save_model_name="model", new_feature_names=[]) :


    # split data for ML (train set / test set)
    data_seen = dataset.sample(frac=frac_ratio, random_state=765).reset_index(drop=True)
    data_unseen = dataset.drop(data_seen.index).reset_index(drop=True)

    features = ["N1", "N2", "d1" , "d2", "freq", "move_tx", "move_rx", "offset_tx", "offset_rx", "per", "space1", "space2", "space3", "space4", "l1", "l2", "h1", "w1"] + new_feature_names

    # regresion setting
    exp_reg101 = setup(data = data_seen, target = parameter, session_id=123, silent=silent, use_gpu=False, remove_perfect_collinearity=False, \
    numeric_features = features, \
    categorical_features = []) 


    # create model
    model = create_model(algorithm)


    # save model
    if save_en == True :
        save_model(model, save_model_name)

    return [model, data_seen, data_unseen]


def test() :
    
    return 1