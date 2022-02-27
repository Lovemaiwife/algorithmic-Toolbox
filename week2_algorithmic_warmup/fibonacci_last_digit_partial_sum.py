# Uses python3
def get_fibonacci_sum_mod(n):
    if n <= 1:
        return n

    else:
        mod = n % 60 #pisano period of 10 pi(10) = 60
        if mod == 0: #this will cause for loop to have range(2,1)
            return 0
        else:
            current = 1
            previous = 0
            total = 1
            for x in range(2, mod + 1):
                new = (current + previous) % 10
                total = (total + new)
                previous = current
                current = new
            return total

if __name__ == '__main__':
    m, n = input().split()
    if int(m) == 0: #this will cause get_fibonacci_sum_mod(-1)
        print((get_fibonacci_sum_mod(int(n)) - get_fibonacci_sum_mod(int(m))) % 10)
    else:
        print((get_fibonacci_sum_mod(int(n)) - get_fibonacci_sum_mod(int(m) - 1)) % 10)