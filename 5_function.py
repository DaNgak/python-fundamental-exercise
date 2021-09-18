# Function pada Python
# Kata kunci nya di "def" dan indentasi untuk isi dari functionnya

# 1 Function standart
def hello():
    print("Hello")

hello()

# 2. Fungsi dengan parameter
def hello_nama(nama):
    print(f"Hello {nama}, Selamat Datang")
hello_nama("BengakDev")

# 3. Fungsi dengan return
def hello_nama_return(nama):
    print(f"Hello {nama}, Selamat Datang")
    return True

if(hello_nama("BengakDev")):
    hello_nama_return("BengakDev")

def umur(tahun_lahir):
    return 2021-tahun_lahir

umur_now = umur(2000)
print(umur_now)


