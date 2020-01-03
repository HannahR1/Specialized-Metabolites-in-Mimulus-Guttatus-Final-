#Name: RemoveWhiteSpc1.py
def main():
    outfile = open("MguttatusStrp.fasta", "a")
    with open("MguttatusSeq.fasta")as input:
        count = 0
        for line in input:

            if line[0] == ">":
                if count != 0:
                    outfile.write("\n")

                outfile.write(line.strip())

            else:
                outfile.write(line.strip())

            count += 1

main()
