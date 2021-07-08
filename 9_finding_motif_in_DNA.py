""" Given: Two DNA strings s and t
    (each of length at most 1 kbp).

    Return: All locations of t
    as a substring of s. """

import re

def main():

    dataset = input('Path to dataset: ')

    with open(dataset, 'r') as f:
        content = f.readlines()
        dna = content[0].strip()
        motif = content[1].strip()

    # Create a list with motif positions (add 1 to each position to take into account 0 start)
    motif_positions = [x + 1 for x in motif_scan(dna_seq=dna, motif=motif)]

    print(' '.join(str(num) for num in motif_positions))


def motif_scan(dna_seq, motif):

    # Search for overlapping motifs
    positions = [motif.start() for motif in re.finditer(f'(?={motif})', dna_seq)]

    return positions


if __name__ == '__main__':
    main()