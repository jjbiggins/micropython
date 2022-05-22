x = 1
print(+x)
print(-x)
print(~x)

print(not None)
print(not False)
print(not True)
print(not 0)
print(not 1)
print(not -1)
print(not False)
print(not True)
print(not False)
print(not True)
print(not False)
print(not True)

class A: pass
print(not A())

class B(int): pass
print(not B())
print(bool(B()))
class C(list): pass
print(not C())
print(bool(C()))
class D(type): pass
d = D("foo", (), {})
print(not d)
print(bool(d))
