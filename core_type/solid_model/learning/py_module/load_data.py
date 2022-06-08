import pandas as pd
import numpy as np

def load_data(fn, pp=None, size_en=False, size=100000):

    csv = pd.read_csv(fn)
    csv = csv.dropna(axis=0).reset_index(drop=True) #drop NaN

    if pp == 1 : # post process (option : elemenate outlier data)

        csv = csv[csv['Lmt']>0.1].reset_index(drop=True)
        csv = csv[csv['Lmr']>0.1].reset_index(drop=True)
        csv['k'] = -csv['k']
        csv = csv[csv['k']>0].reset_index(drop=True)

    if size_en == True :
        csv = csv.sample(n=size).reset_index(drop=True)

    #calculate R
    array_len = len(csv)
    R1 = np.zeros(array_len)
    R2 = np.zeros(array_len)
    R1 = csv["copperloss_tx"]/100**2
    R2 = csv["copperloss_rx"]/100**2

    csv = csv.assign(R1 = R1)
    csv = csv.assign(R2 = R2)

    return csv 