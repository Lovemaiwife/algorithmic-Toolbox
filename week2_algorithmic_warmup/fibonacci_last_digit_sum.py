# Uses python3




def get_fibonacci_low(m):
    if m <= 1:
        return m

    else:
        mod = m % 60 #pisano period of 10 pi(10) = 60
        if mod == 0: #(this will cause for loop to have range(2,1))
            return 0
        else:
            current = 1
            previous = 0
            total = 1
            for x in range(2, mod + 1):
                new = (current + previous) % 10
                total = (total + new) % 10 
                previous = current
                current = new
            return total

def get_fibonacci_high(n):
    if n <= 1:
        return n

    else:
        mod = n % 60 #pisano period of 10 pi(10) = 60
        if mod == 0: #(this will cause for loop to have range(2,1))
            return 0
        else:
            current = 1
            previous = 0
            total = 1
            for x in range(2, mod + 1):
                new = (current + previous) % 10
                total = (total + new) % 10 
                previous = current
                current = new
            return total

if __name__ == '__main__':
    m, n = input(),split()
    print(get_fibonacci_low(int(m) - 1) - get_fibonacci_high(int(n)))