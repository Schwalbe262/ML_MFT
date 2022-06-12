import yaml
import os
import subprocess
import random
import csv
import time
import csv
import numpy as np
import math
import pandas as pd
import shutil

#from pycaret.regression import load_model


																																																

REFERENCE_SCRIPT_FILE_NAME = f'run_ansys_ref.py'
f = open("../computer_name.txt", 'r')
COMPUTER_NAME = f.readline()

def random_choice(X) :
    return round(np.random.choice( np.arange( X[0] , X[1]+X[2] , X[2]) ),X[3])
    
def run_simul(version_idx_str):
    #0 Initialize random variables

    N1_range = [2, 15, 1, 0]

    w1_range = [20, 200, 1, 0] # under, upper, resolution
    l1_range = [10, 50, 1, 0]
    l2_range = [40, 100, 1, 0]
    h1_range = [50, 130, 1, 0]

    per_range = [1000,10000,100,0]

    space1_range = [4, 50, 1, 0] 
    space2_range = [4, 50, 1, 0] 
    space3_range = [4, 50, 1, 0] 
    space4_range = [4, 50, 1, 0] 

    coil_width1_range = [2, 10, 0.5, 1] 
    coil_width2_range = [2, 10, 0.5, 1] 

    move_z1_range = [0.5,5,0.5,1]
    move_z2_range = [0.5,5,0.5,1]

    offset_z1_range = [-20,20,0.5,1]
    offset_z2_range = [-20,20,0.5,1]


    # Design 1

    N1 = random_choice(N1_range)

    offset_z1 = random_choice(offset_z1_range)
    offset_z2 = random_choice(offset_z2_range)

    move_z1 = random_choice(move_z1_range)
    move_z2 = random_choice(move_z2_range)

    coil_width1 = random_choice(coil_width1_range)
    coil_width2 = random_choice(coil_width2_range)

    per = random_choice(per_range)

    space1 = random_choice(space1_range)
    space2 = random_choice(space2_range)
    space3 = random_choice(space3_range)
    space4 = random_choice(space4_range)

    w1 = random_choice(w1_range)
    l1 = random_choice(l1_range)

    height = max(N1*coil_width1 + (N1-1)*move_z1 + 2*abs(offset_z1), N1*coil_width2 + (N1-1)*move_z2 + 2*abs(offset_z2))
    length = coil_width1 + coil_width2 + space2 + space4

    if length>l2_range[0] and length<l2_range[1] :
        l2_range = [length+5,l2_range[1],l2_range[2],l2_range[3]]
    elif length>l2_range[0] and length>l2_range[1] :
        l2_range = [length+5,length*1.2,l2_range[2],l2_range[3]]

    #print(l2_range)
    
    l2 = random_choice(l2_range)


    if height>h1_range[0] and height<h1_range[1] :
        h1_range = [height+5,h1_range[1],h1_range[2],h1_range[3]]
    if height>h1_range[0] and height>h1_range[1] :
        h1_range = [height+5,height*1.2,h1_range[2],h1_range[3]]
    
    h1 = random_choice(h1_range)


    airx = 5.0 * (w1 + 2*(max(2*space1+coil_width1,2*space3+coil_width2)))
    airy = 5.0 * (l2 + 2*l1 + 2*(max(space2+coil_width1,space4+coil_width2)))
    airz = 5.0 * (h1 + 2*l1)



    #FIXME : add some variables


    #0.5 Config Identifier-Variable set.
    config = {
        "$VERSION_IDX_STR"  :   version_idx_str,
        "$air_x"  :  airx,
        "$air_y"  :  airy,
        "$air_z"  :  airz,
        "$N1"  :  N1,
        "$w1"  :  w1,
        "$l1"  :  l1,
        "$l2"  :  l2,
        "$h1"  :  h1,
        "$per" : per,
        "$space1"  :  space1,
        "$space2"  :  space2,
        "$space3"  :  space3,
        "$space4"  :  space4,
        "$coil_width1"  :  coil_width1,
        "$coil_width2"  :  coil_width2,
        "$move_z1"  :  move_z1,
        "$move_z2"  :  move_z2,
        "$offset_z1"  :  offset_z1,
        "$offset_z2"  :  offset_z2,
        #FIXME : add some idt : variables
    }


    #1 Make Folder
    folder_name = f'SIMUL_{version_idx_str}'
    os.mkdir(f'.\ML\SIMUL_{version_idx_str}')


    #2 Make Variable info file
    with open(f'.\ML\SIMUL_{version_idx_str}\info.yaml', "w") as info_file:
        yaml.dump(config,info_file)


    #3 Make python script file
    #Load file string
    ref_script_str = ""
    with open(REFERENCE_SCRIPT_FILE_NAME) as f :
        lines = f.readlines()
    ref_script_str = "\n".join(lines)

    #Change Identifiers
    for idt, var in config.items() :
        ref_script_str = ref_script_str.replace(idt, str(var))

    #Save file
    with open(f'.\\ML\\SIMUL_{version_idx_str}\\run_ansys_{version_idx_str}.py',"w") as f :
        f.write(ref_script_str)


    #4 make batch file.
    filepath2 = os.path.join('ML',folder_name,f'run_bat_{version_idx_str}.bat')
    with open(f'.\\ML\\SIMUL_{version_idx_str}\\run_bat_{version_idx_str}.bat',"w") as f :
        f.write(f'"C:\\Program Files\\AnsysEM\\AnsysEM21.1\\Win64\\ansysedt.exe" -iconic -runscriptandexit ".\\ML\SIMUL_{version_idx_str}\\run_ansys_{version_idx_str}.py"')


    workingDir = f'.\\ML\\SIMUL_{version_idx_str}'
    executeFile = f'.\\ML\\SIMUL_{version_idx_str}\\run_bat_{version_idx_str}.bat'
    #os.chdir(workingDir)
    try :
        os.system(executeFile)
    except :
        time.sleep(1)


    temp1 = pd.read_csv(f'.\ML_data\magnetizing_inductance{version_idx_str}.csv', sep=",")
    if temp1.columns[1] == "Matrix1.CplCoef(Tx,Rx)^2 * Matrix1.L(Tx,Tx) [mH]" :
        temp1[:,1] = temp1[:,1]*1000
        temp1[:,2] = temp1[:,2]*1000
        temp1 = temp1.to_numpy()
    else :
        temp1 = temp1.to_numpy()
    
    temp2 = pd.read_csv(f'.\ML_data\leakage_inductance{version_idx_str}.csv', sep=",")
    if temp2.columns[1] == "(1-Matrix1.CplCoef(Tx,Rx)^2) * Matrix1.L(Tx,Tx) [nH]]" :
        temp2[:,1] = temp2[:,1]/1000
        temp2[:,2] = temp2[:,2]/1000
        temp2 = temp2.to_numpy()
    else :
        temp2 = temp2.to_numpy()

    temp3 = pd.read_csv(f'.\ML_data\loss{version_idx_str}.csv', sep=",")
    temp3 = temp3.to_numpy()

    parameter = np.array([N1,w1,l1,l2,h1,per,space1,space2,space3,space4,coil_width1,coil_width2,move_z1,move_z2,offset_z1,offset_z2])

    temp1 = np.append(parameter,temp1)
    temp2 = np.append(parameter,temp2)
    temp3 = np.append(parameter,temp3)


    print(temp1)
    print(temp2)
    print(temp3)


    data1 = np.loadtxt(f'Z:\Autosimul_data\MFT\core_type_solid2\{COMPUTER_NAME}\script28\magnetizing_inductance.csv', delimiter=",")
    new_data1 = np.vstack((data1, temp1))
    np.savetxt(f'Z:\Autosimul_data\MFT\core_type_solid2\{COMPUTER_NAME}\script28\magnetizing_inductance.csv',new_data1,delimiter=",")

    data2 = np.loadtxt(f'Z:\Autosimul_data\MFT\core_type_solid2\{COMPUTER_NAME}\script28\leakage_inductance.csv', delimiter=",")
    new_data2 = np.vstack((data2, temp2))
    np.savetxt(f'Z:\Autosimul_data\MFT\core_type_solid2\{COMPUTER_NAME}\script28\leakage_inductance.csv',new_data2,delimiter=",")

    data3 = np.loadtxt(f'Z:\Autosimul_data\MFT\core_type_solid2\{COMPUTER_NAME}\script28\loss.csv', delimiter=",")
    new_data3 = np.vstack((data3, temp3))
    np.savetxt(f'Z:\Autosimul_data\MFT\core_type_solid2\{COMPUTER_NAME}\script28\loss.csv',new_data3,delimiter=",")



for i in range(0, 10000): 

    #run_simul(i)
    #print("end")


    try :
        try:
            os.remove(f'.\ML_aedt\ML28.aedt.lock')
        except:
            time.sleep(1)
        if os.path.isfile(f'.\ML_aedt\ML28.aedt') :
            os.remove(f'.\ML_aedt\ML28.aedt')
        time.sleep(1)	

        shutil.copy(f'.\ML_aedt\ML_ref.aedt',f'.\ML_aedt\ML28.aedt')
        time.sleep(1)

        try:
            run_simul(i)
        except Exception as e: 
            print(f'error number {i}')
            print(e)

        if os.path.isfile(f'.\ML_aedt\ML28.aedt') :
            os.remove(f'.\ML_aedt\ML28.aedt')
        time.sleep(1)	

        shutil.rmtree(f'.\ML_aedt\ML28.aedtresults')
        try:
            os.remove(f'.\ML_aedt\ML28.aedt.lock')
        except:
            time.sleep(1)
    except :
        time.sleep(1)	


    
    time.sleep(1)


os.system("pause")
