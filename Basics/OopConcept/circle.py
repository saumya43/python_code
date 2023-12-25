import math
class Circle:
    # define object intializer and self: is a class instance
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return round(math.pi * self.radius ** 2, 2)

# run this program by creating object and calling method and classes
# import circle from Circle
# circle_1 = circle(42)
# circle_1.radius
# circle_1.calculate_area()
