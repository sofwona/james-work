print("Hello, what is your name?")
n = input()
print("What is your age?")
a = eval(input())

from datetime import datetime

k= datetime.now()
wy = eval(k.strftime("%Y")) 

val = wy-a

print ("Hello {}, you were born in {}".format(n, val))

# The code is flawed. Since the only data used to calculate age is year of birth, the algorithm assumes that the users age has increased in the current year. That is to say, the code will only be accurate on December 31st at 11:59pm.