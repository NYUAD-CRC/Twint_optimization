#!/bin/bash

#Define the resource requirements here using #SBATCH

#For requesting 10 CPUs
#SBATCH -c 1
##SBATCH -p nvidia
##SBATCH --gres=gpu:1

#Max wallTime for the job
#SBATCH -t 32:00:00
#SBATCH -o 4_days_one_cpu.txt
#Resource requiremenmt commands end here


source /share/apps/NYUAD/miniconda/3-4.11.0/bin/activate
#activate any environments if required
conda activate twitter

#Execute the code
python 4_days.py | tee -a result.csv
