""" Given: Positive integers n ≤ 40 and k ≤ 5.

    Return: The total number of rabbit pairs that will be present after n months,
    if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a
    litter of k rabbit pairs (instead of only 1 pair). """

def main():

    n = input('Enter n: ')
    k = input('Enter k: ')

    f = [1, 1]

    for num in range(int(n)-1):
        F = f[num + 1] + f[num]*int(k)
        f.append(F)

    print(f[int(n)-1])


if __name__ == '__main__':
    main()