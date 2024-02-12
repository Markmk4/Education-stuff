from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x1, y1):
        self.x = point1.x + x1
        self.y = point1.y + y1

    def length(self, other):
        return round(sqrt((pow((self.x - other.x) ** 2 + (self.y - other.y), 2))), 2)


point1 = Point(3, 5)
point2 = Point(7, -5)
print(point1.x, point1.y)
print(point2.x, point2.y)
print(point1.length(point2))
