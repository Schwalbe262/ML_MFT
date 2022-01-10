import pandas as pd
import numpy as np



def drop_output(dataset, parameter) :

    # input parameter
    input_arrs = dataset[["N1","N2","d1","d2","freq","move_tx","move_rx","offset_tx","offset_rx","per","space1","space2","space3","space4","l1","l2","h1","w1"]] # 20

    # output parameter
    output_arrs = dataset[parameter]

    # merge
    processed_data = pd.concat([input_arrs, output_arrs],axis=1)


    return processed_data




