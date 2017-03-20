q= ["apple", "banana", "mango"]
w= ["pear", "raspberry", "ginger"]

y=[]
y.extend(q)
y.extend(w)

print(sorted(y, key=str.lower))

# Since no input was specified I used my own.