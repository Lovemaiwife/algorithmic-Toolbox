def lcm(number1, number2):
	orig_n1 = number1
	orig_n2 = number2
	while True:
		remainder = number1 % number2
		if remainder == 0:
			break
		else:
			number1 = number2
			number2 = remainder
	print(int(orig_n1 * orig_n2 / number2))
n = input().split()
number1 = max(int(n[0]), int(n[1]))
number2 = min(int(n[0]), int(n[1]))
lcm(number1, number2)
