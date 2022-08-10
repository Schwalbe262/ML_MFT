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


    # Design 1

    raw_data = np.loadtxt("manual.csv",delimiter=",")

    [N1,N2,w1,l1,l2,h1,per,space1,space2,space3,space4,space5,space6,coil_width1,coil_width2,move_z1,move_z2,offset_z1,offset_z2] = raw_data[int(version_idx_str),:]

    NX1 = N1/2
    NX2 = N2/2




    airx = 500
    airy = 500
    airz = 500



    #FIXME : add some variables


    #0.5 Config Identifier-Variable set.
    config = {
        "$VERSION_IDX_STR"  :   version_idx_str,
        "$air_x"  :  airx,
        "$air_y"  :  airy,
        "$air_z"  :  airz,
        "$N1"  :  N1,
        "$N2"  :  N2,
        "$NX1"  :  NX1,
        "$NX2"  :  NX2,
        "$w1"  :  w1,
        "$l1"  :  l1,
        "$l2"  :  l2,
        "$h1"  :  h1,
        "$per" : per,
        "$space1"  :  space1,
        "$space2"  :  space2,
        "$space3"  :  space3,
        "$space4"  :  space4,
        "$space5"  :  space5,
        "$space6"  :  space6,
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




for i in range(0, 10000): 

    #run_simul(i)
    #print("end")


    try :
        try:
            os.remove(f'.\ML_aedt\ML1.aedt.lock')
        except:
            time.sleep(1)
        if os.path.isfile(f'.\ML_aedt\ML1.aedt') :
            os.remove(f'.\ML_aedt\ML1.aedt')
        time.sleep(1)	

        shutil.copy(f'.\ML_aedt\ML_ref.aedt',f'.\ML_aedt\ML1.aedt')
        time.sleep(1)

        try:
            run_simul(i)
        except Exception as e: 
            print(f'error number {i}')
            print(e)

        if os.path.isfile(f'.\ML_aedt\ML1.aedt') :
            os.remove(f'.\ML_aedt\ML1.aedt')
        time.sleep(1)	

        shutil.rmtree(f'.\ML_aedt\ML1.aedtresults')
        try:
            os.remove(f'.\ML_aedt\ML1.aedt.lock')
        except:
            time.sleep(1)
    except :
        time.sleep(1)	


    
    time.sleep(1)


os.system("pause")
