"""  Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

     Return: A longest common substring of the collection.
     (If multiple solutions exist, you may return any single solution.) """

from Bio import SeqIO


def main():

    dataset = input('Path to dataset: ')

    m = shared_motif(dataset)

    print(max(m, key=len))


def shared_motif(dataset):

    """ Finds the longest shared motif for all sequences in the dataset """

    seq_list = []

    # Parse the dataset
    with open(dataset, 'r') as f:
        for s in SeqIO.parse(f, 'fasta'):
            seq_list.append(str(s.seq))

    motif_list = []

    # Create a list of all possible motifs for the given sequence
    motifs = [seq_list[0][i: j] for i in range(len(seq_list[0])) for j in range(i + 1, len(seq_list[0]) + 1)]
    for el in motifs:
        if len(el) < 3:
            motifs.remove(el)

    for m in motifs:
        if all(m in s for s in seq_list):
            motif_list.append(m)

    return motif_list


if __name__ == '__main__':
    main()

