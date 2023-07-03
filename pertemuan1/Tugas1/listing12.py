def squareroot(n):
    if n < 0:
        raise ValueError("Nilai n tidak boleh negatif")
    elif n == 0:
        return 0
    
    root = n / 2 # tebakan awal akan berupa 1/2 of n
    for k in range(20):
        root = (1 / 2) * (root + (n / root))
    return root

try:
    print(squareroot(9))
    print(squareroot(4563))
    print(squareroot(0))
except ValueError as e:
    print("Error:", str(e))