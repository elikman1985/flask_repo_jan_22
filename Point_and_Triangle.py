class Point:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def __str__(self):
        return 'x:' + str(self.dx) + ' | ' 'y:' + str(self.dy)

    def __add__(self, other):
        res = Point(
            self.dx + other.dx,
            self.dy + other.dy
        )
        return res

    def __sub__(self, other):
        res = Point(
            self.dx - other.dx,
            self.dy - other.dy
        )
        return res

    def get_xy(self):
        res = Point(
            self.dx,
            self.dy
        )
        return res


class Triangle:
    def __init__(self, pt1, pt2, pt3):
        self.pt1 = pt1
        self.pt2 = pt2
        self.pt3 = pt3

    def get_perimeter(self):
        ab = ((self.pt2.dx - self.pt1.dx) ** 2 + (self.pt2.dy - self.pt1.dy) ** 2) ** 0.5
        bc = ((self.pt3.dx - self.pt2.dx) ** 2 + (self.pt3.dy - self.pt2.dy) ** 2) ** 0.5
        ac = ((self.pt3.dx - self.pt1.dx) ** 2 + (self.pt3.dy - self.pt1.dy) ** 2) ** 0.5
        return ab + bc + ac

    def get_square(self):
        return abs(((self.pt2.dx - self.pt1.dx) * (self.pt3.dy - self.pt1.dy)
                    - (self.pt3.dx - self.pt1.dx) * (self.pt2.dy - self.pt1.dy)) * 0.5)

    def new_a(self, new_pt):
        self.pt1 = new_pt
        return self.pt1

    def new_b(self, new_pt):
        self.pt2 = new_pt
        return self.pt2

    def new_c(self, new_pt):
        self.pt3 = new_pt
        return self.pt3


a = Point(3, 6)
b = Point(1, 9)
c = Point(4, 0)

t = Triangle(a, b, c)

# print(Triangle.get_perimeter(t))
# print(Triangle.get_square(t))
#
# d = Point(5, 5)
# e = Point(7, 3)
# f = Point(1, 6)
#
# Triangle.new_a(t, d)
# Triangle.new_b(t, e)
# Triangle.new_c(t, f)
#
# print(Triangle.get_perimeter(t))
# print(Triangle.get_square(t))
