def main():
    #read in the file and check the _th character
#if it is not a "1" then remove from the file output
    infile = "PspgIDUniq.txt"
    outfile = "PspgIDPrim.txt"
    outfile = open(outfile, "a")
    print ("These fasta IDs will be removed: ")
    with open(infile)as input:
        for line in input:
            if line[14] == "1":
                #write that line to the new file
                
                outfile.write(line)
            else:
                print (line)


main()



