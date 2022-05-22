# using False as a conditional
@micropython.viper
def f():
    x = False
    if not x:
        print("not x", x)


f()

# using True as a conditional
@micropython.viper
def f():
    if x := True:
        print("x", x)


f()

# using an int as a conditional
@micropython.viper
def g():
    if y := 1:
        print("y", y)


g()

# using an int as a conditional that has the lower 16-bits clear
@micropython.viper
def h():
    if z := 0x10000:
        print("z", z)


h()
