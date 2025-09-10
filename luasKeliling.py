import math

def lingkaran(r):
    luas = math.pi * r ** 2
    keliling = 2 * math.pi * r
    return luas, keliling

r = float(input("Masukkan jari-jari lingkaran: "))
luas, keliling = lingkaran(r)

print(f"Luas lingkaran: {luas}")
print(f"Keliling lingkaran: {keliling}")