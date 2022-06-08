from pycaret.regression import *

# see ref : https://pycaret.readthedocs.io/en/latest/api/regression.html

# - normalize method
# zscore : z = (x-u)
# minmax : 0 - 1
# maxabs
# robust

def regression_basic(dataset, parameter, algorithm="ligthgbm", frac_ratio=0.9, silent=True, save_en=False, save_model_name="model", new_feature_names=[], \
    normalize=False, normalize_method="zscore", remove_outliers=False, outliers_threshold=0.05, n_jobs=-1, use_gpu=False) :


    # split data for ML (train set / test set)
    data_seen = dataset.sample(frac=frac_ratio, random_state=765).reset_index(drop=True)
    data_unseen = dataset.drop(data_seen.index).reset_index(drop=True)

    features = ["width0","width1","height0","height1","move","coil0_width","coil1_width","gap0","gap1"] + new_feature_names

    # regresion setting
    exp_reg101 = setup(data = data_seen, target = parameter, session_id=123, silent=silent, remove_perfect_collinearity=False, \
    normalize=normalize, normalize_method=normalize_method, remove_outliers=remove_outliers, outliers_threshold=outliers_threshold, n_jobs=n_jobs, use_gpu=use_gpu, \
    numeric_features = features, \
    categorical_features = []) 


    # create model
    model = create_model(algorithm)


    # save model
    if save_en == True :
        save_model(model, save_model_name)

    return [model, data_seen, data_unseen]


# - search algorithm
# scikit-learn : random, grid
# scikit-optimize : bayesian
# tune-sklearn : random, grid, bayesian, hyperopt, optuna, bohb
# optuna : random, tpe

def tune_model(model, n_iter=10, optimize="R2", early_stopping=False, choose_better=False, verbose=False, search_algorithm=None, search_library="scikit-learn") :

    tuned_model = pycaret.regression.tune_model(model, n_iter=n_iter, optimize=optimize, early_stopping=early_stopping, choose_better=choose_better, verbose=verbose, \
        search_library=search_library, search_algorithm=search_algorithm)

    return tuned_model


def finalize_model(model) :

    finalized_model = pycaret.regression.finalize_model(model)

