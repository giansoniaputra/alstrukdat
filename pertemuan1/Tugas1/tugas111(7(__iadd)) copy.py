class MyNumber:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        if isinstance(other, MyNumber):
            self.value += other.value
        elif isinstance(other, int):
            self.value += other
        else:
            raise TypeError("Operand harus berupa objek MyNumber atau integer.")
        
        return self

# Contoh penggunaan
x = MyNumber(5)
y = MyNumber(10)

x += y  # Memanggil __iadd__
print(x.value)  # Output: 15

x += 3  # Memanggil __iadd__
print(x.value)  # Output: 18
