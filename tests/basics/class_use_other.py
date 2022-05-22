# check that we can use an instance of B in a method of A

class A:
    def store(self, b):
        self.value = b

class B:
    pass

b = B()
A.store(b, 1)
print(b.value)
