# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    else:
        f = [0, 1]
        for x in range(2, n + 1):
            f.append(f[x - 1] % 10 + f[x - 2] % 10)
        return f[n] % 10

if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
