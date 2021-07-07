""" Given: Positive integers n≤100 and m≤20.

    Return: The total number of pairs of rabbits that will remain after the
    n-th month if all rabbits live for m months. """

def main():

    n = input('Enter n: ')
    m = input('Enter m: ')
    
    fn = mortal_fibonacci(n,m)

    print(fn)
    print(fn[int(n)-1])


def mortal_fibonacci(n,m):

    """ Calculates the number of pairs after n generations with m life span """

    f = [1, 1]

    # Before exceeding life span just a simple Fibonacci sequence
    for num in range(int(n) - 1):
        if len(f) < int(m):
            F = f[num + 1] + f[num]
            f.append(F)
        # Take into account mortality
        else:
            s = []
            for i in range(int(m)-1):
                s.append(f[num - i])
            F = sum(s)
            f.append(F)

    return f


if __name__ == '__main__':
    main()