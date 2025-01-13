class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

if __name__ == '__main__':
    circle = Circle(1)
    print(circle.get_radius())

    circle.set_radius(3)
    print(circle.get_radius())