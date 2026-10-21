import random

def tebak_angka():
    print("Selamat datang di permainan Tebak Angka!")
    print("Saya telah memilih sebuah angka antara 1 hingga 9.")
    print("Coba tebak angka tersebut. Anda memiliki 1 kesempatan.")

angka_tebakan = random.randint(1, 9)
kesempatan = 1
if kesempatan > 0:
    tebakan = int(input("Masukkan tebakan Anda: "))
    if tebakan == angka_tebakan:
        print("Selamat! Anda menebak angka dengan benar.")
    else:
        print("Kesempatan Anda telah habis. Angka yang benar adalah:", angka_tebakan)
else:
    print("Kesempatan Anda telah habis. Angka yang benar adalah:", angka_tebakan)