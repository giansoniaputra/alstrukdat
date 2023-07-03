class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

x = Fraction(1, 2)
print(x.getNum())  # Mengembalikan pembilang (numerator): 1
print(x.getDen())  # Mengembalikan penyebut (denominator): 2
