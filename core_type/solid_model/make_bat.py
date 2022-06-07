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


for k in range(1, 31): 

    f = open(f'script{k}.bat', 'w')
    f.write(f'cd script{k}\n')
    f.write(f'python rrs.py')
    f.close()


