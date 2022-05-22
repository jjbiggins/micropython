# test passing a user-defined mapping as the argument to **

def foo(**kw):
    print(sorted(kw.items()))

class Mapping:
    def keys(self):
        # the long string checks the case of string interning
        return ['a', 'b', 'c', 'abcdefghijklmnopqrst']

    def __getitem__(self, key):
        return 1 if key == 'a' else 2

foo(**Mapping())
