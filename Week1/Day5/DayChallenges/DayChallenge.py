
class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            self.radius = 1
    @property
    def diameter(self):
        return self.radius * 2
    @property
    def area(self):
        return math.pi * (self.radius ** 2)
    def __str__(self):
        return (
            f"Circle(radius={self.radius}, "
            f"diameter={self.diameter:.2f}, "
            f"area={self.area:.2f})"
        )
    def __add__(self, other):
        new_radius = self.radius + other.radius
        return Circle(radius=new_radius)
    def __gt__(self, other):
        return self.radius > other.radius
    def __eq__(self, other):
        return self.radius == other.radius
    def __lt__(self, other):
        return self.radius < other.radius