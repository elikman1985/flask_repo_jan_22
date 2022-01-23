class Shape:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy


class Point(Shape):
    def __init__(self, dx, dy):
        Shape.__init__(self, dx, dy)


class Circle(Shape):
    def __init__(self, dx, dy, r):
        Shape.__init__(self, dx, dy)
        # super().__init__(dx, dy)
        self.r = r

    def contains(self, pt):
        if self.r ** 2 >= (pt.dx - c.dx) ** 2 + (pt.dy - c.dy) ** 2:
            return True
        else:
            return False

    def __contains__(self, pt):
        return self.r ** 2 >= (pt.dx - c.dx) ** 2 + (pt.dy - c.dy) ** 2


p = Point(4, 0)
c = Circle(1, 0, 3)
print(c.contains(p))
print(p in c)
