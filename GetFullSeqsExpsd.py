#Name: GetFullSeqsExpsd.py
#input: infile4 = Mim.UGT.v3.format.fasta, MimUGTPrimary2.txt
#output: outfile4 = Mim.UGT.v4.fasta

def main():
    infile =  "Mim.UGT.v3.Fmt.fasta"
    IDinfile = "MimUGTPrimary2.txt" 
    outfile = "Mim.UGT.v4.fasta"
    found = 0;
    with open(infile)as input:
        print("working on getting the sequences in the in a fasta file!........")
        for line in input: 
           # if found == 139:
                #print ("All seqs found", found )
                #break
                
            if line[0] == ">":
                
                #check that fasta name if its in the mim file  
                
                #open the mim file and readlines 
                #this puts it into a list 
                mimFile = open(IDinfile)
                mimList = mimFile.readlines()
                mimFile.close()
                
                #extract the name from the line
                out = open(outfile, "a")
                for lineM in mimList:
                #print(line[10], lineM[10])
                    
                # if lineM in line:
               
                    if line[7] == lineM[7] and line[8]== lineM[8] and line[9] == lineM[9] and line[10]== lineM[10] and line[11]== lineM[11] and line[12]== lineM[12] and line[13] == lineM[13] and line[14] == lineM[14]: 
                        found += 1
                        
                    
                        i = 0
                        out.write("\n")
                        while line[i] != "*":
                            out.write(line[i])
                            if line[i-4] == "=" and line[i-3]== "v" and line[i-2]== "2" and  line[i-1]== "." and line[i] == "0":
                                out.write("\n")
                            i += 1
                    
main()
    
