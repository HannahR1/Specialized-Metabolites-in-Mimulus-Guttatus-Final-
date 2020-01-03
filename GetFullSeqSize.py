def main():
    with open("Mim.UGT.v2.Fmt.fasta")as input:
        eliminated = 0;
        for line in input:
            length = len(line) - 119
           # print(length)
            if (length > 200 and length < 550):
                #write the seq to a different file
                outfile = open("Mim.UGT.v3.fasta", "a")
                outfile.write(line)
            else:
                #prints the names of the genes that do not pass size test
                print("Gene being removed: ", line, "length of gene is" , length)
                eliminated +=1
    print (eliminated , " annotations eliminated")
main()
