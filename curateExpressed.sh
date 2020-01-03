#!/bin/bash --login
########## SBATCH Lines for Resource Request ##########
#SBATCH --time=00:01:00
#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=1
#SBATCH --job-name curateExpressed.sh 

sort expressedAnnot.txt | uniq >  expressedAnnotuniq.txt

fgrep -f expressedAnnotuniq.txt MguttatusSeq.fasta > MimUGTExpFastaID.txt

python parsePrimary3.py

python RemoveWhiteSpc4.py

python Format4.py

python GetFullSeqsExpsd.py
