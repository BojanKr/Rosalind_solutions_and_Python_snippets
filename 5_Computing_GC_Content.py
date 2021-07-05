import os
from Bio import SeqIO

def main():

    gc_count_dict = {}

    # Find GC count for each sequence
    for sequence in SeqIO.parse(os.path.join(os.getcwd(), '5_rosalind_gc.txt'), 'fasta'):
        c_count = sequence.seq.count('C')
        g_count = sequence.seq.count('G')
        gc_count = ((c_count + g_count)/len(sequence))*100
        gc_count_dict[sequence.id] = gc_count

    # Get the highest GC count
    highest_gc = max(gc_count_dict, key=gc_count_dict.get)

    print(highest_gc, gc_count_dict[highest_gc])

if __name__ == '__main__':
    main()