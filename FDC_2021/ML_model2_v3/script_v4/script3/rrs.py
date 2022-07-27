import yaml
import os
import subprocess
import random
import csv
import time
import csv
import numpy as np
import math
import pandas
import shutil

#from pycaret.regression import load_model




REFERENCE_SCRIPT_FILE_NAME = f'C:\\script3\\run_ansys_ref.py'
    

def run_simul(version_idx_str):
    #0 Initialize random variables

    N1_range = [2,12]
    N2_range = [2,12]

    d1_list = [[8.1, 3000, 0.1],[6.9, 2000, 0.1],[6.0, 1500, 0.1],[5.1, 1300, 0.1],[4.9, 1150, 0.1],[4.7, 1000, 0.1],[3.6, 650, 0.1]]
    d2_list = [[8.1, 3000, 0.1],[6.9, 2000, 0.1],[6.0, 1500, 0.1],[5.1, 1300, 0.1],[4.9, 1150, 0.1],[4.7, 1000, 0.1],[3.6, 650, 0.1]]
    freq_range = [10,60]
    move_tx_range = [0,60]
    move_rx_range = [0,60]
    offset_tx_range = [-30,30]
    offset_rx_range = [-30,30]
    per_range = [2000,6000]
    space1_range = [0,150]
    space2_range = [0,500]
    space3_range = [0,150]
    space4_range = [0,500]
    l1_range = [8,50]
    l2_range = [50,100]
    h1_range = [100,200]
    w1_range = [20,200]

    N1 = random.randrange(N1_range[0], N1_range[1])
    N2 = random.randrange(N2_range[0], N2_range[1])
    
    d1_num = random.randrange(0,len(d1_list))
    d2_num = random.randrange(0,len(d2_list))

    d1 = d1_list[d1_num][0]
    d2 = d2_list[d2_num][0]
    d1_litz_num = d1_list[d1_num][1]
    d2_litz_num = d2_list[d2_num][1]
    d1_litz_dia = d1_list[d1_num][2]
    d2_litz_dia = d2_list[d2_num][2]

    freq = random.randrange(freq_range[0], freq_range[1])*1e+3
    move_tx = random.randrange(move_tx_range[0],move_tx_range[1]) * 1e-1
    move_rx = random.randrange(move_rx_range[0],move_rx_range[1]) * 1e-1
    offset_tx = random.randrange(offset_tx_range[0],offset_tx_range[1])
    offset_rx = random.randrange(offset_rx_range[0],offset_rx_range[1])
    per = random.randrange(per_range[0], per_range[1])
    space1 = random.randrange(space1_range[0], space1_range[1]) * 1e-1
    space2_min = math.ceil(space1+d1*1+d2/2+1)
    space2 = random.randrange(space2_min*1e+1, space2_range[1]) * 1e-1
    space3 = random.randrange(space3_range[0], space3_range[1]) * 1e-1
    space4_min = math.ceil(space3+d1*1+d2/2+1)
    space4 = random.randrange(space4_min*1e+1, space4_range[1]) * 1e-1
    l1 = random.randrange(l1_range[0], l1_range[1])
    l2_min = math.ceil(space2 + d2)
    l2 = random.randrange(l2_min, l2_range[1])
    h11 = math.ceil((N1+1)*move_tx + (N1+3)*d1) + abs(offset_tx)*2
    h12 = math.ceil((N2+1)*move_rx + (N2+3)*d2) + abs(offset_rx)*2
    maxh = max(h11,h12)
    h1 = random.randrange(maxh, h1_range[1])
    w1 = random.randrange(w1_range[0], w1_range[1])


    X2freq = random.randrange(freq_range[0], freq_range[1])*1e+3
    X2move_tx = random.randrange(move_tx_range[0],move_tx_range[1]) * 1e-1
    X2move_rx = random.randrange(move_rx_range[0],move_rx_range[1]) * 1e-1
    X2offset_tx = random.randrange(offset_tx_range[0],offset_tx_range[1])
    X2offset_rx = random.randrange(offset_rx_range[0],offset_rx_range[1])
    X2per = random.randrange(per_range[0], per_range[1])
    X2space1 = random.randrange(space1_range[0], space1_range[1]) * 1e-1
    X2space2_min = math.ceil(X2space1+d1*1+d2/2+1)
    X2space2 = random.randrange(X2space2_min*1e+1, space2_range[1]) * 1e-1
    X2space3 = random.randrange(space3_range[0], space3_range[1]) * 1e-1
    X2space4_min = math.ceil(X2space3+d1*1+d2/2+1)
    X2space4 = random.randrange(X2space4_min*1e+1, space4_range[1]) * 1e-1
    X2l1 = random.randrange(l1_range[0], l1_range[1])
    X2l2_min = math.ceil(X2space2 + d2)
    X2l2 = random.randrange(X2l2_min, l2_range[1])
    X2h11 = math.ceil((N1+1)*X2move_tx + (N1+3)*d1) + abs(X2offset_tx)*2
    X2h12 = math.ceil((N2+1)*X2move_rx + (N2+3)*d2) + abs(X2offset_rx)*2
    X2maxh = max(X2h11,X2h12)
    X2h1 = random.randrange(X2maxh, h1_range[1])
    X2w1 = random.randrange(w1_range[0], w1_range[1])


    X3freq = random.randrange(freq_range[0], freq_range[1])*1e+3
    X3move_tx = random.randrange(move_tx_range[0],move_tx_range[1]) * 1e-1
    X3move_rx = random.randrange(move_rx_range[0],move_rx_range[1]) * 1e-1
    X3offset_tx = random.randrange(offset_tx_range[0],offset_tx_range[1])
    X3offset_rx = random.randrange(offset_rx_range[0],offset_rx_range[1])
    X3per = random.randrange(per_range[0], per_range[1])
    X3space1 = random.randrange(space1_range[0], space1_range[1]) * 1e-1
    X3space2_min = math.ceil(X3space1+d1*1+d2/2+1)
    X3space2 = random.randrange(X3space2_min*1e+1, space2_range[1]) * 1e-1
    X3space3 = random.randrange(space3_range[0], space3_range[1]) * 1e-1
    X3space4_min = math.ceil(X3space3+d1*1+d2/2+1)
    X3space4 = random.randrange(X3space4_min*1e+1, space4_range[1]) * 1e-1
    X3l1 = random.randrange(l1_range[0], l1_range[1])
    X3l2_min = math.ceil(X3space2 + d2)
    X3l2 = random.randrange(X3l2_min, l2_range[1])
    X3h11 = math.ceil((N1+1)*X3move_tx + (N1+3)*d1) + abs(X3offset_tx)*2
    X3h12 = math.ceil((N2+1)*X3move_rx + (N2+3)*d2) + abs(X3offset_rx)*2
    X3maxh = max(X3h11,X3h12)
    X3h1 = random.randrange(X3maxh, h1_range[1])
    X3w1 = random.randrange(w1_range[0], w1_range[1])




    X4freq = random.randrange(freq_range[0], freq_range[1])*1e+3
    X4move_tx = random.randrange(move_tx_range[0],move_tx_range[1]) * 1e-1
    X4move_rx = random.randrange(move_rx_range[0],move_rx_range[1]) * 1e-1
    X4offset_tx = random.randrange(offset_tx_range[0],offset_tx_range[1])
    X4offset_rx = random.randrange(offset_rx_range[0],offset_rx_range[1])
    X4per = random.randrange(per_range[0], per_range[1])
    X4space1 = random.randrange(space1_range[0], space1_range[1]) * 1e-1
    X4space2_min = math.ceil(X4space1+d1*1+d2/2+1)
    X4space2 = random.randrange(X4space2_min*1e+1, space2_range[1]) * 1e-1
    X4space3 = random.randrange(space3_range[0], space3_range[1]) * 1e-1
    X4space4_min = math.ceil(X4space3+d1*1+d2/2+1)
    X4space4 = random.randrange(X4space4_min*1e+1, space4_range[1]) * 1e-1
    X4l1 = random.randrange(l1_range[0], l1_range[1])
    X4l2_min = math.ceil(X4space2 + d2)
    X4l2 = random.randrange(X4l2_min, l2_range[1])
    X4h11 = math.ceil((N1+1)*X4move_tx + (N1+3)*d1) + abs(X4offset_tx)*2
    X4h12 = math.ceil((N2+1)*X4move_rx + (N2+3)*d2) + abs(X4offset_rx)*2
    X4maxh = max(X4h11,X4h12)
    X4h1 = random.randrange(X4maxh, h1_range[1])
    X4w1 = random.randrange(w1_range[0], w1_range[1])

    str_tx = f'Tx_in,Tx_out,Tx1,'
    Tx_loop = ""
    for i in range(1,N1) :

        str_tx = str_tx + f'Tx{i+1},'

        Tx_loop = Tx_loop + "oEditor.Paste()\n"
        Tx_loop = Tx_loop + "oEditor.Move(\n"
        Tx_loop = Tx_loop + "   [\n"
        Tx_loop = Tx_loop + f'    "NAME:Selections",\n'
        Tx_loop = Tx_loop + f'    "Selections:="		, "Tx{i+1}",\n'
        Tx_loop = Tx_loop + f'    "NewPartsModelFlag:="	, "Model"\n'
        Tx_loop = Tx_loop + "   ],\n"
        Tx_loop = Tx_loop + "   [\n"
        Tx_loop = Tx_loop + f'    "NAME:TranslateParameters",\n'
        Tx_loop = Tx_loop + f'    "TranslateVectorX:="	, "0",\n'
        Tx_loop = Tx_loop + f'    "TranslateVectorY:="	, "0",\n'
        Tx_loop = Tx_loop + f'    "TranslateVectorZ:="	, "-{i}*move_tx+offset_tx"\n'
        Tx_loop = Tx_loop + "   ])\n"
    str_tx = str_tx[:-1]

    str_rx = f'Rx_in,Rx_out,Rx1,'
    Rx_loop = ""
    for i in range(1,N2) :

        str_rx = str_rx + f'Rx{i+1},'

        Rx_loop = Rx_loop + "oEditor.Paste()\n"
        Rx_loop = Rx_loop + "oEditor.Move(\n"
        Rx_loop = Rx_loop + "   [\n"
        Rx_loop = Rx_loop + f'    "NAME:Selections",\n'
        Rx_loop = Rx_loop + f'    "Selections:="		, "Rx{i+1}",\n'
        Rx_loop = Rx_loop + f'    "NewPartsModelFlag:="	, "Model"\n'
        Rx_loop = Rx_loop + "   ],\n"
        Rx_loop = Rx_loop + "   [\n"
        Rx_loop = Rx_loop + f'    "NAME:TranslateParameters",\n'
        Rx_loop = Rx_loop + f'    "TranslateVectorX:="	, "0",\n'
        Rx_loop = Rx_loop + f'    "TranslateVectorY:="	, "0",\n'
        Rx_loop = Rx_loop + f'    "TranslateVectorZ:="	, "-{i}*move_rx+offset_rx"\n'
        Rx_loop = Rx_loop + "   ])\n"
    str_rx = str_rx[:-1]


    #FIXME : add some variables

    #0.5 Config Identifier-Variable set.
    config = {
        "$VERSION_IDX_STR"  :   version_idx_str,
        "$N1"  :  N1,
        "$N2"  :  N2,
        "$d1"  :  d1,
        "$d2"  :  d2,
        "$litz_num_d1"  :  d1_litz_num,
        "$litz_num_d2"  :  d2_litz_num,
        "$litz_dia_d1"  :  d1_litz_dia,
        "$litz_dia_d2"  :  d2_litz_dia,
        "$freq" : freq,
        "$move_tx" : move_tx,
        "$move_rx" : move_rx,
        "$offset_tx" : offset_tx,
        "$offset_rx" : offset_rx,
        "$per" : per,
        "$space1" : space1,
        "$space2" : space2,
        "$space3" : space3,
        "$space4" : space4,
        "$l1" : l1,
        "$l2" : l2,
        "$h1" : h1,
        "$w1" : w1,
        "$X2freq" : X2freq,
        "$X2move_tx" : X2move_tx,
        "$X2move_rx" : X2move_rx,
        "$X2offset_tx" : X2offset_tx,
        "$X2offset_rx" : X2offset_rx,
        "$X2per" : X2per,
        "$X2space1" : X2space1,
        "$X2space2" : X2space2,
        "$X2space3" : X2space3,
        "$X2space4" : X2space4,
        "$X2l1" : X2l1,
        "$X2l2" : X2l2,
        "$X2h1" : X2h1,
        "$X2w1" : X2w1,
        "$X3freq" : X3freq,
        "$X3move_tx" : X3move_tx,
        "$X3move_rx" : X3move_rx,
        "$X3offset_tx" : X3offset_tx,
        "$X3offset_rx" : X3offset_rx,
        "$X3per" : X3per,
        "$X3space1" : X3space1,
        "$X3space2" : X3space2,
        "$X3space3" : X3space3,
        "$X3space4" : X3space4,
        "$X3l1" : X3l1,
        "$X3l2" : X3l2,
        "$X3h1" : X3h1,
        "$X3w1" : X3w1,
        "$X4freq" : X4freq,
        "$X4move_tx" : X4move_tx,
        "$X4move_rx" : X4move_rx,
        "$X4offset_tx" : X4offset_tx,
        "$X4offset_rx" : X4offset_rx,
        "$X4per" : X4per,
        "$X4space1" : X4space1,
        "$X4space2" : X4space2,
        "$X4space3" : X4space3,
        "$X4space4" : X4space4,
        "$X4l1" : X4l1,
        "$X4l2" : X4l2,
        "$X4h1" : X4h1,
        "$X4w1" : X4w1,
        "$Tx_loop" : Tx_loop,
        "$str_tx" : str_tx,
        "$Rx_loop" : Rx_loop,
        "$str_rx" : str_rx

        #FIXME : add some idt : variables
    }

    #1 Make Folder
    folder_name = f'SIMUL_{version_idx_str}'
    os.mkdir(f'C:\script3\ML\SIMUL_{version_idx_str}')

    #2 Make Variable info file
    with open(f'C:\script3\ML\SIMUL_{version_idx_str}\info.yaml', "w") as info_file:
        yaml.dump(config,info_file)

    #3 Make python script file
    #Load file string
    ref_script_str = ""
    with open(REFERENCE_SCRIPT_FILE_NAME) as f :
        lines = f.readlines()
    ref_script_str = "\n".join(lines);

    #Change Identifiers
    for idt, var in config.items() :
        ref_script_str = ref_script_str.replace(idt, str(var))

    #Save file
    with open(f'C:\\script3\\ML\\SIMUL_{version_idx_str}\\run_ansys_{version_idx_str}.py',"w") as f :
        f.write(ref_script_str)


    #4 make batch file.
    
    filepath2 = os.path.join('ML',folder_name,f'run_bat_{version_idx_str}.bat')
    with open(f'C:\\script3\\ML\\SIMUL_{version_idx_str}\\run_bat_{version_idx_str}.bat',"w") as f :
        f.write(f'"C:\\Program Files\\AnsysEM\\AnsysEM21.1\\Win64\\ansysedt.exe" -iconic -runscriptandexit "C:\\script3\\ML\\SIMUL_{version_idx_str}\\run_ansys_{version_idx_str}.py"')

    workingDir = f'C:\script3\ML\SIMUL_{version_idx_str}'
    executeFile = f'C:\script3\ML\SIMUL_{version_idx_str}\\run_bat_{version_idx_str}.bat'
    os.chdir(workingDir)
    os.system(executeFile)

    with open(f'C:\script3\ML_data\Data1 {version_idx_str}.csv',"r") as f :
        rdr = csv.reader(f)
        for line1_1 in rdr:
            a = 1
    with open(f'C:\script3\ML_data\Data2 {version_idx_str}.csv',"r") as f :
        rdr = csv.reader(f)
        for line2_1 in rdr:
            a = 1

    with open(f'C:\script3\ML_data\Data3 {version_idx_str}.csv',"r") as f :
        rdr = csv.reader(f)
        for line1_2 in rdr:
            a = 1
    with open(f'C:\script3\ML_data\Data4 {version_idx_str}.csv',"r") as f :
        rdr = csv.reader(f)
        for line2_2 in rdr:
            a = 1

    with open(f'C:\script3\ML_data\Data5 {version_idx_str}.csv',"r") as f :
        rdr = csv.reader(f)
        for line1_3 in rdr:
            a = 1
    with open(f'C:\script3\ML_data\Data6 {version_idx_str}.csv',"r") as f :
        rdr = csv.reader(f)
        for line2_3 in rdr:
            a = 1

    with open(f'C:\script3\ML_data\Data7 {version_idx_str}.csv',"r") as f :
        rdr = csv.reader(f)
        for line1_4 in rdr:
            a = 1
    with open(f'C:\script3\ML_data\Data8 {version_idx_str}.csv',"r") as f :
        rdr = csv.reader(f)
        for line2_4 in rdr:
            a = 1


    with open(f'C:\script3\ML_data\Data.csv',"a", encoding='utf-8', newline='') as f :

        tmp = np.concatenate((N1, N2, d1, d2, freq, move_tx, move_rx, offset_tx, offset_rx, per, space1, space2, space3, space4, l1, l2, h1, w1, line1_1[1], line1_1[2], line1_1[3], line1_1[4], line1_1[5], line1_1[6], line1_1[7], line1_1[8], line1_1[9], line1_1[10], line1_1[11], line1_1[12], line1_1[13], line1_1[14], line1_1[15], line2_1[2], line2_1[3]), axis=None)
        wr = csv.writer(f)
        wr.writerow(tmp)

        tmp = np.concatenate((N1, N2, d1, d2, X2freq, X2move_tx, X2move_rx, X2offset_tx, X2offset_rx, X2per, X2space1, X2space2, X2space3, X2space4, X2l1, X2l2, X2h1, X2w1, line1_2[1], line1_2[2], line1_2[3], line1_2[4], line1_2[5], line1_2[6], line1_2[7], line1_2[8], line1_2[9], line1_2[10], line1_2[11], line1_2[12], line1_2[13], line1_2[14], line1_2[15], line2_2[2], line2_2[3]), axis=None)
        wr = csv.writer(f)
        wr.writerow(tmp)

        tmp = np.concatenate((N1, N2, d1, d2, X3freq, X3move_tx, X3move_rx, X3offset_tx, X3offset_rx, X3per, X3space1, X3space2, X3space3, X3space4, X3l1, X3l2, X3h1, X3w1, line1_3[1], line1_3[2], line1_3[3], line1_3[4], line1_3[5], line1_3[6], line1_3[7], line1_3[8], line1_3[9], line1_3[10], line1_3[11], line1_3[12], line1_3[13], line1_3[14], line1_3[15], line2_3[2], line2_3[3]), axis=None)
        wr = csv.writer(f)
        wr.writerow(tmp)

        tmp = np.concatenate((N1, N2, d1, d2, X4freq, X4move_tx, X4move_rx, X4offset_tx, X4offset_rx, X4per, X4space1, X4space2, X4space3, X4space4, X4l1, X4l2, X4h1, X4w1, line1_4[1], line1_4[2], line1_4[3], line1_4[4], line1_4[5], line1_4[6], line1_4[7], line1_4[8], line1_4[9], line1_4[10], line1_4[11], line1_4[12], line1_4[13], line1_4[14], line1_4[15], line2_4[2], line2_4[3]), axis=None)
        wr = csv.writer(f)
        wr.writerow(tmp)



for i in range(1, 10000): 

    #run_simul(i)
    #print("end")


    try :
        try:
            os.remove(f'C:\script3\ML_aedt\ML3.aedt.lock')
        except:
            time.sleep(1)
        if os.path.isfile(f'C:\script3\ML_aedt\ML3.aedt') :
            os.remove(f'C:\script3\ML_aedt\ML3.aedt')
        time.sleep(1)	

        shutil.copy(f'C:\script3\ML_aedt\ML_ref.aedt',f'C:\script3\ML_aedt\ML3.aedt')
        time.sleep(1)

        run_simul(i)
        time.sleep(1)

        if os.path.isfile(f'C:\script3\ML_aedt\ML3.aedt') :
            os.remove(f'C:\script3\ML_aedt\ML3.aedt')
        time.sleep(1)	

        rmdir(f'C:\script3\ML_aedt\ML3.aedtresults')
        try:
            os.remove(f'C:\script3\ML_aedt\ML3.aedt.lock')
        except:
            time.sleep(1)
    except :
        time.sleep(1)	


    
    time.sleep(1)
