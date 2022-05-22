# test loading from ptr16 type
# only works on little endian machines


@micropython.viper
def get(src: ptr16) -> int:
    return src[0]


@micropython.viper
def get1(src: ptr16) -> int:
    return src[1]


@micropython.viper
def memadd(src: ptr16, n: int) -> int:
    return sum(src[i] for i in range(n))


@micropython.viper
def memadd2(src_in) -> int:
    src = ptr16(src_in)
    n = len(src_in) >> 1
    return sum(src[i] for i in range(n))


b = bytearray(b"1234")
print(b)
print(get(b), get1(b))
print(memadd(b, 2))
print(memadd2(b))
