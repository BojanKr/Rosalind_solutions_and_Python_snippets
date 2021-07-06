""" Given: A DNA string s of length at most 1000 bp.

    Return: The reverse complement sc of s. """


def main():

    dataset = input('Path to dataset: ')

    with open(dataset, 'r') as f:
        seq = f.readlines()[0]

        reverse_seq = seq[::-1]

        reverse = reverse_complement(sequence=reverse_seq)
        print(reverse)


def reverse_complement(sequence):

    """ Finds the reverse complement of a given DNA sequence """

    reverse_complement_seq = ''

    for nucleotide in sequence:
        if nucleotide == 'A':
            reverse_complement_seq = reverse_complement_seq + 'T'
        elif nucleotide == 'C':
            reverse_complement_seq = reverse_complement_seq + 'G'
        elif nucleotide == 'G':
            reverse_complement_seq = reverse_complement_seq + 'C'
        elif nucleotide == 'T':
            reverse_complement_seq = reverse_complement_seq + 'A'

    return reverse_complement_seq


if __name__ == '__main__':
    main()
