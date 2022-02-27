# Uses python3
import sys

def get_change(m):
    coin_10 = m // 10
    coin_5 = (m - 10 * coin_10) // 5
    coin_1 = (m - 10 * coin_10 - 5 * coin_5)
    m = coin_10 + coin_5 + coin_1
    return m


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
