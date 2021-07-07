""" Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

    Return: The adjacency list corresponding to O3. You may return edges in any order. """

from Bio import SeqIO

def main():

    dataset = input('Path to dataset: ')

    # k is the size of sufix/prefix omparted between two sequences
    k = input('Enter k: ')

    g = overlap_graph(dataset, k)

    for pair in g:
        print(pair)


def overlap_graph(dataset, k):

    """ Finds node pairs of overlap graph (this is a directed graph) """

    # List to store connected pairs
    pairs = []

    with open(dataset, 'r') as f:
        records =list(SeqIO.parse(f, 'fasta'))

    # First direction
    for seq in records:
        for i in range(len(records)):
            if seq.id != records[i].id:
                if seq.seq[-int(k):] == records[i].seq[0:int(k)]:
                    pairs.append(seq.id + ' ' + records[i].id)

    return pairs

if __name__ == '__main__':
    main()
