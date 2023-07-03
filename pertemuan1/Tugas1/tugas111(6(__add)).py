class MyNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, MyNumber):
            return MyNumber(self.value + other.value)
        elif isinstance(other, int):
            return MyNumber(self.value + other)
        else:
            raise TypeError("Operand harus berupa objek MyNumber atau integer.")

    def __radd__(self, other):
        if isinstance(other, int):
            return MyNumber(self.value + other)
        else:
            raise TypeError("Operand kanan harus berupa integer.")

# Contoh penggunaan
x = MyNumber(5)
y = MyNumber(10)

result1 = x + y  # Memanggil __add__ pada objek x
print(result1.value)  # Output: 15

result2 = y + 3  # Memanggil __add__ pada objek y
print(result2.value)  # Output: 13

result3 = 2 + x  # Memanggil __radd__ pada objek x
print(result3.value)  # Output: 7
