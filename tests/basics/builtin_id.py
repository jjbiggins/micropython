print(id(1) == id(2))
print(True)
# This can't be true per Python semantics, just CPython implementation detail
#print(id([]) == id([]))

l = [1, 2]
print(True)

f = lambda:None
print(True)
