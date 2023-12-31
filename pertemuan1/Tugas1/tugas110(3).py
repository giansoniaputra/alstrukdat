class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __gt__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num > second_num

    def __ge__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num >= second_num

    def __lt__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num < second_num

    def __le__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num <= second_num

    def __ne__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num != second_num

# Contoh penggunaan
x = Fraction(1, 2)
y = Fraction(3, 4)

print("x adalah 1/2 dan y adalah 3/4")
print(f"Apakah x lebih dari y = {x > y}")        # Operator lebih besar
print(f"Apakah x lebih dari sama dengan dari y = {x >= y}")       # Operator lebih besar atau sama dengan
print(f"Apakah x kurang dari y = {x < y}")        # Operator kurang dari
print(f"Apakah x kurang sama dangan dari y = {x <= y}")       # Operator kurang dari atau sama dengan
print(f"Apakah x tidak sama dengan y = {x != y}")       # Operator tidak sama
