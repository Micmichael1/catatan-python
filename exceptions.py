# Exception Handling dibuat untuk mengantisipasi kesalahan dan error yang mungkin terjadi pada saat penggunaan program
# Exception Handling berfungsi untuk menghindari program nge-crash sehingga dibuat alternatif jalannya

try:
    age=int(input('Age: '))
    print(age)
    income = 2000
    risk = 2000/age

# Exception ValueError akan berjalan apabila type data yang dimasukkan tidak sesuai
# Error "ValueError" diketaui dari saat menjalankan program tanpa menggunakan exception handling maka akan muncul error
except ValueError:
    print('Invalid Value')
# Exception "ZeroDivisionError" akan berjalan jika age yang dimasukkan adalah 0
# Error "ZeroDivisionError" disebabkan karena terjadi pembagian dengan angka 0
except ZeroDivisionError:
    print('Age cannot be zero')

print("hello,world!")