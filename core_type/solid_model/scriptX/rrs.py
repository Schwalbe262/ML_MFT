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

def random_choice(X) :
    return round(np.random.choice( np.arange( X[0] , X[1]+X[2] , X[2]) ),X[3])
    
def run_simul(version_idx_str):
    #0 Initialize random variables

    move_range = [0.05, 0.4, 0.025, 3] # under, upper, resolution, 소수점자리수
    width0_range = [400, 1000, 25, 0]
    width1_range = [250, 1000, 25, 0]

    height0_range = [2500, 8000, 100, 0]
    height1_range = [1000, 3500, 100, 0]

    gap0_range = [25, 150, 5, 0]
    gap1_range = [25, 50, 5 ,0]

    coil0_width_range = [20, 20, 1 ,0]
    coil1_width_range = [20, 20, 1 ,0]


    # Design 1

    move = random_choice(move_range) 
    width0 = random_choice(width0_range) 
    width1_range = [250, width0/2, 25, 0]
    width1 = random_choice(width1_range) 

    height0 = random_choice(height0_range) 
    height1_range = [1000, height0/2, 100, 0]
    height1 = random_choice(height1_range) 

    coil0_width = random_choice(coil0_width_range) 
    coil1_width = random_choice(coil1_width_range) 

    gap0 = random_choice(gap0_range) 
    gap1 = random_choice(gap1_range) 
    

    


    #FIXME : add some variables


    #0.5 Config Identifier-Variable set.
    config = {
        "$VERSION_IDX_STR"  :   version_idx_str,
        "$move"  :  move,
        "$width0"  :  width0,
        "$width1"  :  width1,
        "$height0"  :  height0,
        "$height1"  :  height1,
        "$gap0"  :  gap0,
        "$gap1"  :  gap1,
        "$coil0_width"  :  coil0_width,
        "$coil1_width"  :  coil1_width
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


    temp1 = pd.read_csv(f'.\ML_data\inductance{version_idx_str}.csv', sep=",")
    temp1 = temp1.to_numpy()
    temp2 = pd.read_csv(f'.\ML_data\coupling{version_idx_str}.csv', sep=",")
    temp2 = temp2.to_numpy()
    temp3 = pd.read_csv(f'.\ML_data\loss{version_idx_str}.csv', sep=",")
    temp3 = temp3.to_numpy()

    parameter = np.array([width0,width1,height0,height1,move,coil0_width,coil1_width,gap0,gap1])

    temp1 = np.append(parameter,temp1)
    temp2 = np.append(parameter,temp2)
    temp3 = np.append(parameter,temp3)


    print(temp1)
    print(temp2)
    print(temp3)


    data1 = np.loadtxt(f'.\ML_data\inductance.csv', delimiter=",")
    new_data1 = np.vstack((data1, temp1))
    np.savetxt(f'.\ML_data\inductance.csv',new_data1,delimiter=",")

    data2 = np.loadtxt(f'.\ML_data\coupling.csv', delimiter=",")
    new_data2 = np.vstack((data2, temp2))
    np.savetxt(f'.\ML_data\coupling.csv',new_data2,delimiter=",")

    data3 = np.loadtxt(f'.\ML_data\loss.csv', delimiter=",")
    new_data3 = np.vstack((data3, temp3))
    np.savetxt(f'.\ML_data\loss.csv',new_data3,delimiter=",")




for i in range(0, 10000): 

    #run_simul(i)
    #print("end")


    try :
        try:
            os.remove(f'.\ML_aedt\ML6.aedt.lock')
        except:
            time.sleep(1)
        if os.path.isfile(f'.\ML_aedt\ML6.aedt') :
            os.remove(f'.\ML_aedt\ML6.aedt')
        time.sleep(1)	

        shutil.copy(f'.\ML_aedt\ML_ref.aedt',f'.\ML_aedt\ML6.aedt')
        time.sleep(1)

        try:
            run_simul(i)
        except Exception as e: 
            print(f'error number {i}')
            print(e)

        if os.path.isfile(f'.\ML_aedt\ML6.aedt') :
            os.remove(f'.\ML_aedt\ML6.aedt')
        time.sleep(1)	

        shutil.rmtree(f'.\ML_aedt\ML6.aedtresults')
        try:
            os.remove(f'.\ML_aedt\ML6.aedt.lock')
        except:
            time.sleep(1)
    except :
        time.sleep(1)	


    
    time.sleep(1)


os.system("pause")
