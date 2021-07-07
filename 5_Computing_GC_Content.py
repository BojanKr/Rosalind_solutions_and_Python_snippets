""" Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

    Return: The ID of the string having the highest GC-content,
    followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all
    decimal answers unless otherwise stated; please see the note on absolute error below. """

from Bio import SeqIO

def main():

    dataset = input('Path to dataset: ')

    gc_count = get_gc_count(dataset)

    # Get the highest GC count
    highest_gc = max(gc_count, key=gc_count.get)

    print(gc_count)

    print(highest_gc, gc_count[highest_gc])


def get_gc_count(dataset):

    """ Finds GC count for each sequence """

    gc_count_dict = {}

    for sequence in SeqIO.parse(dataset, 'fasta'):
        c_count = sequence.seq.count('C')
        g_count = sequence.seq.count('G')
        gc_count = ((c_count + g_count)/len(sequence))*100
        gc_count_dict[sequence.id] = gc_count


    return gc_count_dict


if __name__ == '__main__':
    main()