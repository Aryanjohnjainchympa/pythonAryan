#create
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#Access
print(thistuple[1])

#update
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#delete
del thistuple
print(thistuple)
