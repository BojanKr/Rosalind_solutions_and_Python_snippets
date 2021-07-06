""" Given: A DNA string t having length at most 1000 nt.

    Return: The transcribed RNA string of t. """

def main():

    dataset = input('Path to dataset: ')

    with open(dataset, 'r') as f:
        dna_seq = f.readlines()[0]

        rna_sequence = transcribe(dna_sequence=dna_seq)
        print(rna_sequence)


def transcribe(dna_sequence):

    """ Transcribes DNA sequence into RNA sequence """

    rna_seq = ''

    for nucleotide in dna_sequence:
        if nucleotide is not 'T':
            rna_seq = rna_seq + nucleotide
        else:
            rna_seq = rna_seq + 'U'

    return rna_seq


if __name__ == '__main__':
    main()