import os

def reverse_complement():

    with open(os.path.join(os.getcwd(), '3_rosalind_revc.txt')) as f:
        seq = f.readlines()[0]
        print(seq)
        reverse_complement_seq = ''

        reverse_seq = seq[::-1]
        print(reverse_seq)

        for nucleotide in reverse_seq:
            if nucleotide == 'A':
                reverse_complement_seq = reverse_complement_seq + 'T'
            elif nucleotide == 'C':
                reverse_complement_seq = reverse_complement_seq + 'G'
            elif nucleotide == 'G':
                reverse_complement_seq = reverse_complement_seq + 'C'
            elif nucleotide == 'T':
                reverse_complement_seq = reverse_complement_seq + 'A'

        print(reverse_complement_seq)

reverse_complement()
