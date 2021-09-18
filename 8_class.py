# Membuat class pada python
# Sama seperti java intinya dan konsepnya sama saja ada atribut ada method
# Cuma bedanya di penulisan sana kalo dijava masi ribet pakai String, int, dll
# Di python tinggal tulis nama atribut nya aja
# Untuk methodnya tinggal pakai def namaMethod(param):, jangan lupa indentnya
class User:
    nama = "BengakDev"
    umur = 17
    def sayHello(self, nama):
        return f"Halo {nama}, Salam kenal saya {self.nama}"

user = User()
print(user.nama)
print(user.umur)
print(user.sayHello("Si Dia"))