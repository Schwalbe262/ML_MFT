import pandas as pd
import numpy as np
import math



def drop_output(dataset, parameter) :

    # input parameter
    input_arrs = dataset[["N1","N2","d1","d2","freq","move_tx","move_rx","offset_tx","offset_rx","per","space1","space2","space3","space4","l1","l2","h1","w1"]] # 20

    # output parameter
    output_arrs = dataset[parameter]

    # merge
    processed_data = pd.concat([input_arrs, output_arrs],axis=1)


    return processed_data




def cut_data(dataset, parameter, lo=float('-inf'), hi=float('inf')) :

    dataset = dataset[dataset[parameter]>lo].reset_index(drop=True) # cut lower bound
    dataset = dataset[dataset[parameter]<hi].reset_index(drop=True) # cut upper bound


    return dataset




def add_feature(dataset, parameter, new_feature_names = []) :

    # input parameter
    input_arrs = dataset[["N1","N2","d1","d2","freq","move_tx","move_rx","offset_tx","offset_rx","per","space1","space2","space3","space4","l1","l2","h1","w1"]] # 18
    N1,N2,d1,d2,freq,move_tx,move_rx,offset_tx,offset_rx,per,space1,space2,space3,space4,l1,l2,h1,w1 = np.hsplit(input_arrs.to_numpy(),18)

    # output parameter
    output_arrs = dataset[parameter]

    if new_feature_names != [] :

        # featured parameter
        N1s = N1**2
        N2s = N2**2
        offset = abs(offset_tx-offset_rx)
        length1 = N1 * (l1*2 + space1*2 + w1 + space3*2)/2 + N1 * (l1*2 + space1*2 + w1 + space3*2)/2
        length4 = N2 * (l1*2 + space2*2 + w1 + space4*2)/2 + N2 * (l2*2 + space2*2 + w1 + space4*2)/2
        window1 = (l1 * 2 + space1 *2) * (w1 + space3 *2)
        window2 = (l1 * 2 + space2 *2) * (w1 + space4 *2)
        window_ratio = window2/window1
        from_l2 = (l2) - (space2)
        hw1 = N1*d1 + (N1-1)*move_tx
        hw2 = N2*d2 + (N2-1)*move_rx
        hw_diff = abs(hw1-hw2)+offset
        space12 = space2-d2/2-space1
        space34 = space4-d2/2-space3
        volume = (4*l1+2*l2)*(h1+2*l1)*w1 - 2*(l2*w1*h1)
        WL_iso1 = per*(l2+2*l1)*(N1**2*space12/hw1)
        WL_iso2 = per*(l2+2*l1)*(N1**2*space34/hw1)
        skin_depth = (1/3.14/freq/per)**0.5
        copper_skin_depth = (1.678*1e-2/3.14/0.999991/4/3.14/1e-7/freq)**0.5*1e-3
        skin_depth_ratio = d1*1e-3/copper_skin_depth
        d1s = d1**2
        d2s = d2**2
        ratio1 = (d1/2)**2 - ((d1/2)-skin_depth)**2 / (d1/2)**2
        ratio2 = (d2/2)**2 - ((d2/2)-skin_depth)**2 / (d2/2)**2


        per0 = 1 * 4 * 3.14 * 1e-7
        deq1 = (3.14/4)**0.5*d1*1e-3
        deq2 = (3.14/4)**0.5*d2*1e-3

        con = 1/1.678e-8
        eff1 = N1*deq1/h1
        eff2 = N2*deq2/h1

        sd = (1/3.14/per0/con/freq)**0.5
        sd1 = sd/eff1**0.5
        sd2 = sd/eff2**0.5

        delta1 = deq1 / sd1
        delta2 = deq2 / sd2

        m = 2

        sinh = np.vectorize(math.sinh)
        sin = np.vectorize(math.sin)
        cosh = np.vectorize(math.cosh)
        cos = np.vectorize(math.cos)

        G11 = (sinh(delta1)+cos(delta1))/(cosh(delta1)-cos(delta1))
        G12 = (sinh(delta1)-cos(delta1))/(cosh(delta1)+cos(delta1))
        Fr1 = delta1/2 * (G11 + (m**2-1)/3*G12)

        G21= (sinh(delta2)+cos(delta2))/(cosh(delta2)-cos(delta2))
        G22 = (sinh(delta2)-cos(delta2))/(cosh(delta2)+cos(delta2))
        Fr2 = delta2/2 * (G21 + (m**2-1)/3*G22)


        new_features_dict = {
            "N1s"       : N1s,
            "N2s"       : N2s,
            "offset"    : offset,
            "length1"   : length1,
            "length4"   : length4,
            "window1" : window1,
            "window2"  : window2,
            "window_ratio" : window_ratio,
            "from_l2"   : from_l2,
            "hw1" : hw1,
            "hw2" : hw2,
            "hw_diff" : hw_diff,
            "space12" : space12,
            "space34" : space34,
            "volume" : volume,
            "WL_iso1" : WL_iso1,
            "WL_iso2" : WL_iso2,
            "skin_depth" : skin_depth,
            "copper_skin_depth" : copper_skin_depth,
            "skin_depth_ratio" : skin_depth_ratio,
            "d1s" : d1s,
            "d2s" : d2s,
            "eff1" : eff1,
            "eff2" : eff2,
            "G11" : G11,
            "G12" : G12,
            "G21" : G21,
            "G22" : G22,
            "Fr1" : Fr1,
            "Fr2" : Fr2,
            "sd1" : sd1,
            "sd2" : sd2,
            "ratio1" : ratio1,
            "ratio2" : ratio2,
            "delta1" : delta1,
            "delta2" : delta2,
            "Fr1" : delta1/2 * (G11+G12),
            "Fr2" : delta2/2 * (G21+G22)
        }
        #filter by 'new_features'
        new_features_arr = [v for (k,v) in new_features_dict.items() if k in new_feature_names]
        new_features_arr = pd.DataFrame(np.array(new_features_arr).squeeze().transpose(), columns = new_feature_names)


        # Merge
        processed_data = pd.concat([input_arrs, output_arrs, new_features_arr],axis=1)

    else : 
        
        # Merge
        processed_data = pd.concat([input_arrs, output_arrs],axis=1)

    return processed_data