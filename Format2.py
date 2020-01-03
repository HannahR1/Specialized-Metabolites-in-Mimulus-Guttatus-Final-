#Name: Format2.py
def main():
    outfile = open( "Mim.UGT.v1Fmt.fasta", "a")
    with open( "Mim.UGT.v1Strp.fasta")as input:
        count = 0
        for line in input:
            outfile.write( line.strip() + "*"+ "\n")

main()
