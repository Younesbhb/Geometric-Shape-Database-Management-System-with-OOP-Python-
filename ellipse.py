import math
from shape import Shape

class Ellipse(Shape):
    def __init__(self, a, b):
        # Call the constructor of the parent class
        super().__init__()

        #for the details and save method
        self.previous_a = a
        self.previous_b = b


        # a (semi-major axis) is always greater than b (semi-minor axis)
        self.a = max(a, b)
        self.b = min(a, b)
        
    def area(self):
        # The formula for area of ellipse is π*a*b
        return math.pi * self.a * self.b

    def eccentricity(self):
        # The formula for eccentricity of ellipse is sqrt(a^2 - b^2)
        try:
            return math.sqrt(self.a ** 2 - self.b ** 2)
        except ValueError:
            return None

    def print(self):
        class_name = type(self).__name__
        perimeter = self.perimeter()
        area = self.area()
        eccentricity = self.eccentricity()
        # if perimeter and area are None, print "undefined"
        perimeter = "undefined" if perimeter is None else round(perimeter, 5)
        area = "undefined" if area is None else round(area, 5)
        eccentricity = "undefined" if eccentricity is None else round(eccentricity, 5)

        print(f"{self.id}: {class_name}, perimeter: {perimeter}, area: {area}, linear eccentricity: {eccentricity}")

    def __eq__(self, other):
        return type(self) is type(other) and self.a == other.a and self.b == other.b

    def __hash__(self):
        return hash((type(self), self.a, self.b))
