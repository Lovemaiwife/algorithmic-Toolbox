def gcd(number1, number2):
	while True:
		remainder = number1 % number2
		if remainder == 0:
			break
		else:
			number1 = number2
			number2 = remainder
	print(number2)
n = input().split()
number1 = max(int(n[0]), int(n[1]))
number2 = min(int(n[0]), int(n[1]))
gcd(number1, number2)
