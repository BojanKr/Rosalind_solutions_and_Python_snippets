import os

def transcribe():

    with open(os.path.join(os.getcwd(), '2_rosalind_rna.txt')) as f:
        dna_seq = f.readlines()[0]
        print(dna_seq)
        rna_seq = ''

        for nucleotide in dna_seq:
            if nucleotide is not 'T':
                rna_seq = rna_seq + nucleotide
            else:
                rna_seq = rna_seq + 'U'

    print(rna_seq)

transcribe()