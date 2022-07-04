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


with open(f'.\inductance.csv',"a", encoding='utf-8', newline='') as f :
    for k in range (1,201) :
        with open(f'.\script{k}\ML_data\inductance.csv', "r") as infile:
            f.write(infile.read())

with open(f'.\coupling.csv',"a", encoding='utf-8', newline='') as f :
    for k in range (1,201) :
        with open(f'.\script{k}\ML_data\coupling.csv', "r") as infile:
            f.write(infile.read())

with open(f'.\loss.csv',"a", encoding='utf-8', newline='') as f :
    for k in range (1,201) :
        with open(f'.\script{k}\ML_data\loss.csv', "r") as infile:
            f.write(infile.read())