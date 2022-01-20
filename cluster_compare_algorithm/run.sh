#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=47    # Cores per node
#SBATCH --partition=cpu1        # Partition Name (cpu1, gpu1, hgx)
##
#SBATCH --job-name=SlurmExample
#SBATCH -o SLURM.%N.%j.out         # STDOUT
#SBATCH -e SLURM.%N.%j.err         # STDERR
##

hostname
date

## 
#module add  ANACONDA/2020.11

python ~/ML_MFT/cluster_compare_algorithm.py
