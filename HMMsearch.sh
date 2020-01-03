#!/bin/bash --login
########## SBATCH Lines for Resource Request ##########
#SBATCH --time=00:01:00
#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=1
#SBATCH --job-name HMMERsearch

export PATH=$PATH:/$HOME/Documents/HMMER/hmmer-3.2.1/hmmer-3.2.1/src/

hmmsearch -A MimUGTs.sto UDPGT.hmm MguttatusSeq.fasta > hmmsearch.out 

python GetHmmSearchHits1.py

sort MimUGTIDs.txt | uniq >  MimUGTIDsUniq.txt

fgrep -f MimUGTIDsUniq.txt MguttatusSeq.fasta > MimUGTFastaID.txt

python parsePrimary1.py

python RemoveWhiteSpc1.py

python Format1.py

python GetFullSeqs.py

