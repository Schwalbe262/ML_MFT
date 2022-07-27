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


for k in range(1, 13): 

    f = open(f'C:\script_v4\script{k}.bat', 'w')
    f.write(f'cd c:\script{k}\n')
    f.write(f'python rrs.py')
    f.close()


