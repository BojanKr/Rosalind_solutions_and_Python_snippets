""" Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
    k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

    Return: The probability that two randomly selected mating organisms will produce an individual possessing a
    dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate. """


def main():

    dataset = input('Path to dataset: ')

    with open(dataset, 'r') as f:
        content = f.read().split()
        k = int(content[0])
        m = int(content[1])
        n = int(content[2])

    prob = probability(k, m, n)

    print('Probability is {}'.format(str(prob)))


def probability(k, m, n):

    total_sum = k + m +n

    p_kxk = k/total_sum * (k - 1)/(total_sum - 1)
    p_kxm = (k/total_sum * m/(total_sum - 1)) * 2
    p_kxn = (k/total_sum * n/(total_sum - 1)) * 2
    p_mxm = m/total_sum * (m - 1)/(total_sum -1) * 3/4
    p_mxn = (m/total_sum * n/(total_sum - 1)) * 1/2 * 2

    p = p_kxk + p_kxm + p_kxn + p_mxm + p_mxn

    return p


if __name__ == '__main__':
    main()