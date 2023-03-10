#!/bin/bash

#Define the resource requirements here using #SBATCH

#For requesting 5 CPUs
#SBATCH -c 5

#Max wallTime for the job
#SBATCH -t 48:00:00
#SBATCH -o 5_processes_5_cores_10_days.txt
#Resource requiremenmt commands end here

source /share/apps/NYUAD5/miniconda/3-4.11.0/bin/activate

#activate any environments if required
conda activate twitter

#Execute the code
time python optimized_refactored.py | tee -a  result_5_processes_5_cores_10_days.csv

