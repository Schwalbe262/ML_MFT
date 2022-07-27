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


for k in range(1, 19): 

    f = open(f'C:\script_v3\script{k}.bat', 'w')
    f.write(f'cd c:\script{k}\n')
    f.write(f'python random_run_script.py')
    f.close()


