def max_pairwise_product(numbers):
    n = len(numbers)
    max_i = 0
    max_i_idx = 0
    for i in range(n):
        if numbers[i] > max_i:
            max_i = numbers[i]
            max_i_idx = i
    del numbers[max_i_idx]
    max_j = 0
    for j in range(n - 1):
        if numbers[j] > max_j:
            max_j = numbers[j]

    return max_i * max_j

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
