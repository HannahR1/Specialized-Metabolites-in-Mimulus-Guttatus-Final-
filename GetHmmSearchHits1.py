#Name: GetHmmSearchHits.py
#Description: get the names of the mimulus genes that was a hit
#Input: MimUGTs.sto
#Output: MimUGTIDs.txt


def main():
    inFileName = "MimUGTs.sto"
    outFileName = "MimUGTIDs.txt"
    #infile = open(inFileName)
    #lines = infile.readlines()
    #infileName.close

    print ("writing to output file ..." )

    outfile = open(outFileName, "a")
    with open( inFileName)as input:
        linnum = 0;
        #linenum = 0
        for line in input:
            linnum+=1
            if line[0] == "M":
                i = 0
                #write the characters in order until it reaches a " "
                #while line[i] < 42:
                while (i < 14):
                   
                    outfile.write(line[i])
                    i+=1
                outfile.write("\n")
main()




