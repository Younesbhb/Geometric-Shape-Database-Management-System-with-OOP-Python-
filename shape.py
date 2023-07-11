class Shape:
    id_counter=0
    def __init__(self):
        Shape.id_counter+=1
        self.id=Shape.id_counter

    def perimeter(self):
        return None

    def area(self):
        return None

    def print(self):
        class_name = type(self).__name__
        perimeter = self.perimeter()
        area = self.area()

        # if perimeter and area are None, print "undefined"
        perimeter = "undefined" if perimeter is None else round(perimeter, 5)
        area = "undefined" if area is None else round(area, 5)

        print(f"{self.id}: {class_name}, perimeter: {perimeter}, area: {area}")

    def __eq__(self, other):
        return type(self) is type(other)

    def __hash__(self):
        return hash((type(self),))
