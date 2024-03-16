# Cara menggunakan built-in module dari python
# Panggil modulenya
# Untuk mengetahui module apa saja yang tersedia lihat pada "referensi.txt" di folder python
import random
# Menghasilkan angka random dari 0-1
print("Menghasilkan angka random dari 0-1")
for i in range (3):
    print(random.random())

# Menghasilkan angka random dari 10 sampai 19
print("Menghasilkan angka random dari 10 sampai 19")
for i in range (3):
    print(random.randint(10, 19))


members=['michael','michelle','sjukiman','eli']
print(sorted(members))
leader=random.choice(members)
print("leader : ",leader)