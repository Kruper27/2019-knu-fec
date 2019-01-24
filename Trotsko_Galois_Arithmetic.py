import timeit


# addition, multiplication, division in GF(2 ^ 8)
def add(self, other):
    return self ^ other


def mul(self, other):
    if self == 0 or other == 0:
        return 0
    log = gflog[self] + gflog[other]
    if log >= x_to_w - 1:
        log -= x_to_w - 1
    return gfilog[log]


def div(self, other):
    if self == 0:
        return 0
    elif other == 0:
        raise ZeroDivisionError
    else:
        diff_log = gflog[self] - gflog[other]
        if diff_log < 0:
            diff_log += x_to_w - 1
        return gfilog[diff_log]


# generation of the logarithm and inverse logarithm tables
x_to_w = 1 << 8
prim_poly = 285
gflog = [None] * x_to_w
gfilog = [None] * x_to_w

b = 1
for log in range(x_to_w):
    gflog[b] = log
    gfilog[log] = b
    b <<= 1
    if b & x_to_w:
        b = b ^ prim_poly


if __name__ == '__main__':
    print('123 + 78 10 ^ 6 times: ', timeit.timeit(setup='from __main__ import add', stmt='add(123, 78)'))
    print('123 * 78 10 ^ 6 times: ', timeit.timeit(setup='from __main__ import mul', stmt='mul(123, 78)'))
    print('123 / 78 10 ^ 6 times: ', timeit.timeit(setup='from __main__ import div', stmt='div(123, 78)'))
