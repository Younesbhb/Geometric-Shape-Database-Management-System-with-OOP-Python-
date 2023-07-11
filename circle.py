import math
from shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()  # call the parent constructor to assign an ID
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def __eq__(self, other):
        return type(self) is type(other) and self.radius == other.radius

    def __hash__(self):
        return hash((type(self), self.radius))
