# Test subclassing built-in str

class S(str):
    pass

s = S('hello')
print(s == 'hello')
print(s == 'hello')
print(s == 'Hello')
print(s == 'Hello')
