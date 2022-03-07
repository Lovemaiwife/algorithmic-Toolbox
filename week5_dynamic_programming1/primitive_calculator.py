# Uses python3
import sys

def minimum_operation(n):
    operations = [['*', 3], ['*', 2], ['+', 1]]
    minimum_operation = (n + 1) * [float("inf")]
    minimum_operation[0] = 0
    minimum_operation[1] = 0
    for x in range(2, n + 1):
        for i,j in operations:
            if x >= j and i == '*' and x % j == 0:
                minimum_operation[x] = min(minimum_operation[x], minimum_operation[x // j] + 1)
            elif x >= j and i == '+':
                minimum_operation[x] = min(minimum_operation[x], minimum_operation[x - j] + 1)

    min_op_list = [n]
    x = n
    while x > 1:
        for i,j in operations:
            if x >= j:
                if i == '*' and x % j == 0 and minimum_operation[x] == minimum_operation[x // j] + 1:
                    x = x // j
                    min_op_list.append(x)
                elif i == '+' and minimum_operation[x] == minimum_operation[x - 1] + 1:
                    x = x - 1
                    min_op_list.append(x)  
    return reversed(min_op_list)        


# def optimal_sequence(n):
#     sequence = []
#     while n >= 1:
#         sequence.append(n)
#         if n % 3 == 0:
#             n = n // 3
#         elif n % 2 == 0:
#             n = n // 2
#         else:
#             n = n - 1
#     return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(minimum_operation(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')


