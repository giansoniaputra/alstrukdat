class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

# Contoh penggunaan
x = Fraction(1, 2)
y = Fraction(3, 4)

print(f"Hasil dari 1/2 - 3/4 = {x - y}")        # Operator pengurangan
print(f"Hasil dari 1/2 * 3/4 = {x * y}")        # Operator perkalian
print(f"Hasil dari 1/2 / 3/4 = {x / y}")        # Operator pembagian
