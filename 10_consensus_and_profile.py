""" Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

    Return: A consensus string and profile matrix for the collection.
    (If several possible consensus strings exist, then you may return any one of them.) """

from Bio import SeqIO
import pandas as pd

def main():

    # Read the data
    dataset = input('Path to dataset: ')

    with open(dataset, 'r') as f:
        records = list(SeqIO.parse(f, 'fasta'))
        print(records[0].seq)

    # Get nucleotide frequency per position
    occurences = count_occurences(records)
    # Print resulting frequency per position in a readable manner
    for index,row in occurences.iterrows():
        print(index + ':', ' '.join(row.astype(str)))

    # Get consensus sequence form frequency
    consensus_sequence = consensus(occurences)
    print(consensus_sequence)


def count_occurences(records):

    """ Counts occurences of nucleotides in each position of the sequence.

        Returns a dataframe with counts. """

    nucleotides = {'A': [], 'C': [], 'G': [], 'T': []}

    for i in range(len(records[0].seq)):
        A = 0
        C = 0
        G = 0
        T = 0
        for j in range(len(records)):
            if records[j].seq[i] == 'A':
                A += 1
            elif records[j].seq[i] == 'C':
                C += 1
            elif records[j].seq[i] == 'G':
                G += 1
            else:
                T += 1


        nucleotides['A'].append(A)
        nucleotides['C'].append(C)
        nucleotides['G'].append(G)
        nucleotides['T'].append(T)

    df = pd.DataFrame(nucleotides.values(), index=nucleotides.keys())

    return df


def consensus(df):

    """ Writes a consesnus sequence based on nucleotide occurences in the sequence """

    i = 0
    consensus_seq = ''

    for column in df:
        highest = df[column].max()
        nucleotide = df.index[df[column] == highest].tolist()[0]

        consensus_seq = consensus_seq + nucleotide

    return consensus_seq


if __name__ == "__main__":
    main()