for n in range(2, 11):
    for x in range(2, n):
        print(n, x)
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
        break