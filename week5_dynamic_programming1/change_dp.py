# Uses python3
import sys

def get_change(m):
    #write your code here
    denominations = [1, 3, 4]
    min_coins = (1 + m) * [float("inf")]
    min_coins[0] = 0
    for i in range(1, m + 1):
        for d in denominations:
            if i >= d:
                min_coins[i] = min(min_coins[i], min_coins[i - d] + 1)

    return min_coins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))


