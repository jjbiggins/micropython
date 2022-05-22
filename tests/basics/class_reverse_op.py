class A:

    def __init__(self, v):
        self.v = v

    def __add__(self, o):
        return A(self.v + o.v) if isinstance(o, A) else A(self.v + o)

    def __radd__(self, o):
        return A(self.v + o)

    def __repr__(self):
        return f"A({self.v})"

print(A(3) + 1)
print(2 + A(5))
