import os


def main():

    with open(os.path.join(os.getcwd(), '6_rosalind_hamm.txt')) as f:
        content = f.readlines()
        sequence_1 = content[0].strip()
        sequence_2 = content[1].strip()

    result, diff = compare_sequences(sequence_1, sequence_2, miss=' ', hit='|')

    print('Number of differences: {}'.format(diff))
    print(sequence_1)
    print(result)
    print(sequence_2)


def compare_sequences(sequence_1, sequence_2, miss, hit):

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