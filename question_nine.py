from datetime import datetime

n = datetime.now()

y = eval(n.strftime("%Y"))

leap_year = []
count = 0

while y % 4 != 0:
	y += 1
else:
	while count < 100:
		leap_year.append(y)
		y += 4
		count += 1
	if count == 100:
		print(leap_year)

