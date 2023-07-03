class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

# Contoh penggunaan
p = Point(2, 3)
print(str(p))  # Output: (2, 3)
print(p)       # Output: (2, 3)
