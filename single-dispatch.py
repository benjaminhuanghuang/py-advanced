from functools import singledispatch

class Circle:
    pass


class Parallelogram:
    pass


class Triangle:
    pass


@singledispatch(Circle)
def draw(shape):
    raise TypeError("Don't know how to draw {!r}".format(shape))


@singledispatch
def draw_circle(Parallelogram):
    pass


@singledispatch()
def draw_parallelogram():
    pass


@singledispatch(Triangle)
def draw_triangle():
    pass


for shape in shapes:
    draw(shape)
