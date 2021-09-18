# Import modul datetime
# modul datetime ini sudah ada secara default pada python
# Jadi kita tidak perlu install-install lewat Python Instalation Package atau PIP
# kita tinggal pakai saja dengan menuliskan import nama modul yang anda mau
# Jika modul tersebut tidak tersedia pada python secara default anda perlu install lewat PIP dulu
from datetime import datetime, timedelta

# dari kata import datetime tersebut, datetime nya sudah berbentuk object
# Jadi kita tinggal menggunakan nama methodnya saja yang ingin digunakan
print(datetime.now())
def today():
    """
    Menampilkan waktu saat ini.
    Import dulu modul datetimenya
    """
    return datetime.now()

hari_ini = today()
print(hari_ini)

# Import module dari modul yang kita buat sendiri
# Buat file modulumur seperti modulumur.py
from modulumur import umur
umur = umur(2000)
print(umur)