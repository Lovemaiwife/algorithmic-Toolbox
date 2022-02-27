# Uses python3
def get_fibonacci_huge(n):
    if n <= 1:
        return n

    else:
        n = n % 60
        if n >= 2:
            f = [0 ,1]
            for x in range(2, n + 1):
                f.append(f[x - 1] + f[x - 2])
            return (f[n] * (f[n] + f[n - 1])) % 10
        elif n == 1:
            return 1
        else:
            return 0

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_huge(n))
