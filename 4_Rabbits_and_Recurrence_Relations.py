def fibonacci():

    n = 34
    k = 2

    f = [1, 1]

    for num in range(n-1):
        F = f[num + 1] + f[num]*k
        f.append(F)

    print(f)


fibonacci()