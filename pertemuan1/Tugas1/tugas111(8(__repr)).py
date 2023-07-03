class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Contoh penggunaan
p = Point(2, 3)
print(repr(p))  # Output: Point(2, 3)   
