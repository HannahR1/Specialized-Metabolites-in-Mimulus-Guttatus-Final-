#Name:GetFullSeqsPSPG.py

def main():
    found = 0;
    with open("Mim.UGT.v1Fmt.fasta")as input:
        print("working on getting the sequences in the in a fasta file!........")
        for line in input: 
            #if found == 139:
                
            if line[0] == ">":
                #check that fasta name if its in the mim file  
                #open the mim file and readlines 
                #this puts it into a list 
                mimFile = open("PspgIDPrim.txt")
                mimList = mimFile.readlines()
                mimFile.close()
               
                #extract the name from the line
                outfile = open("Mim.UGT.v2.fasta", "a")
                for lineM in mimList:
               
                    if line[7] == lineM[7] and line[8]== lineM[8] and line[9] == lineM[9] and line[10]== lineM[10] and line[11]== lineM[11] and line[12]== lineM[12] and line[13] == lineM[13] and line[14] == lineM[14]: 
                        found += 1
                        #write the name and sequence to the new file
                        #open the new file for appending 
                        i = 0
                        outfile.write("\n")
                        while line[i] != "*":
                            outfile.write(line[i])
                            if line[i-4] == "=" and line[i-3]== "v" and line[i-2]== "2" and  line[i-1]== "." and line[i] == "0":
                                outfile.write("\n")
                            i += 1
                    
main()
    
