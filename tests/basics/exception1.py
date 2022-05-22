# test basic properties of exceptions

print(repr(IndexError()))
print(IndexError())

print(IndexError("foo"))

a = IndexError(1, "test", [100, 200])
print(repr(a))
print(a)
print(a.args)

s = StopIteration()
print(s.value)
s = StopIteration(1, 2, 3)
print(s.value)

print(OSError().errno)
print(OSError(1, "msg").errno)
