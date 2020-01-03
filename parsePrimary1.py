def main():

    infile1 = "MimUGTFastaID.txt"
    outfile1 = "MimUGTPrimary.txt"
    print ("These fasta IDs will be removed: ") 
    with open(infile1)as input:
        for line in input:
            if line[14] == "1":
                #write that line to the new file
                outfile = open(outfile1, "a")
                outfile.write(line)
            else:
                #prints out the fasta IDs that will be removed
                print (line)
                

main()
