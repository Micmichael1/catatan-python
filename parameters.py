# Function wajib dibuat sebelum memanggil fungsi
# nama_pertama dan nama_kedua disebut sebagai parameter
# untuk mengubah nama variable dalam satu function
# klik kanan pada variable yang ingin direname dan tekan refactor kemudian rename
# maka semua variable tersebut akan berubah nama
def greet_user(nama_pertama,nama_kedua):
    print(f"Hello {nama_pertama} {nama_kedua}")
    print("How is your day?")
print("start")
nama_pertama=input("What is your first name? ")
nama_kedua=input("WHat is your last name? ")
greet_user(nama_pertama,nama_kedua)
# sedangkan "michelle" dan input dari nama merupakan argumen
# argument dibawah disebut positional argument karena hasilnya akan berbeda tergantung dengan penempatan argument
greet_user("Michelle","lim")
print("end")