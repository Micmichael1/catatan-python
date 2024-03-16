# File converters.py sudah dibuat sebelumnya untuk dijadikan sebagai module
# Guna module adalah untuk membagi codingan kita sehingga terlihat lebih rapi dan bisa digunakan ulang

# Cara 1 (Memanggil seluruh module)
# Panggil converters.py
import converters
# Sekarang fungsi,methods dan lain lain dari converters.py dapat digunakan di sini
print(converters.kg_to_lbs(10))

# Cara 2 (Memanggil fungsi tertentu dari suatu module)
# Tidak perlu import converter tinggal langsung from converters import fungsi yang kita inginkan
# Untuk melihat fungsi fungsi" dan method" yang terdapat di module converters
# tinggal tekan ctrl + space setelah from converters import
from converters import kg_to_lbs
# dengan cara ini, anda tidak perlu lagi memanggil nama module untuk menggunakan fungsi dan method di dalamnya
print(kg_to_lbs(10))
