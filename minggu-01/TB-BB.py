Tinggibadan = float(input("Tinggi badan (m): "))
beratbadan = float(input("Berat badan (kg): "))

print("Tinggi badan Anda adalah: " + str(Tinggibadan) + " m")
print("Berat badan Anda adalah: " + str(beratbadan) + " kg")

bmi = beratbadan / (Tinggibadan ** 2)
print("BMI Anda adalah: " + str(bmi))

if bmi  < 16.00:
    print("Anda termasuk kategori: Gizi Buruk")
    
elif bmi >= 16.00 and bmi <= 18.49:
    print("Anda termasuk kategori: Gizi Kurang")
    
elif bmi >= 18.50 and bmi <= 24.99:
    print("Anda termasuk kategori normal ideal")
    
elif bmi >= 25.00 and bmi <= 29.99:
    print("anda termasuk kategori gizi berlebih atau sedikit gemuk")
    
elif bmi > 30.00 and bmi <= 35.00:
    print("anda termasuk kategori obesitas dan anda disarankan untuk segera menurunkan berat badan")
    
    
    