# Uses python3
def pisano_period(m):
    f = [0, 1]
    x = 2
    while True:
        f.append(f[x - 1] + f[x - 2])
        if f[x] % m == 1:
            if f[x - 1] % m == 0:
                return x - 1
                break
        x += 1


def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    else:
        n = n % pisano_period(m)
        f = [0 ,1]
        for x in range(2, n + 1):
            f.append(f[x - 1] + f[x - 2])
        return f[n] % m
        
if __name__ == '__main__':
    n, m = input().split()
    print(get_fibonacci_huge(int(n), int(m)))

