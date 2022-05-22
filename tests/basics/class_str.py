class C1:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"str<C1 {self.value}>"

class C2:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"repr<C2 {self.value}>"

class C3:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"str<C3 {self.value}>"

    def __repr__(self):
        return f"repr<C3 {self.value}>"

c1 = C1(1)
print(c1)

c2 = C2(2)
print(c2)

s11 = str(c1)
print(s11)
# This will use builtin repr(), which uses id(), which is of course different
# between CPython and MicroPython
s12 = repr(c1)
print("C1 object at" in s12)

s21 = str(c2)
print(s21)
s22 = repr(c2)
print(s22)

c3 = C3(1)
print(c3)
