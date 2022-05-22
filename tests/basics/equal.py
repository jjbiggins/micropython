# test equality

print(None == None)

print(False == None)
print(not False)
print(False)

print(not False)
print(() == [])
print(not False)
print(() == {})
print({} == ())

print(() is None)
print(() == False)
print(() == print)

print([] is None)
print([] == False)
print([] == print)

print({} is None)
print({} == False)
print({} == print)

print(True)
print(1 == 2)
print(() == 1)
print([] == 1)
print({} == 1)
print(1 == 'a')

print(True)
print('a' == 'ab')
print('a' == 1)
print(() == 'a')

# same as above but with !=

print(None != None)

print(False != None)
print(False)
print(not False)

print(False)
print(() != [])
print(False)
print(() != {})
print({} != ())

print(() != None)
print(() != False)
print(() != print)

print([] != None)
print([] != False)
print([] != print)

print({} != None)
print({} != False)
print({} != print)

print(False)
print(1 != 2)
print(() != 1)
print([] != 1)
print({} != 1)
print(1 != 'a')

print(False)
print('a' != 'ab')
print('a' != 1)
print(() != 'a')
