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
import os


for k in range(1, 31): 


    edited_lines = []
    with open(f'.\\script{k}\\rrs.py',encoding="UTF-8") as f:
        lines = f.readlines()
        for line in lines:
           # 조건에 따라 원하는 대로 line을 수정
            if f'script1' in line:
                edited_lines.append(line.replace('script1',f'script{k}'))
            else:
                edited_lines.append(line)

    with open(f'.\\script{k}\\rrs.py', 'w') as f:
        f.writelines(edited_lines)


    edited_lines = []
    with open(f'.\\script{k}\\rrs.py') as f:
        lines = f.readlines()
        for line in lines:
           # 조건에 따라 원하는 대로 line을 수정
            if f'ML1' in line:
                edited_lines.append(line.replace('ML1',f'ML{k}'))
            else:
                edited_lines.append(line)

    with open(f'.\\script{k}\\rrs.py', 'w') as f:
        f.writelines(edited_lines)

    edited_lines = []
    with open(f'.\\script{k}\\run_ansys_ref.py') as f:
        lines = f.readlines()
        for line in lines:
           # 조건에 따라 원하는 대로 line을 수정
            if f'script1' in line:
                edited_lines.append(line.replace('script1',f'script{k}'))
            else:
                edited_lines.append(line)

    with open(f'.\\script{k}\\run_ansys_ref.py', 'w') as f:
        f.writelines(edited_lines)


    edited_lines = []
    with open(f'.\\script{k}\\run_ansys_ref.py') as f:
        lines = f.readlines()
        for line in lines:
           # 조건에 따라 원하는 대로 line을 수정
           if f'ML1' in line:
                edited_lines.append(line.replace('ML1',f'ML{k}'))
           else:
                edited_lines.append(line)

    with open(f'.\\script{k}\\run_ansys_ref.py', 'w') as f:
        f.writelines(edited_lines)




