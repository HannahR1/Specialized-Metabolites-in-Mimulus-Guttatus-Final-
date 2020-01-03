def main():
    count = 0
    countL = 0 
    name = "Mim.UGT.v1.fasta"
    with open(name)as input:
        for line in input:
            countL +=1
#            print (line[0])
            if line[0] == ">":
                count += 1
    print ("there are " , count, " sequnences", "on", countL, "lines in filename: ", name)

main()
