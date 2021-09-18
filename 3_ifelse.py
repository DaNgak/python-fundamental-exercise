# If Else
# If pada python sama saja seperti bahasa pemrograman lain
# Tetapi bedanya pada python if nya lebih luas
# Bisa digunakan untuk searching data, pemilihan sepihak, statement berulang
# Bedanya dengan bahasa lain pada python pakai titik dua setelah selesai statement
# dan statementnya tidak pakai kurang buka dan kurung tutup, dan untuk kurung kurawalnya
# diganti dengan indentasi, indentasi disini adlaah jarak dari awal code yang agak menjorok ke arah kanan

# Indentasi pada python
# Indentasi digunakan untuk berbagai macam statement yang menggunakan titik dua : (dalam bahasa lain biasanya kurung kurawal)
# Biasanya setelah titik dua harus ada indentasi agar tidak terjadi error
# Indentasi normalnya adalah 2 spasi ataupun 4 spasi
# indentasi biasanya dipakai di if else, di for atau loop, class, dan object cloning

# Contoh if else
# Catatan pada pyhton else if diganti denga elif
angka = 10.5
angka2 = 20
if angka % 2 == 1:
    print("angka Ganjil")
elif angka % 2 == 0:
    print("angka Genap")
else :
    print("Ini bukan bilangan bulat woi !!!")


if angka == 10 and angka2 == 15:
    print("Operasi Benar")
else:
    print("Operasi Salah")

if angka == 10 or angka2 == 15:
    print("Operasi Benar")
else:
    print("Operasi Salah")


# If statement untuk searching
daftar_angka = [1, 2, 3, 4, 5]
if 5 in daftar_angka:
    print("Angka 5 ada di array")
else :
    print("Angka 5 tidak ada di array")

if "p" in "python":
    print("Huruf p ada di python")
else :
    print("Huruf p tidak ada di python")

# untuk pemilihan sepihak, statement berulang bisa di pelajari sendiri yok