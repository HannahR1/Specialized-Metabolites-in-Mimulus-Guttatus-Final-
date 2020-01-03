#Name: Format3.py

def main():
    outfile = open("Mim.UGT.v2.Fmt.fasta", "a")
    with open("Mim.UGT.v2.Strp.fasta")as input:
        count = 0
        for line in input:
            #print (line)
            outfile.write( line.strip() + "*"+ "\n")

main()
