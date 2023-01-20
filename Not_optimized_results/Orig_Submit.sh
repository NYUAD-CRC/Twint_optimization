#!/bin/bash

#Define the resource requirements here using #SBATCH

#For requesting 10 CPUs
#SBATCH -c 1

#Max wallTime for the job
#SBATCH -t 32:00:00
#SBATCH -o Org_one_cpu_two_days.txt
#Resource requiremenmt commands end here

source /share/apps/NYUAD5/miniconda/3-4.11.0/bin/activate

#activate any environments if required
conda activate twitter

#Execute the code
python 	Original.py | tee -a Orig_result.csv

