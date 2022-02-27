# n = int(input())
# numbers = [int(x) for x in input().split()]



def max_pairwise_product(numbers):
	n = len(numbers)
	max_product = 0
	for first in range(n):
	    for second in range(first + 1, n):
	        max_product = max(max_product,
	            numbers[first] * numbers[second])

	return max_product
def pairwise_product_self(numbers):
	n = len(numbers)
	max_i = 0
	for i in range(n):
		if numbers[i] > max_i:
			max_i = numbers[i]
			global max_i_idx 
			max_i_idx = i

	del numbers[max_i_idx]
	max_j = 0
	for j in range(n - 1):
		if numbers[j] > max_j:
			max_j = numbers[j]

	return max_i * max_j



import random
while True:
	n = random.randint(2, 1500)
	print(n)
	numbers = list(range(n))
# print(numbers)
	if max_pairwise_product(numbers) == pairwise_product_self(numbers):
		print('OK')
	else:
		print('wrong', n)
		break
# main()



