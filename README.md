# Specialized-Metabolites-in-Mimulus-Guttatus-Final-

# Specialized-Metabolites-in-Mimulus-guttatus-
#readme file 

# HMMsearch - Extract the UGTs from the Mimulus Protein Annotation Database 
HMMsearch.sh - extracts the mimulus genes that are UGTs 
Input(s):
MguttatusSeq.fasta - genome of mimulus guttatus annotated genes
UDPGT.hmm - hmm profile of UDPGTs from pfam 
Files: GetHmmSearchHits.py, parsePrimary.py, RemoveWhiteSpc.py, GetFullSeqs.py
Outputs: hmmsearch.out - the hmmSearch output file not formatted in the sto
MimUGTs.sto - hmmsearch output formatted into .sto file
MimUGTIDsUniq.txt - IDs from the MimUGTIDs.txt that are unique and nonoverlapping
MimUGTFastaID.txt -  full fasta ID from the original mimulus genome annotation file

Name: GetHmmSearchHits2.py
Description: Get the names of the mimulus genes that was a hit 
Input: MimUGTs.sto
Output:  MimUGTIDs.txt

Name: parsePrimary.py
Description: parses through the MimUGTIDs.txt to write fasta IDs refer only to primary annotations to the output file. 
Input(s): MimUGTFastaID.txt
Outputs(s): MimUGTPrimary.txt

Name: RemoveWhiteSpc1.py
Description: Removes the whitespace and formats the file that contains the all mimulus protein annotation sequences. 
Input: MguttatusSeq.fasta
Output:  MguttatusStrp.fasta 

Name: Format1.py 
Description: Adds a star after each sequence to fomrat the file. 
Input: MguttatusStrp.fasta 
Output: MguttatusFmt.fasta 

Name: GetFullSeqs.py
Description: Writes full sequences from mimulus genome to the output file given a list of full fasta IDs 
Input: MimUGTPrimary.txt, MguttatusFmt.fasta
Output: Mim.UGT.v1.fasta 

# Curation 1 - Curate for PSPG completeness                                            
Name: curatePspg.sh
Description: curates sequences based on the PSPG conserved motif completeness
Files: 
pspgBox.py, parsePrimary2.py,RemoveWhiteSpc.py, GetFullSeqsPSPG.py

Name: pspgBox.py
Description: For annotations that have a full PSPG box,  writes the IDs to a new file.
Input: MimUGTs.sto 
Output: PspgID.txt, "fullPSPG.txt" 

Name: parsePrimary2.py 
Description: Parses through the "PspgID.txt" to write fasta IDs that refer only to primary annotations to the output file. 
Input: PspgIDUniq.txt
Outputs: PspgIDPrim.txt

########take out Name: CheckSubset.py
Description: checks if the PSPGID.py ids are all contained in the Output: Mim.UGT.v1.fasta
Inputs:PspgIDPrimary.txt, MimUGTPrimary.txt
Output: Output printed to screen or saved into jobmanager execution file.
"The sequences identitfied to encode a PSPG box in  PspgID.txt is a subset of genes that are UGTs from MimUGTPrimary.txt." 

Name: RemoveWhiteSpc2.py
Description: Removes the whitespace and formats the file that contains the all mimulus protein annotation sequences. 
Input: Mim.UGT.v1.fasta 
Output: Mim.UGT.v1Strp.fasta 

Name: Format2.py 
Description: Adds a star after each sequence to format the file. 
Input:  Mim.UGT.v1Strp.fasta 
Output: Mim.UGT.v1Fmt.fasta 

Name: GetFullSeqsPSPG.py *update name* 
Description: Writes full sequences from "PspgID.txt" to "Mim.UGT.v2.fasta" which are the sequences that encode a full PSPG box. 
Input: infile2 = PspgIDPrim.txt, Mim.UGT.v1Fmt.fasta 
Output: Mim.UGT.v2.fasta
 
# Curation 2 - Curate for sequence Size                   
Name: CurateSize.sh         
Description: Curates Mim.UGT.V2.fasta based on length of sequence 
Files: strpSeqs.py, GetSize.py

Name: RemoveWhiteSpc3.py
Description: Removes the white space from the sequences 
Input: Mim.UGT.v2.fasta
Output: Mim.UGT.v2.Strp.fasta

Name: Format3.py 
Description: Adds a star after each sequence to format the file. 
Input:  Mim.UGT.v2.Strp.fasta 
Output: Mim.UGT.v2.Fmt.fasta 

Name: GetFullSeqSize.py *update name(in putty)* 
Description:  For annotations that fall within this threshold between 200 and 550 amino acids long, it writes the sequence to a new file
Input: Mim.UGT.v2.Fmt.fasta    not: Mim.UGT.v2.Strp.fasta
Output:  Mim.UGT.v3.fasta
comments: Upper bound was origanly 500 but was then increased to 550.  

#need something that gets the ids of the new subset 

# Curation3 -  Expressed Mimulus UGTs               
Name: curateExpressed.sh
Description: curates Mim.UGT.v3 based on the mimulus gutattus UGTs that are expressed. 
Input: expressedAnnot.txt
Output: expressedAnnotuniq.txt - gets the unique fasta IDs, MimUGTExpFastaID.txt - full fasta IDs of expressed genes 
Files: expressedAnnot.txt, parsePrimary.py, GetFullSeqsExpsd.py

Name: expressedAnnot.txt
Description: contains the IDs of the Mimulus UGT annotations that are associated with expressed genes. 
Notes: (from heatmap)

Name: expressedAnnotuniq.txt 
Description: contains the IDs of the Mimulus UGT annotations that are associated with expressed genes that are unique. 

Name: parsePrimary3.py
Infile2 = MimUGTExpFastaID.txt
Outfile2 = MimUGTPrimary2.txt

Name: RemoveWhiteSpc4.py
Description: Removes the white space from the sequences 
Input: Mim.UGT.v3.fasta
Output: Mim.UGT.v3.Strp.fasta

Name: Format4.py 
Description: Adds a star after each sequence to fomrat the file. 
Input:  Mim.UGT.v3.Strp.fasta 
Output: Mim.UGT.v3.Fmt.fasta 

Name: GetFullSeqsExpsd.py
infile4 =  MimUGTPrimary2.txt  Mim.UGT.v3.Fmt.fasta      not: Mim.UGT.v3.format.fasta, 
outfile4 = Mim.UGT.v4.fasta
