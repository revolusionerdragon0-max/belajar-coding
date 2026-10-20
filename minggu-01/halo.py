nama = input("Siapa Nama Anda? ")
umur = int(input("Berapa umur Anda? "))

print("Halo, " + nama + " mau bikin ktp?")
if umur >= 17:
    print("Kamu sudah cukup umur untuk bikin KTP.")
else:
    print("maaf ya belum cukup umur buat ktp")