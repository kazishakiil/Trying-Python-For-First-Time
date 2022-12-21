thistuple = ("apple", "banana", "cherry")
print(thistuple)
#accessss korlam ok
print(thistuple[1])
#remove
y=list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(y)
