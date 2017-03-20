class Calculator():
	def __init__ (self):
		print("Enter a number")
		self.a= eval(input())
		print("Enter another number")
		self.b= eval(input())

	def sum(self):
		answer= self.a+self.b
		print(answer)
		return

	def diff(self):
		answer= self.a-self.b
		print(answer)
		return

	def mult(self):
		answer= self.a*self.b
		print(answer)
		return

	def div(self):
		answer= self.a/self.b
		print(answer)
		return

	def mod(self):
		answer= self.a%self.b
		print(answer)
		return