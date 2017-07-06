class Circle:
    pass


class Parallelogram:
    pass


class Triangle:
    pass


def draw_circle():
    pass


def draw_parallelogram():
    pass


def draw_triangle():
    pass


def draw(shape):
    drawers = {
        Circle: draw_circle,
        Parallelogram: draw_parallelogram,
        Triangle: draw_triangle
    }
    try:
        drawer = drawers[type(shape)]
    except KeyError as e:
        raise TypeError("Can't draw shape".format(e))
    else:
        drawer(shape)
