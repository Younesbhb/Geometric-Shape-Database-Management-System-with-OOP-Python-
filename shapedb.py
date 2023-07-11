from shape import Shape
from circle import Circle
from ellipse import Ellipse
from rhombus import Rhombus

class ShapeDB:
    def __init__(self):
        self.shapes = []
        
        
    def load(self, filename):
        print(f"Processing {filename}...")
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"Error: File not found: {filename}")
            return

        num_rows = len(lines)
        num_shapes_added = 0
        num_errors = 0

        for line in lines:
            data = line.strip().split(' ')
            shape_type = data[0]

            try:
                if shape_type.lower() == "circle":
                    radius = int(data[1])
                    if radius <= 0:
                        raise ValueError(f"Invalid Circle radius on line {lines.index(line)+1}: {line.strip()}")
                    self.shapes.append(Circle(radius))
                    num_shapes_added += 1
                elif shape_type.lower() == "rhombus":
                    d1 = int(data[1])
                    d2 = int(data[2])
                    if d1 <= 0 or d2 <= 0:
                        raise ValueError(f"Invalid Rhombus parameters on line {lines.index(line)+1}: {line.strip()}")
                    self.shapes.append(Rhombus(d1, d2))
                    num_shapes_added += 1
                elif shape_type.lower() == "ellipse":
                    a = int(data[1])
                    b = int(data[2])
                    if a <= 0 or b <= 0:
                        raise ValueError(f"Invalid Ellipse parameters on line {lines.index(line)+1}: {line.strip()}")
                    self.shapes.append(Ellipse(a, b))
                    num_shapes_added += 1
                elif shape_type.lower() == "shape":
                    self.shapes.append(Shape())
                    num_shapes_added += 1
                else:
                    print(f"Error: Unknown shape type '{shape_type}' on line {lines.index(line)+1}: {line.strip()}")
                    num_errors += 1
            except ValueError as e:
                print(f"{str(e)}")
                num_errors += 1

        print(f"Processed {num_rows} row(s), {num_shapes_added} shape(s) added, {num_errors} error(s).")

        

    def toset(self):
        self.shapes = list(set(self.shapes))


    def save(self, filename):
        try:
            with open(filename, 'w') as f:
                for shape in self.shapes:
                    f.write(self.shape_to_string(shape) + "\n")
        except Exception as e:
            print(f"Error: Unable to write to file {filename}. Error details: {str(e)}")

    def shape_to_string(self, shape):
        
        if isinstance(shape, Circle):
            radius = int(shape.radius)
            return f"circle {radius}"
        
        elif isinstance(shape, Ellipse):
            a = int(shape.previous_a)
            b = int(shape.previous_b)
            return f"ellipse {a} {b}"
        
        elif isinstance(shape, Rhombus):
            d1 = int(shape.d1)
            d2 = int(shape.d2)
            return f"rhombus {d1} {d2}"
        
        elif isinstance(shape, Shape):
            return "shape"
    
    def print(self):
        for shape in self.shapes:
            shape.print()

    def summary(self):
        # Initialize a dictionary to hold the counts of each shape
        shape_counts = {'Shape': 0, 'Circle': 0, 'Ellipse': 0, 'Rhombus': 0}
        for shape in self.shapes:
            shape_counts[type(shape).__name__] += 1

        # Print the shape summary in the desired format
        shape_names = sorted(shape_counts.keys())  # Sort the shape names alphabetically
        for shape_name in shape_names:
            count = shape_counts[shape_name]
            # Plural form
            if shape_name == 'Rhombus':
                print(f"{shape_name}(es): {count}")
            elif shape_name == 'Shape':
                print(f"Shape(s): {len(self.shapes)}")
            else:
                print(f"{shape_name}(s): {count}")

    def details(self):
        shape_strings = []

        for shape in self.shapes:
            if type(shape) == Shape:
                shape_strings.append("shape")

        for shape in self.shapes:
            if isinstance(shape, Circle):
                radius = shape.radius
                shape_strings.append(f"circle {radius}")
                            
        for shape in self.shapes:
            if isinstance(shape, Ellipse):
                a = shape.previous_a
                b = shape.previous_b
                shape_strings.append(f"ellipse {a} {b}")

        for shape in self.shapes:
            if isinstance(shape, Rhombus):
                d1 = shape.d1
                d2 = shape.d2
                shape_strings.append(f"rhombus {d1} {d2}")

        print("\n".join(shape_strings))
        

def main():
    db = ShapeDB()
    while True:

        command = input("> ")
        command_word, _, rest = command.partition(' ')

        if command_word.upper() == "LOAD":
            db.load(rest)
        elif command_word.upper() == "TOSET":
            db.toset()
        elif command_word.upper() == "SAVE":
            db.save(rest)
        elif command_word.upper() == "PRINT":
            db.print()
        elif command_word.upper() == "SUMMARY":
            db.summary()
        elif command_word.upper() == "DETAILS":
            db.details()
        elif command_word.upper() == "QUIT":
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
