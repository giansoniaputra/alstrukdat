class Fraction:
    def __init__(self, top, bottom):
        if not isinstance(top, int) or not isinstance(bottom, int):
            raise ValueError("Pembilang dan penyebut harus berupa integer.")

        if bottom < 0:
            top = -top
            bottom = abs(bottom)

        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    # Implementasi operator aritmatika dan operator relasional lainnya...

# Contoh penggunaan
x = Fraction(1, 2)
y = Fraction(-3, 4)  # Penyebut negatif, tetapi pembilang diubah menjadi negatif

print(x)  # Output: 1/2
print(y)  # Output: -3/4
