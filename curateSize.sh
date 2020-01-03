#!/bin/bash --login
########## SBATCH Lines for Resource Request ##########
#SBATCH --time=00:01:00
#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=1
#SBATCH --job-name curateSize

python RemoveWhiteSpc3.py
python Format3.py
python GetFullSeqSize.py
