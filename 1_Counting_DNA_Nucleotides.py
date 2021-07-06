""" Given: A DNA string s of length at most 1000 nt.

    Return: Four integers (separated by spaces) counting the respective number of times that
    the symbols 'A', 'C', 'G', and 'T' occur in s. """

def main():

    seq = input('Input sequence: ')

    count = count_nucleotides(sequence=seq)
    print(count)

def count_nucleotides(sequence):

    nucleotides = ['A', 'C', 'G', 'T']
    c = {}

    for nucleotide in nucleotides:
        nucl_count = sequence.count(nucleotide)

        c[nucleotide] = str(nucl_count)

    return c


if __name__ == '__main__':
    main()