# basic dictionary

d = {}
print(d)
d[2] = 123
print(d)
d = {1: 2, 3: 3}
print(len(d), d[1], d[3])
d[1] = 0
print(len(d), d[1], d[3])
print(str(d) in {'{1: 0, 3: 3}', '{3: 3, 1: 0}'})

for x in range(1, 100):
    d[x] = x
print(d[50])

# equality operator on dicts of different size
print({} == {1:1})

# equality operator on dicts of same size but with different keys
print({1:1} == {2:1})

# 0 replacing False's item
d = {False: 'false', 0: 'zero'}
print(d)

# False replacing 0's item
d = {0: 'zero', False: 'false'}
print(d)

# 1 replacing True's item
d = {True: 'true', 1: 'one'}
print(d)

# True replacing 1's item
d = {1: 'one', True: 'true'}
print(d)

# mixed bools and integers
d = {False:10, True:11, 2:12}
print(d[0], d[1], d[2])

# value not found
try:
    {}[0]
except KeyError as er:
    print('KeyError', er, er.args)

# unsupported unary op
try:
    +{}
except TypeError:
    print('TypeError')

# unsupported binary op
try:
    {} + {}
except TypeError:
    print('TypeError')
