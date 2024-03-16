course='Python For Beginners'
course1='pYThon fOr beGiNNeRs'
# Menghitung Jumlah Karakter Pada Sebuah Kalimat
# print() dan len() disebut sebagai function biasa
print(len(course))

# Membuat Seluruh Karakter Pada Kalimat Menjadi Huruf Besar/Huruf Kecil Tanpa Menyentuh & Mengubah Variabel Awal
# upper() & lower() disebut sebagai method karena hanya spesifik untuk satu objek pada soal ini adalah string
print(course.upper())
print(course.lower())
print(course)

# Membuat karakter pertama tiap kata menjadi huruf besar dan huruf selain huruf pertama tiap kalimat menjadi huruf kecil
print(course.title())

# Mencari letak posisi suatu karakter dalam sebuah kalimat & juga mulai dari array mana sebuah kata yang dimasukkan
print(course.find('o'))
# Method find() bersifat case sensitive sehingga o kecil tidak sama dengan O besar. Sehingga akan mengeluarkan input -1 (tidak ditemukan)
print(course.find('O'))
print(course.find('Beginners'))

# Mengubah karakter dengan menggunakan method replace()
print(course.replace('Beginners','Absolute Beginners'))
# Method replace() bersifat case sensitive sehingga jika beda case maka object tidak akan berubah
print(course.replace('beginners','Absolute Beginners'))
# Method replace() juga bisa digunakan untuk me-replace satu karakter saja
print(course.replace('P','F'))

# Memeriksa apakah input terdapat dalam object
# Fungsi in ber-tipe data boolean
print('Python' in course)
