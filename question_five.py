class Sort():
	def __init__(self):

		print("Please input the list of words to be sorted. How many words do you intend to input? ")
		count = eval(input())
		if count > 0:
			counter = 0
			self.list = []
			print("Begin")
			while counter < count:
				counter += 1
				print("Please enter a word.")
				self.list.append(input())
			else:
				print("Your list is as follows: {}".format(sorted(self.list, key=str.lower)))
		else:
			print("Please give a number greater than zero.")