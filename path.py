from pathlib import Path
# Mengimport module Path
# Path merupakan sebuah class sehingga wajib di berikan object terlebih dahulu sebelum bisa digunakan
# path:D:\kuliah\python
# directory:ecommerce
# Path berhubungan tentang object oriented programming dalam pengolahan directory dan files
# Pembuatan Path terbagi dua:
# Absolute Path:Manual Memasukkan path locatioan directorinya cth: D:\kuliah\python
# Relative Path:Directory dimana program dibuat
# path=Path("path")
# path1=Path("test")
# # Mengecheck apakah direktori ecommerce terdapat pada path program ini
# # Bersifat Boolean
# print(path.exists())
# # Membuat Directori baru
# print(path.mkdir())
# # Menghapus Direktori path1
# print(path1.rmdir())
# # Merujuk ke path program ini
path2=Path()
# Mencari semua(*) file pada path directory ini yang menggunakaan extension(.py)
# jika ingin mencari semua file dengan semua jenis extension maka menggunkan path2.glob('*.*')
# jika ingin mencari semua file dan directori maka menggunkan path2.glob('*')
print(path2.glob('*.py'))
# Melakukan perulangan for untuk memunculkan semua file pada direktori path ini
for file in path2.glob('*.*'):
    print(file)
