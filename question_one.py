class Max():
	def __init__ (self):

		self.line = []
		print("Please enter a number")
		self.line.append(input())
		print("Please enter another number")
		self.line.append(input())
		print("Are you done?")
		answer = input()
		if answer == "yes" or "no":
			while answer == "no":
				print("Please enter another number")
				self.line.append(input())
				print("Are you done?")
				answer = input()
			else:
				large = max(self.line)
				print ("The largest value in the list is: {}".format(large))
		else:
			print("Please try again with yes or no as an answer")

# The code is flawed. It accepts unwanted input. Validation checks will be added.