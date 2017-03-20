class Divisible():
	def __init__ (self):


		print("Please enter the denominator of the division")
		self.denominator = eval(input())
		print("Please input the list of numerators of the division. How many numbers do you intend to input? ")
		count = eval(input())
		if count > 0:
			counter = 0
			self.div = []
			self.indiv = []
			print("Begin")
			while counter < count:
				counter += 1
				print("Enter a number.")
				self.numerator = eval(input())
				if self.numerator%self.denominator == 0:
					self.div.append(self.numerator)
				else:
					self.indiv.append(self.numerator)
			else:
				print("Numbers divisible by {} are {}".format(self.denominator,self.div))
				print("Numbers divisible by {} are {}".format(self.denominator,self.indiv))
		else:
			print("Please give a number greater than zero.")


