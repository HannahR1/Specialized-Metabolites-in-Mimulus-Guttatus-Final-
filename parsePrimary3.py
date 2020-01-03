#Name: parsePrimary3.py
def main():

    infile ="MimUGTExpFastaID.txt"
    outfile = "MimUGTPrimary2.txt"

    print ("These fasta IDs will be removed: ")
    with open(infile)as input:
        for line in input:
            if line[14] == "1":
                #write that line to the new file
                outfile1 = open(outfile, "a")
                outfile1.write(line)
            else:
                print (line)


main()
