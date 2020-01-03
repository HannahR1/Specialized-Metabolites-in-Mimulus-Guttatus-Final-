def main():
    outfile = open("Mim.UGT.v2.Strp.fasta", "a")
    with open("Mim.UGT.v2.fasta")as input:
        count = 0
        for line in input:
            #print("works") 
            if line[0] == ">":
                if count != 0:
                    outfile.write("\n")


             
                outfile.write(line.strip())
             
            else:
             
                outfile.write(line.strip())
             
            count += 1

main()
