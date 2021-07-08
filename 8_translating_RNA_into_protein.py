""" Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

    Return: The protein string encoded by s. """

from Bio.Seq import Seq

def main():

    dataset = input('Path to dataset: ')

    with open(dataset, 'r') as f:
        sequence = f.read()

    mrna_seq = Seq(sequence)
    protein_seq = mrna_seq.translate()

    print(protein_seq)


if __name__ == '__main__':
    main()