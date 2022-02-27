# Uses python3
def calc_fib(n):
    if n <= 1:
        return n

    else:
        f = [0, 1]
        for x in range(2, n + 1):
            f.append(f[x - 1] + f[x - 2])
        return f[n]
n = int(input())
print(calc_fib(n))
