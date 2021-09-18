# 1. Pengenalan variabel
# variabel ya variabel buat nampung data intinya gitu
# tidak seperti java yang harus instasiasi tipe datanya itu interger apa string
# di python tidak perlu sobat, python udah pinter ga perlu instansiasi tipe data
# cukup ketik nama variabelnya lalu kasi nilainya apa aja
# contoh

nama = "Bengak" 
# variabel nama itu sudah tipe datanya string secara otomatis di deteksi oleh python
umur = 18
# variabel umur itu sudah tipe datanya integer secara otomatis di deteksi oleh python

# tidak perlu bikin seperti dijava
# String nama = "Bengak"
# itu terlihat sangat ribet tidak seperti python simpel sekali

# tapi minusnya konsep tipe data minus seperti python ini 
# variabelnya bisa di ganti dengan tipe data apapun
# contoh
nama = 19
umur = "BengakDev"
# jika kita mencetak hasilnya tidak akan error
# dan variabel nama mencetak 19 dan umur mencetak BengakDev
print("Nama = ", nama, "\nUmur = ", umur)
# 2. tipe data di python
# a. String
string = "Ini String"
concatstring = string + "Gampang kan ??"
# concat di string cukup pake tanda +
print(string)
print(concatstring)
# mengubah/format tipe string 
# contoh paling gampang uppercase, lowercase, dan formating
# sisanya bisa kalian explor lagi sendiri :)
nama = "Bengak Dev"
print(nama.upper()) 
print(nama.lower()) 
kalimat = f"Nama saya adalah {nama}, Saya suka python"
print(kalimat)
# b. Boolean
inibooleantrue = True
inibooleanfalse = False
inibooleantruedibalik = not True
print(inibooleantrue)
print(inibooleanfalse)
print(inibooleantruedibalik)
# c. Integer 
bilanganpositif = 10
bilangannegatif = -10
print(bilanganpositif)
print(bilangannegatif)
# d. Float
bilangankomapositif = 43.19
bilangankomanegatif = -43.19
print(bilangankomapositif)
print(bilangankomanegatif)
# e. List(sebenarnya array tapi di python disebut list) 
# - Buat tipe data list
daftar_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
daftar_angka_str = ["satu", "dia", "tiga"]
daftar_angka_campur = [1, "dua", -3, "empat", 5, True, 6.7, False]
print(daftar_angka)
print(daftar_angka_str)
print(daftar_angka_campur)
# - Akses tipe data list
# caranua cukup mudah dengan menuliskan listnya kemudian diikuti dengan indexnya
print(daftar_angka[0])
print(daftar_angka_str[2])
print(daftar_angka_campur[4])
print(daftar_angka_campur[6])
# cetak list yang tidak ada indexnya
# print(daftar_angka_campur[100])
# itu sengaja saya comment kalo di run ya pasti error sobat :)

# - tambah data tipe data list
daftar_angka = [1, 2, 3]
# kalo mau tambah data pake fungsi append()
# cara pakainya masukkan value yang mau di push atau ditambah
# contoh push index 1 yaitu angka 2
daftar_angka.append(10)
print(daftar_angka)
# kalo mau hapus data pake fungsi pop()
# cara pakainya masukkan index yang mau di pop
# contoh pop index 1 yaitu angka 2
daftar_angka.pop(1)
print(daftar_angka)
# sebenarnya masih ada banyak method yang digunakan
# menambahkan dan menghapus serta memanipulasi list
# yaa kalian bisa searching atau pelajari sendiri nanti
# intinya yang penting seperti tambah data dan hapus data
# sudah saya contohkan di atas, sisanya kalian explor lagi :)

# e. List Assosiatif
# PR



