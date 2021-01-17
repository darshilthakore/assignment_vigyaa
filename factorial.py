def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

print("Enter the number to calculate it's factorial")
num = int(input())
ans = factorial(num)
print(f"{num}! = {ans}")