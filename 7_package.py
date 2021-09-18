# Package pada python

# Package pada python adalah modul yang berasal dari luar
# Standartnya adalah dari PIP (Python Instalation Package)

# cara pakainya mirip seperti modul
# Contoh kita pakai package requests yang biasanya dipake fetch API
# Caranya buka terminal kalian terus ketik aja 
# pip install requests
# Tunggu sampai selesai, kalau sudah seharusnya ada folder namanya __pycache__
# Jika sudah maka next, ya mengodof
import requests as bengak
# Sama seperti modul kita import dulu package requests-nya 
# Kalian boleh pakai as jika nama packagenya terlalu panjang
# Boleh juga tidak pakai as, Kalau tidak pakai as tulis aja 
# import requests
# Nanti yang dipakai adalah object requests buka object bengak lagi

# Untuk mengetahui package requests bisa apa aja dan 
# Cara pakai nya bagaimana bisa kunjungi dokumentasi resminya
# Baca, jangan males baca !!!, baca nya di https://pypi.org/project/requests/
hasil = bengak.get('https://pypi.org/project/requests/')

print(hasil.status_code)

print(hasil.text)