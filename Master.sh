#!/bin/bash --login
########## SBATCH Lines for Resource Request ##########
#SBATCH --time=00:01:00
#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=1
#SBATCH --job-name Master.sh 

sbatch HMMsearch.sh

sbatch curatePspg.sh

sbatch curateSize.sh

sbatch curateExpressed.sh
