angka = 0
hasil = 0
i = 0
while i<10:
    angka=int(input("Minta angka bossq : "))
    if(angka>50 and angka<85):
        hasil=hasil+angka
        i=i+1
    else:
        print("Angka harus lebih besar dari 50 dan lebih kecil 85")
        continue