""" Given: Six nonnegative integers, each of which does not exceed 20,000.
    The integers correspond to the number of couples in a population possessing each
    genotype pairing for a given factor. In order, the six given integers represent the number of
    couples having the following genotypes:

    AA-AA
    AA-Aa
    AA-aa
    Aa-Aa
    Aa-aa
    aa-aa

    Return: The expected number of offspring displaying the dominant phenotype in the next generation,
    under the assumption that every couple has exactly two offspring. """

def main():

    dataset = input('Path to dataset: ')

    p = probability(dataset)

    print(p)


def probability(dataset):

    """ Calculates probability that offspring will have a dominant allele given the number of
        pairs carrying certain genotype """

    # Get numbers of pairs
    with open(dataset, 'r') as f:
        pair_num = f.readline().split()

    # Calculate how much offspring with dominant alleles each pair gives
    AAAA = int(pair_num[0]) * 2 * 1
    AAAa = int(pair_num[1]) * 2 * 1
    AAaa = int(pair_num[2]) * 2 * 1
    AaAa = int(pair_num[3]) * 2 * 0.75
    Aaaa = int(pair_num[4]) * 2 * 0.5
    aaaa = int(pair_num[5]) * 2 * 0

    return AAAA + AAaa + AAAa + aaaa + AaAa + Aaaa


if __name__ == '__main__':
    main()