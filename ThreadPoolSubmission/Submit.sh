#!/bin/bash

#Define the resource requirements here using #SBATCH

#For requesting 10 CPUs
#SBATCH -c 1
##SBATCH -p nvidia
##SBATCH --gres=gpu:1

#Max wallTime for the job
#SBATCH -t 32:00:00
#SBATCH -o one_cpu_second.txt
#Resource requiremenmt commands end here


#activate any environments if required
conda activate twitter

#Execute the code
python test.py | tee -a result.csv
