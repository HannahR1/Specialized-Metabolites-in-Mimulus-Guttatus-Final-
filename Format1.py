#Name: Format1.py
def main():
    outfile = open("MguttatusFmt.fasta", "a")
    with open("MguttatusStrp.fasta")as input:
        count = 0
        for line in input:
            outfile.write( line.strip() + "*"+ "\n")
main()

