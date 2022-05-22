# Test a deep set of "yield from" statements.


def recursive_yield_from(depth, iter_):
    if depth <= 0:
        yield from iter_
    else:
        yield from recursive_yield_from(depth - 1, iter_)


def test(n):
    global result
    result = sum(recursive_yield_from(10, range(n)))


###########################################################################
# Benchmark interface

bm_params = {
    (100, 10): (2000,),
    (1000, 10): (20000,),
    (5000, 10): (100000,),
}


def bm_setup(params):
    (nloop,) = params
    return lambda: test(nloop), lambda: (nloop // 100, result)
