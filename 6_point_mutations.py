""" Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

    Return: The Hamming distance dH(s,t). """


def main():

    dataset = input('Path to dataset: ')

    with open(dataset, 'r') as f:
        content = f.readlines()
        sequence_1 = content[0].strip()
        sequence_2 = content[1].strip()

    result, diff = compare_sequences(sequence_1, sequence_2, miss=' ', hit='|')

    print('Number of differences: {}'.format(diff))
    print(sequence_1)
    print(result)
    print(sequence_2)


def compare_sequences(sequence_1, sequence_2, miss, hit):

    """ Compares two sequences to find the Hamming distance """

    result = ''
    diff = 0

    for n1,n2 in zip(sequence_1, sequence_2):
        if n1 == n2:
            result += hit
        else:
            result += miss
            diff += 1

    return result, diff


if __name__ == '__main__':
    main()