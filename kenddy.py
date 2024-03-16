# LED yang diperlukan untuk tiap angka dibuat dalam sebuah dictionary
led={"0":6,
     "1":2,
     "2":5,
     "3":5,
     "4":4,
     "5":5,
     "6":6,
     "7":3,
     "8":7,
     "9":6,
     }

# Minta input angka
angka=input("Masukkan Angka Anda : ")

# Pisah tiap digit angka dan masukkan ke list
angka=[i for i in str(angka)]

total=0

# Hitung LED per angka dan dijumlahkan
for a in angka:
    total=total+led[a]

print("Jumlah Led Yang Diperlukan Adalah :",total)