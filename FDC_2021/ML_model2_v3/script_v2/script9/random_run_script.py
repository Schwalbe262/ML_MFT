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

#from pycaret.regression import load_model




REFERENCE_SCRIPT_FILE_NAME = f'C:\\script9\\run_ansys_ref.py'
    

def run_simul(version_idx_str):
    #0 Initialize random variables

    V1 = 1000
    X2V1 = 1000
    X3V1 = 1000
    X4V1 = 1000

    var1 = 10
    var2 = 15

    Imin = 8
    Imax = 27

    N1 = random.randrange(3,10)*2
    N2 = random.randrange(3,10)*2
    N = max(N1,N2)
    NX1 = int(N1/2)
    NY1 = int(NX1+1)
    NX2 = int(N2/2)
    NY2 = int(NX2+1)

    l1_min = 80 # 1e-1
    l1_max = 200 # 1e-1
    l2_max = 60
    h1_max = 80
    w1_min = 20
    w1_max = 100
    space2_max = 30
    space4_max = 30
    space5_max = 200
    space6_max = 200

    per = random.randrange(2000,5000)
    freq = 40e+3
    d1 = random.randrange(50,200) * 1e-2
    d2 = random.randrange(50,200) * 1e-2
    move_tx = d1 + random.randrange(10,200) * 0.01
    move_rx = d2 + random.randrange(10,200) * 0.01
    l1 = random.randrange(l1_min,l1_max)*1e-1
    space5 = random.randrange(math.ceil(d1*1e+2+d2*1e+2),math.ceil(d1*1e+2+d2*1e+2+space5_max)) * 1e-2
    space6 = random.randrange(math.ceil(d1*1e+2+d2*1e+2),math.ceil(d1*1e+2+d2*1e+2+space6_max)) * 1e-2
    space1 = random.randrange(math.ceil((d1/2+d2/2)*100),math.ceil((d1/2+d2/2+5)*100)) * 1e-2
    space2 = random.randrange(math.ceil((d1+d2+space1+space5+1)*100),space2_max*100) * 1e-2
    space3 = random.randrange(math.ceil((d1/2+d2/2)*100),math.ceil((d1/2+d2/2+5)*100)) * 1e-2
    space4 = random.randrange(math.ceil((d1+d2+space3+space6+1)*100),space4_max*100) * 1e-2
    l2 = random.randrange(math.ceil(space2+space5+d2/2+1),l2_max)
    maxh = max(math.ceil((NX1+1)*move_tx + 2*d1),math.ceil((NX2+1)*move_rx + 2*d2))
    h11 = math.ceil((NX1+1)*move_tx + 6*d1)
    h12 = math.ceil((NX2+1)*move_rx + 6*d2)
    h1 = random.randrange(maxh+math.ceil(max(d1,d2)),h1_max)
    offset_tx = random.randrange( -abs(math.ceil(-h1 + h11)), abs(math.ceil(h1 - h11)))/2
    offset_rx = random.randrange( -abs(math.ceil(-h1 + h12)), abs(math.ceil(h1 - h12)))/2
    w1 =  random.randrange(w1_min,w1_max)
    air = max(2*l1+h1,4*l1+l2,w1+40+d1+d2) + 50
    airx = w1/2+space4+30
    if N1==N :
        I2 = random.randrange(100,800)*1e-3
        I1 = N2/N1*I2 * random.randrange(800,1200) * 1e-3
    elif N2==N :
        I1 = random.randrange(100,800)*1e-3
        I2 = N1/N2*I1 * random.randrange(800,1200) * 1e-3

    X2per = random.randrange(2000,5000)
    X2freq = 40e+3
    X2d1 = random.randrange(50,200) * 1e-2
    X2d2 = random.randrange(50,200) * 1e-2
    X2move_tx = X2d1 + random.randrange(10,200) * 0.01
    X2move_rx = X2d2 + random.randrange(10,200) * 0.01
    X2l1 = random.randrange(l1_min,l1_max)*1e-1
    X2space5 = random.randrange(math.ceil(X2d1*1e+2+X2d2*1e+2),math.ceil(X2d1*1e+2+X2d2*1e+2+space5_max)) * 0.01
    X2space6 = random.randrange(math.ceil(X2d1*1e+2+X2d2*1e+2),math.ceil(X2d1*1e+2+X2d2*1e+2+space6_max)) * 0.01
    X2space1 = random.randrange(math.ceil((X2d1/2+X2d2/2)*100),math.ceil((X2d1/2+X2d2/2+5)*100)) * 1e-2
    X2space2 = random.randrange(math.ceil((X2d1+X2d2/2+X2space1+X2space5+1)*100),space2_max*100) * 1e-2
    X2space3 = random.randrange(math.ceil((X2d1/2+X2d2/2)*100),math.ceil((X2d1/2+X2d2/2+5)*100)) * 1e-2
    X2space4 = random.randrange(math.ceil((X2d1+X2d2/2+X2space3+X2space6+1)*100),space4_max*100) * 1e-2
    X2l2 = random.randrange(math.ceil(X2space2+X2space5+X2d2/2+1),l2_max)
    X2maxh = max(math.ceil((NX1+1)*X2move_tx + 2*X2d1),math.ceil((NX2+1)*X2move_rx + 2*X2d2))
    X2h11 = math.ceil((NX1+1)*X2move_tx + 6*X2d1)
    X2h12 = math.ceil((NX2+1)*X2move_rx + 6*X2d2)
    X2h1 = random.randrange(X2maxh+math.ceil(max(X2d1,X2d2)),h1_max)
    X2offset_tx = random.randrange( -abs(math.ceil(-X2h1 + X2h11)), abs(math.ceil(X2h1 - X2h11)))/2
    X2offset_rx = random.randrange( -abs(math.ceil(-X2h1 + X2h12)), abs(math.ceil(X2h1 - X2h12)))/2
    X2w1 =  random.randrange(w1_min,w1_max)
    X2air = max(2*X2l1+X2h1,4*X2l1+X2l2,X2w1+40+X2d1+X2d2) + 50
    X2airx = X2w1/2+X2space4+30
    if N1==N :
        X2I2 = random.randrange(100,800)*1e-3
        X2I1 = N2/N1*X2I2 * random.randrange(800,1200) * 1e-3
    elif N2==N :
        X2I1 = random.randrange(100,800)*1e-3
        X2I2 = N1/N2*X2I1 * random.randrange(800,1200) * 1e-3



    X3per = random.randrange(2000,5000)
    X3freq = 40e+3
    X3d1 = random.randrange(50,200) * 1e-2
    X3d2 = random.randrange(50,200) * 1e-2
    X3move_tx = X3d1 + random.randrange(10,200) * 0.01
    X3move_rx = X3d2 + random.randrange(10,200) * 0.01
    X3l1 = random.randrange(l1_min,l1_max)*1e-1
    X3space5 = random.randrange(math.ceil(X3d1*1e+2+X3d2*1e+2),math.ceil(X3d1*1e+2+X3d2*1e+2+space5_max)) * 0.01
    X3space6 = random.randrange(math.ceil(X3d1*1e+2+X3d2*1e+2),math.ceil(X3d1*1e+2+X3d2*1e+2+space6_max)) * 0.01
    X3space1 = random.randrange(math.ceil((X3d1/2+X3d2/2)*100),math.ceil((X3d1/2+X3d2/2+5)*100)) * 1e-2
    X3space2 = random.randrange(math.ceil((X3d1+X3d2/2+X3space1+X3space5+1)*100),space2_max*100) * 1e-2
    X3space3 = random.randrange(math.ceil((X3d1/2+X3d2/2)*100),math.ceil((X3d1/2+X3d2/2+5)*100)) * 1e-2
    X3space4 = random.randrange(math.ceil((X3d1+X3d2/2+X3space3+X3space6+1)*100),space4_max*100) * 1e-2
    X3l2 = random.randrange(math.ceil(X3space2+X3space5+X3d2/2+1),l2_max)
    X3maxh = max(math.ceil((NX1+1)*X3move_tx + 2*X3d1),math.ceil((NX2+1)*X3move_rx + 2*X3d2))
    X3h11 = math.ceil((NX1+1)*X3move_tx + 6*X3d1)
    X3h12 = math.ceil((NX2+1)*X3move_rx + 6*X3d2)
    X3h1 = random.randrange(X3maxh+math.ceil(max(X3d1,X3d2)),h1_max)
    X3offset_tx = random.randrange( -abs(math.ceil(-X3h1 + X3h11)), abs(math.ceil(X3h1 - X3h11)))/2
    X3offset_rx = random.randrange( -abs(math.ceil(-X3h1 + X3h12)), abs(math.ceil(X3h1 - X3h12)))/2
    X3w1 =  random.randrange(w1_min,w1_max)
    X3air = max(2*X3l1+X3h1,4*X3l1+X3l2,X3w1+40+X3d1+X3d2) + 50
    X3airx = X3w1/2+X3space4+30
    if N1==N :
        X3I2 = random.randrange(100,800)*1e-3
        X3I1 = N2/N1*X3I2 * random.randrange(800,1200) * 1e-3
    elif N2==N :
        X3I1 = random.randrange(100,800)*1e-3
        X3I2 = N1/N2*X3I1 * random.randrange(800,1200) * 1e-3



    X4per = random.randrange(2000,5000)
    X4freq = 40e+3
    X4d1 = random.randrange(50,200) * 1e-2
    X4d2 = random.randrange(50,200) * 1e-2
    X4move_tx = X4d1 + random.randrange(10,200) * 0.01
    X4move_rx = X4d2 + random.randrange(10,200) * 0.01
    X4l1 = random.randrange(l1_min,l1_max)*1e-1
    X4space5 = random.randrange(math.ceil(X4d1*1e+2+X4d2*1e+2),math.ceil(X4d1*1e+2+X4d2*1e+2+space5_max)) * 0.01
    X4space6 = random.randrange(math.ceil(X4d1*1e+2+X4d2*1e+2),math.ceil(X4d1*1e+2+X4d2*1e+2+space6_max)) * 0.01
    X4space1 = random.randrange(math.ceil((X4d1/2+X4d2/2)*100),math.ceil((X4d1/2+X4d2/2+5)*100)) * 1e-2
    X4space2 = random.randrange(math.ceil((X4d1+X4d2/2+X4space1+X4space5+1)*100),space2_max*100) * 1e-2
    X4space3 = random.randrange(math.ceil((X4d1/2+X4d2/2)*100),math.ceil((X4d1/2+X4d2/2+5)*100)) * 1e-2
    X4space4 = random.randrange(math.ceil((X4d1+X4d2/2+X4space3+X4space6+1)*100),space4_max*100) * 1e-2
    X4l2 = random.randrange(math.ceil(X4space2+X4space5+X4d2/2+1),l2_max)
    X4maxh = max(math.ceil((NX1+1)*X4move_tx + 2*X4d1),math.ceil((NX2+1)*X4move_rx + 2*X4d2))
    X4h11 = math.ceil((NX1+1)*X4move_tx + 6*X4d1)
    X4h12 = math.ceil((NX2+1)*X4move_rx + 6*X4d2)
    X4h1 = random.randrange(X4maxh+math.ceil(max(X4d1,X4d2)),h1_max)
    X4offset_tx = random.randrange( -abs(math.ceil(-X4h1 + X4h11)), abs(math.ceil(X4h1 - X4h11)))/2
    X4offset_rx = random.randrange( -abs(math.ceil(-X4h1 + X4h12)), abs(math.ceil(X4h1 - X4h12)))/2
    X4w1 =  random.randrange(w1_min,w1_max)
    X4air = max(2*X4l1+X4h1,4*X4l1+X4l2,X4w1+40+X4d1+X4d2) + 50
    X4airx = X4w1/2+X4space4+30
    if N1==N :
        X4I2 = random.randrange(100,800)*1e-3
        X4I1 = N2/N1*X4I2 * random.randrange(800,1200) * 1e-3
    elif N2==N :
        X4I1 = random.randrange(100,800)*1e-3
        X4I2 = N1/N2*X4I1 * random.randrange(800,1200) * 1e-3


    str_tx = f'Tx_in,Tx_out,Tx1,'
    Tx_loop = ""
    for i in range(1,NX1) :

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
    Tx2_loop = ""
    str_tx = str_tx + f'Tx{NY1},'

    for i in range(NY1,N1-1) :

        str_tx = str_tx + f'Tx{i+1},'

        Tx2_loop = Tx2_loop + "oEditor.Paste()\n"
        Tx2_loop = Tx2_loop + "oEditor.Move(\n"
        Tx2_loop = Tx2_loop + "   [\n"
        Tx2_loop = Tx2_loop + f'    "NAME:Selections",\n'
        Tx2_loop = Tx2_loop + f'    "Selections:="		, "Tx{i+1}",\n'
        Tx2_loop = Tx2_loop + f'    "NewPartsModelFlag:="	, "Model"\n'
        Tx2_loop = Tx2_loop + "   ],\n"
        Tx2_loop = Tx2_loop + "   [\n"
        Tx2_loop = Tx2_loop + f'    "NAME:TranslateParameters",\n'
        Tx2_loop = Tx2_loop + f'    "TranslateVectorX:="	, "0",\n'
        Tx2_loop = Tx2_loop + f'    "TranslateVectorY:="	, "0",\n'
        Tx2_loop = Tx2_loop + f'    "TranslateVectorZ:="	, "-{NX1-(i+1-NX1)}*move_tx+offset_tx"\n'
        Tx2_loop = Tx2_loop + "   ])\n"
    str_tx = str_tx + f'Tx{N1}'
    #str_tx = str_tx[:-1]

    str_rx = f'Rx_in,Rx_out,Rx1,'
    Rx_loop = ""
    for i in range(1,NX2) :

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
    Rx2_loop = ""
    str_rx = str_rx + f'Rx{NY2},'

    for i in range(NY2,N2-1) :

        str_rx = str_rx + f'Rx{i+1},'

        Rx2_loop = Rx2_loop + "oEditor.Paste()\n"
        Rx2_loop = Rx2_loop + "oEditor.Move(\n"
        Rx2_loop = Rx2_loop + "   [\n"
        Rx2_loop = Rx2_loop + f'    "NAME:Selections",\n'
        Rx2_loop = Rx2_loop + f'    "Selections:="		, "Rx{i+1}",\n'
        Rx2_loop = Rx2_loop + f'    "NewPartsModelFlag:="	, "Model"\n'
        Rx2_loop = Rx2_loop + "   ],\n"
        Rx2_loop = Rx2_loop + "   [\n"
        Rx2_loop = Rx2_loop + f'    "NAME:TranslateParameters",\n'
        Rx2_loop = Rx2_loop + f'    "TranslateVectorX:="	, "0",\n'
        Rx2_loop = Rx2_loop + f'    "TranslateVectorY:="	, "0",\n'
        Rx2_loop = Rx2_loop + f'    "TranslateVectorZ:="	, "-{NX2-(i+1-NX2)}*move_rx+offset_rx"\n'
        Rx2_loop = Rx2_loop + "   ])\n"
    str_rx = str_rx + f'Rx{N2}'
    #str_rx = str_rx[:-1]



    #FIXME : add some variables

    #0.5 Config Identifier-Variable set.
    config = {
        "$VERSION_IDX_STR"  :   version_idx_str,
        "$N1"              :   N1,
        "$N2"              :   N2,
        "$NX1"              :   NX1,
        "$NX2"              :   NX2,
        "$NY1"              :   NY1,
        "$NY2"              :   NY2,

        "$per"              :   per,
        "$freq"              :   freq,
        "$V1"              :   V1,
        "$l1"              :   l1,
        "$l2"              :   l2,
        "$h1"              :   h1,
        "$w1"              :   w1,
        "$d1"              :   d1,
        "$d2"              :   d2,
        "$offset_tx"              :   offset_tx,
        "$offset_rx"              :   offset_rx,
        "$move_tx"              :   move_tx,
        "$move_rx"              :   move_rx,
        "$Tx_loop"              :   Tx_loop,
        "$Tx2_loop"              :   Tx2_loop,
        "$str_tx"              :   str_tx,
        "$Rx_loop"              :   Rx_loop,
        "$Rx2_loop"              :   Rx2_loop,
        "$str_rx"              :   str_rx,
        "$air"              :   air,
        "$xair"              :   airx,
        "$space1"              :   space1,
        "$space2"              :   space2,
        "$space3"              :   space3,
        "$space4"              :   space4,
        "$space5"              :   space5,
        "$space6"              :   space6,
        "$I1"                   : I1,
        "$I2"                   : I2,

        "$X2per"              :   X2per,
        "$X2freq"              :   X2freq,
        "$X2V1"              :   X2V1,
        "$X2l1"              :   X2l1,
        "$X2l2"              :   X2l2,
        "$X2h1"              :   X2h1,
        "$X2w1"              :   X2w1,
        "$X2d1"              :   X2d1,
        "$X2d2"              :   X2d2,
        "$X2offset_tx"              :   X2offset_tx,
        "$X2offset_rx"              :   X2offset_rx,
        "$X2move_tx"              :   X2move_tx,
        "$X2move_rx"              :   X2move_rx,
        "$X2air"              :   X2air,
        "$X2xair"              :   X2airx,
        "$X2space1"              :   X2space1,
        "$X2space2"              :   X2space2,
        "$X2space3"              :   X2space3,
        "$X2space4"              :   X2space4,
        "$X2space5"              :   X2space5,
        "$X2space6"              :   X2space6,
        "$X2I1"                   : X2I1,
        "$X2I2"                   : X2I2,


        "$X3per"              :   X3per,
        "$X3freq"              :   X3freq,
        "$X3V1"              :   X3V1,
        "$X3l1"              :   X3l1,
        "$X3l2"              :   X3l2,
        "$X3h1"              :   X3h1,
        "$X3w1"              :   X3w1,
        "$X3d1"              :   X3d1,
        "$X3d2"              :   X3d2,
        "$X3offset_tx"              :   X3offset_tx,
        "$X3offset_rx"              :   X3offset_rx,
        "$X3move_tx"              :   X3move_tx,
        "$X3move_rx"              :   X3move_rx,
        "$X3air"              :   X3air,
        "$X3xair"              :   X3airx,
        "$X3space1"              :   X3space1,
        "$X3space2"              :   X3space2,
        "$X3space3"              :   X3space3,
        "$X3space4"              :   X3space4,
        "$X3space5"              :   X3space5,
        "$X3space6"              :   X3space6,
        "$X3I1"                   : X3I1,
        "$X3I2"                   : X3I2,


        "$X4per"              :   X4per,
        "$X4freq"              :   X4freq,
        "$X4V1"              :   X4V1,
        "$X4l1"              :   X4l1,
        "$X4l2"              :   X4l2,
        "$X4h1"              :   X4h1,
        "$X4w1"              :   X4w1,
        "$X4d1"              :   X4d1,
        "$X4d2"              :   X4d2,
        "$X4offset_tx"              :   X4offset_tx,
        "$X4offset_rx"              :   X4offset_rx,
        "$X4move_tx"              :   X4move_tx,
        "$X4move_rx"              :   X4move_rx,
        "$X4air"              :   X4air,
        "$X4xair"              :   X4airx,
        "$X4space1"              :   X4space1,
        "$X4space2"              :   X4space2,
        "$X4space3"              :   X4space3,
        "$X4space4"              :   X4space4,
        "$X4space5"              :   X4space5,
        "$X4space6"              :   X4space6,
        "$X4I1"                   : X4I1,
        "$X4I2"                   : X4I2







        #FIXME : add some idt : variables
    }

    #1 Make Folder
    folder_name = f'SIMUL_{version_idx_str}'
    os.mkdir(f'C:\script9\ML\SIMUL_{version_idx_str}')

    #2 Make Variable info file
    with open(f'C:\script9\ML\SIMUL_{version_idx_str}\info.yaml', "w") as info_file:
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
    with open(f'C:\\script9\\ML\\SIMUL_{version_idx_str}\\run_ansys_{version_idx_str}.py',"w") as f :
        f.write(ref_script_str)


    #4 make batch file.
    
    filepath2 = os.path.join('ML',folder_name,f'run_bat_{version_idx_str}.bat')
    with open(f'C:\\script9\\ML\\SIMUL_{version_idx_str}\\run_bat_{version_idx_str}.bat',"w") as f :
        f.write(f'"C:\\Program Files\\AnsysEM\\AnsysEM21.1\\Win64\\ansysedt.exe" -iconic -runscriptandexit "C:\\script9\\ML\\SIMUL_{version_idx_str}\\run_ansys_{version_idx_str}.py"')

    workingDir = f'C:\script9\ML\SIMUL_{version_idx_str}'
    executeFile = f'C:\script9\ML\SIMUL_{version_idx_str}\\run_bat_{version_idx_str}.bat'
    os.chdir(workingDir)
    os.system(executeFile)

    with open(f'C:\script9\ML_data\Data1 {version_idx_str}.csv',"r") as f :
        rdr = csv.reader(f)
        for line1_1 in rdr:
            a = 1
    with open(f'C:\script9\ML_data\Data2 {version_idx_str}.csv',"r") as f :
        rdr = csv.reader(f)
        for line2_1 in rdr:
            a = 1
    with open(f'C:\script9\ML_data\Data3 {version_idx_str}.csv',"r") as f :
        rdr = csv.reader(f)
        for line1_2 in rdr:
            a = 1
    with open(f'C:\script9\ML_data\Data4 {version_idx_str}.csv',"r") as f :
        rdr = csv.reader(f)
        for line2_2 in rdr:
            a = 1
    with open(f'C:\script9\ML_data\Data5 {version_idx_str}.csv',"r") as f :
        rdr = csv.reader(f)
        for line1_3 in rdr:
            a = 1
    with open(f'C:\script9\ML_data\Data6 {version_idx_str}.csv',"r") as f :
        rdr = csv.reader(f)
        for line2_3 in rdr:
            a = 1
    with open(f'C:\script9\ML_data\Data7 {version_idx_str}.csv',"r") as f :
        rdr = csv.reader(f)
        for line1_4 in rdr:
            a = 1
    with open(f'C:\script9\ML_data\Data8 {version_idx_str}.csv',"r") as f :
        rdr = csv.reader(f)
        for line2_4 in rdr:
            a = 1

    with open(f'C:\script9\ML_data\Data.csv',"a", encoding='utf-8', newline='') as f :

        tmp = np.concatenate((N1, N2, d1, d2, freq, move_tx, move_rx, offset_tx, offset_rx, per, space1, space2, space3, space4, space5, space6, l1, l2, h1, w1, line1_1[1], line1_1[2], line1_1[3], line1_1[4], line1_1[5], line1_1[6], line1_1[7], line1_1[8], line1_1[9], line1_1[10], line1_1[11], line1_1[12], line1_1[13], line1_1[14], line1_1[15], line2_1[2], line2_1[3]), axis=None)
        wr = csv.writer(f)
        wr.writerow(tmp)

        tmp = np.concatenate((N1, N2, X2d1, X2d2, X2freq, X2move_tx, X2move_rx, X2offset_tx, X2offset_rx, X2per, X2space1, X2space2, X2space3, X2space4, X2space5, X2space6, X2l1, X2l2, X2h1, X2w1, line1_2[1], line1_2[2], line1_2[3], line1_2[4], line1_2[5], line1_2[6], line1_2[7], line1_2[8], line1_2[9], line1_2[10], line1_2[11], line1_2[12], line1_2[13], line1_2[14], line1_2[15], line2_2[2], line2_2[3]), axis=None)
        wr = csv.writer(f)
        wr.writerow(tmp)

        tmp = np.concatenate((N1, N2, X3d1, X3d2, X3freq, X3move_tx, X3move_rx, X3offset_tx, X3offset_rx, X3per, X3space1, X3space2, X3space3, X3space4, X3space5, X3space6, X3l1, X3l2, X3h1, X3w1, line1_3[1], line1_3[2], line1_3[3], line1_3[4], line1_3[5], line1_3[6], line1_3[7], line1_3[8], line1_3[9], line1_3[10], line1_3[11], line1_3[12], line1_3[13], line1_3[14], line1_3[15], line2_3[2], line2_3[3]), axis=None)
        wr = csv.writer(f)
        wr.writerow(tmp)

        tmp = np.concatenate((N1, N2, X4d1, X4d2, X4freq, X4move_tx, X4move_rx, X4offset_tx, X4offset_rx, X4per, X4space1, X4space2, X4space3, X4space4, X4space5, X4space6, X4l1, X4l2, X4h1, X4w1, line1_4[1], line1_4[2], line1_4[3], line1_4[4], line1_4[5], line1_4[6], line1_4[7], line1_4[8], line1_4[9], line1_4[10], line1_4[11], line1_4[12], line1_4[13], line1_4[14], line1_4[15], line2_4[2], line2_4[3]), axis=None)
        wr = csv.writer(f)
        wr.writerow(tmp)


for i in range(1, 10000): 

    #run_simul(i)
    #print("end")


    try :
        try:
            os.remove(f'C:\script9\ML_aedt\ML9.aedt.lock')
        except:
            time.sleep(1)
        run_simul(i)
        time.sleep(1)	
        try:
            os.remove(f'C:\script9\ML_aedt\ML9.aedt.lock')
        except:
            time.sleep(1)
    except :
        time.sleep(1)	


    
    time.sleep(1)
