# For pada Python
# For digunakan untuk ngeloop sebuah blok kode yang ada didalam
# Ada for, ada while, dan ada do while
# Konsepnya sama seperti Program java dan lain lain
# Kata kuncinya ada statementnya dan juga indentasinya

array = [1, 2, 4, 7, 9, 14, 23]
for angka in array:
    print(angka)
for huruf in "Hello Python":
    print(huruf)

# For in range
for i in range(3):
    print(i)

for i in range(10, 15):
    print(i)

angka = 1
while angka < 10:
    print(angka)
    angka += 1

# break
angka = 1
while angka < 10:
    print(angka)
    if angka == 5:
        break
    angka += 1
# continue
angka = 0
while angka < 10:
    angka += 1
    if angka == 5:
        continue
    print(angka)
    