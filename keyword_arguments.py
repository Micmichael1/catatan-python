def greet_user(nama_pertama,nama_kedua):
    print(f"Hello {nama_pertama} {nama_kedua}")
    print("How is your day?")
print("start")
# Disebut keyword arguments karena penempatan argumentnya sudah ditentukan sebelum fungsinya dijalankan
greet_user(nama_kedua="Lim",nama_pertama="Michelle")
print("end")

# Keyword argumen biasa digunakan untuk memudahkan pembacaan kode bagi user
calc_cost(total=50,shipping=10,discount=5)
