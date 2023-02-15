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

# ==============================
# random_choice : 
# X[0] : 
# X[1] : 
# X[2] : resolution
# X[3] : 
# return : 
def random_choice(X) :
    return round(np.random.choice( np.arange( X[0] , X[1]+X[2] , X[2]) ),X[3])
# ==============================

def run_simul(version_idx_str):

    # ==============================
    # STEP 1-1 : 
    #  overview.txt 

    LV_loss_range = [0, 500, 1, 0]
    HV_loss_range = [0, 500, 1, 0]
    core_loss_range = [0, 1000, 1, 0]
    epoxy_thermal_coeff_range = [0.1, 2.0, 0.1, 1]
    bobin_thermal_coeff_range = [0.1, 2.0, 0.1, 1]
    core_thermal_coeff_range = [4, 200, 1, 0]
    cold_x1_range = [0, 100, 1, 0]
    cold_y1_range = [0, 60, 1, 0]
    cold_z1_range = [5, 30, 1, 0]
    N1_range = [2, 10, 1, 0]

    offset_z1_range = [-20, 20, 0.1, 1]
    offset_z2_range = [-20, 20, 0.1, 1]
    move_z1_range = [0.5, 8, 0.1, 1]
    move_z2_range = [0.5, 8, 0.1 ,1]
    coil_width1_range = [2, 15, 0.1 ,1]
    coil_width2_range = [2, 15, 0.1, 1]
    space1_range = [2, 50, 1, 0]
    space2_range = [2, 50, 1, 0]
    space3_range = [2, 50, 1, 0]
    space4_range = [2, 50, 1, 0]

    epoxy_x_range = [5, 25, 1, 0]
    epoxy_y_range = [5, 25, 1, 0]
    w1_range = [20, 200, 1, 0]
    l1_range = [10, 50, 1, 0]
    epoxy_gap_range = [0, 1, 0.1 ,1]
    bobin_skirt_range = [0, 3, 0.1, 1]


    # ==============================
    # STEP 1-2 : 

    LV_loss = random_choice(LV_loss_range)
    HV_loss = random_choice(HV_loss_range)
    core_loss = random_choice(core_loss_range)
    epoxy_thermal_coeff = random_choice(epoxy_thermal_coeff_range)
    bobin_thermal_coeff = random_choice(bobin_thermal_coeff_range)
    core_thermal_coeff = random_choice(core_thermal_coeff_range)
    cold_x1 = random_choice(cold_x1_range)
    cold_y1 = random_choice(cold_y1_range)
    cold_z1 = random_choice(cold_z1_range)
    N1 = random_choice(N1_range)

    offset_z1 = random_choice(offset_z1_range)
    offset_z2 = random_choice(offset_z2_range)
    move_z1 = random_choice(move_z1_range)
    move_z2 = random_choice(move_z2_range)
    coil_width1 = random_choice(coil_width1_range)
    coil_width2 = random_choice(coil_width2_range)
    space1 = random_choice(space1_range)
    space2 = random_choice(space2_range)
    space3 = random_choice(space3_range)
    space4 = random_choice(space4_range)

    epoxy_x = random_choice(epoxy_x_range)
    epoxy_y = random_choice(epoxy_y_range)
    w1 = random_choice(w1_range)
    l1 = random_choice(l1_range)
    epoxy_gap = random_choice(epoxy_gap_range)
    bobin_skirt = random_choice(bobin_skirt_range)

    
    # ==============================
    # STEP 1-3 : 

    cold_x2_range = [0, cold_x1/2, 1, 0]
    cold_y2_range = [0, cold_y1/2, 1, 0]
    fillet_core_range = [0, l1, 1, 1]
    bobin_thick_range = [0, min(space3,space4), 0.1, 1]


    cold_x2 = random_choice(cold_x2_range)
    cold_y2 = random_choice(cold_y2_range)
    fillet_core = random_choice(fillet_core_range)
    bobin_thick = random_choice(bobin_thick_range)


    # ==============================
    # STEP 1-4 : 

    l2_min = np.round(coil_width1 + coil_width2 + space2 + space4 + epoxy_y,0)

    fillet_epoxy_range = [0, 15, 0.1, 1]
    l2_range = [l2_min+5, 180, 1, 0]

    fillet_epoxy = random_choice(fillet_epoxy_range)
    l2 = random_choice(l2_range)


    # ==============================
    # STEP 1-5 : 

    h1_min = max(N1*coil_width1 + (N1+0.5)*move_z1 + 2*abs(offset_z1), N1*coil_width2 + (N1+0.5)*move_z2 + 2*abs(offset_z2))

    
    if h1_min < 150 :
        h1_range = [h1_min, 150, 1, 0]
    else :
        h1_range = [h1_min, h1_min*1.2,1 ,0]

    h1 = random_choice(h1_range)

    if cold_y1 - cold_y2 < fillet_core : 
        cold_z2_max = math.floor( 10* fillet_core * (1 - math.sin(math.acos((cold_y1 - cold_y2) / fillet_core)) )) / 10
    else :
        cold_z2_max = l1

    cold_z2_range = [0, cold_z2_max, 0.1, 1]

    cold_z2 = random_choice(cold_z2_range)


    # ==============================



    # ==============================
    # STEP 2 : Comfig Identifier-Variable set.

    config = {
        #FIXME idt : variable
        "$VERSION_IDX_STR"  :   version_idx_str,
        "$N1"  :  N1,
        "$w1"  :  w1,
        "$l1"  :  l1,
        "$l2"  :  l2,
        "$h1"  :  h1,
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
        "$LV_loss"  :  LV_loss,
        "$HV_loss"  :  HV_loss,
        "$core_loss"  :  core_loss,
        "$epoxy_x" : epoxy_x,
        "$epoxy_y" : epoxy_y,
        "$cold_x1" : cold_x1,
        "$cold_y1" : cold_y1,
        "$cold_z1" : cold_z1,
        "$cold_x2" : cold_x2,
        "$cold_y2" : cold_y2,
        "$cold_z2" : cold_z2,
        "$fillet_epoxy" : fillet_epoxy,
        "$fillet_core" : fillet_core,
        "$epoxy_thermal_coeff" : epoxy_thermal_coeff,
        "$bobin_thermal_coeff" : bobin_thermal_coeff,
        "$core_thermal_coeff" : core_thermal_coeff,
        "$epoxy_gap" : epoxy_gap,
        "$bobin_thick" : bobin_thick,
        "$bobin_skirt" : bobin_skirt
    }


    # ==============================
    # STEP 3 : Make empty folder for each iteration
    folder_name = f'SIMUL_{version_idx_str}'
    os.mkdir(f'.\ML\SIMUL_{version_idx_str}')


    # ==============================
    # STEP 4 : Make empty folder for each iteration
    with open(f'.\ML\SIMUL_{version_idx_str}\info.yaml', "w") as info_file:
        yaml.dump(config,info_file)


    # ==============================
    # STEP 4 : Make python script file for ansys modeling automation
    # Load file string
    ref_script_str = ""
    with open(REFERENCE_SCRIPT_FILE_NAME) as f :
        lines = f.readlines()
    ref_script_str = "\n".join(lines)

    # Change Identifiers
    for idt, var in config.items() :
        ref_script_str = ref_script_str.replace(idt, str(var))

    # Save file
    with open(f'.\\ML\\SIMUL_{version_idx_str}\\run_ansys_{version_idx_str}.py',"w") as f :
        f.write(ref_script_str)

    # ==============================
    # STEP 5 : Make batch file for running simulation
    filepath2 = os.path.join('ML',folder_name,f'run_bat_{version_idx_str}.bat')
    with open(f'.\\ML\\SIMUL_{version_idx_str}\\run_bat_{version_idx_str}.bat',"w") as f :
        f.write(f'"C:\\Program Files\\AnsysEM\\AnsysEM21.1\\Win64\\ansysedt.exe" -iconic -runscriptandexit ".\\ML\SIMUL_{version_idx_str}\\run_ansys_{version_idx_str}.py"')



    # ==============================
    # STEP 6 : Execute batch file
    workingDir = f'.\\ML\\SIMUL_{version_idx_str}'
    executeFile = f'.\\ML\\SIMUL_{version_idx_str}\\run_bat_{version_idx_str}.bat'

    try :
        os.system(executeFile)
    except :
        time.sleep(1)

    # ==============================
    # ==============================
    # ANSYS simulation ... ... ...
    # ==============================
    # ==============================


    # ==============================
    # STEP 7 : Save temp data
    temp1 = pd.read_csv(f'.\\ML_data\\temp_data_{version_idx_str}.csv', sep=",")
    temp1 = temp1.to_numpy()

    parameter = np.array([N1, w1, l1, l2, h1, space1, space2, space3, space4, fillet_core, \
    fillet_epoxy, coil_width1, coil_width2, move_z1, move_z2, offset_z1, offset_z2, epoxy_x, epoxy_y, LV_loss, \
    HV_loss, core_loss, epoxy_thermal_coeff, core_thermal_coeff, cold_x1, cold_y1, cold_z1, cold_x2, cold_y2, cold_z2, \
    epoxy_gap, bobin_thick, bobin_skirt])

    temp = np.append(parameter,temp1)

    print(temp)


    final_data = np.loadtxt(f'Z:\\Autosimul_data\\MFT\\SST_2023\\core_type_icepak_v1\\{COMPUTER_NAME}\\script15\\temp_data.csv', delimiter=",")
    new_data1 = np.vstack((final_data, temp))
    np.savetxt(f'Z:\\Autosimul_data\\MFT\\SST_2023\\core_type_icepak_v1\\{COMPUTER_NAME}\\script15\\temp_data.csv',new_data1,delimiter=",")




for i in range(0, 10000): 

    #run_simul(i)
    #print("end")


    try :
        try:
            os.remove(f'.\ML_aedt\ML15.aedt.lock')
        except:
            time.sleep(1)
        if os.path.isfile(f'.\ML_aedt\ML15.aedt') :
            os.remove(f'.\ML_aedt\ML15.aedt')
        time.sleep(1)	

        shutil.copy(f'.\ML_aedt\ML_ref.aedt',f'.\ML_aedt\ML15.aedt')
        time.sleep(1)

        try:
            run_simul(i)
        except Exception as e: 
            print(f'error number {i}')
            print(e)

        if os.path.isfile(f'.\ML_aedt\ML15.aedt') :
            os.remove(f'.\ML_aedt\ML15.aedt')
        time.sleep(1)	

        shutil.rmtree(f'.\ML_aedt\ML15.aedtresults')
        try:
            os.remove(f'.\ML_aedt\ML15.aedt.lock')
        except:
            time.sleep(1)
    except :
        time.sleep(1)	


    
    time.sleep(1)


os.system("pause")
