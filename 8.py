from functools import partial


def func(u, v, w, x):
    return u * 4 + v * 3 + w * 2 + x


op = partial(func, 5, 6, 7)
print(op(8))
