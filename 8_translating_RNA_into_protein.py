""" Given: An RNA string s

corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s. """

import os
from Bio.Seq import Seq

def main():

    with open(os.path.join(os.getcwd(), '8_rosalind_prot.txt')) as f:
        sequence = f.read()

    mrna_seq = Seq(sequence)
    protein_seq = mrna_seq.translate()

    print(protein_seq)


if __name__ == '__main__':
    main()