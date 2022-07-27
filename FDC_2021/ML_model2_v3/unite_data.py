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


with open('./Data_2021_08_11_v1.csv',"a", encoding='utf-8', newline='') as f :
    with open('./Data_5950X_N2_0811_v1.csv', "r") as infile:
        f.write(infile.read())
    with open('./Data_5600X1_0811_v1.csv', "r") as infile:
        f.write(infile.read())
    with open('./Data_5600X2_0811_v1.csv', "r") as infile:
        f.write(infile.read())
    with open('./Data_5600X3_0811_v1.csv', "r") as infile:
        f.write(infile.read())
    with open('./Data_5600X4_0811_v1.csv', "r") as infile:
        f.write(infile.read())
    with open('./Data_5600X5_0811_v1.csv', "r") as infile:
        f.write(infile.read())

