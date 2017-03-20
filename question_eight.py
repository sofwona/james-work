print("Please give me a number")
n = eval(input())

sum = 0
for x in range(1, n) or range(n, 1):
	sum += x

if n > 0:
	sum += n
else:
	sum += 1


print(sum)

# The code accepts both positive and negative values of n