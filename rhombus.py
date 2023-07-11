import math
from shape import Shape
class Rhombus(Shape):
    
    def __init__(self, d1, d2):
        super().__init__()
        self.d1 = d1  # Diagonal 1
        self.d2 = d2  # Diagonal 2

    def perimeter(self):
        # The perimeter of a rhombus is 2*sqrt(d1^2 + d2^2)
        return 2*math.sqrt(self.d1**2 + self.d2**2)

    def area(self):
        # The area of a rhombus is 1/2*(d1*d2)
        return 0.5 * self.d1 * self.d2

    def side(self):
        # The side of a rhombus is sqrt(d1^2 + d2^2)/2
        return math.sqrt(self.d1**2 + self.d2**2)/2

    def inradius(self):
        # formula for inradius = (d1*d2) / (2*sqrt(d1^2 + d2^2))
        try:
            return (self.d1 * self.d2) / (2*math.sqrt(self.d1**2 + self.d2**2))
        except (ValueError, ZeroDivisionError):
            return None

    def print(self):
        class_name = type(self).__name__
        perimeter = self.perimeter()
        area = self.area()
        side = self.side()
        inradius = self.inradius()
        perimeter = "undefined" if perimeter is None else round(perimeter,5)
        area = "undefined" if area is None else round(area,5)
        side = "undefined" if side is None else round(side,5)
        inradius = "undefined" if inradius is None else round(inradius,5)
        print(f"{self.id}: {class_name}, perimeter: {perimeter}, area: {area}, side: {side}, in-radius: {inradius}")

    def __eq__(self, other):
        return type(self) is type(other) and self.d1 == other.d1 and self.d2 == other.d2

    def __hash__(self):
        return hash((type(self), self.d1, self.d2))
