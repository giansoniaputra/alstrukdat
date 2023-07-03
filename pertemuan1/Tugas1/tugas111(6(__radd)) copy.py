class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        elif not isinstance(other, Fraction):
            raise TypeError("Operand kanan harus berupa integer atau objek Fraction.")
        
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den

        return Fraction(new_num, new_den)

    def __radd__(self, other):
        return self.__add__(other)

# Contoh penggunaan
x = Fraction(1, 2)
y = 2

result = x + y  # Memanggil __add__
print(result)  # Output: 5/2

result = y + x  # Memanggil __radd__
print(result)  # Output: 5/2
