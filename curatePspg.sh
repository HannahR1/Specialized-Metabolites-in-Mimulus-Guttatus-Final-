#!/bin/bash --login
########## SBATCH Lines for Resource Request ##########
#SBATCH --time=00:01:00
#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=1
#SBATCH --job-name curatePspg.sh


python pspgBox.py

sort "PspgID.txt" | uniq > "PspgIDUniq.txt"

python parsePrimary2.py

python RemoveWhiteSpc2.py

python Format2.py

python GetFullSeqsPSPG.py


