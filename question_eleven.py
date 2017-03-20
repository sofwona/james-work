print("Please enter the word to be tested.")
w = input()

if w == w[::-1]:
	print("{} is a palindrome.".format(w))
else:
	print("{} is not a palindrome.".format(w))

# Note that the program factors in spaces as elements of the string.