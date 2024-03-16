test={2,1,3,1,3,2}
print(test)
# dictionaries berisi key dan value dan dibuat menggunakan kurung siku
# Key wajib bersifat unique
# Value boleh bersifat segala tipe (int,float,string,boolean,list,dsb)
customer = {
    "name" : "michael lim",
    "age": 20,
    "is_verified" : True
}
# Pada dictionaries value spesifik diakses menggunakan key
# Sedangkan pada list dan tuple value spesifik diakses menggunakan index dari valuenya
print(customer["name"])
# Memunculkan semua isi key dan value dictionaries
print(customer)
# Untuk mengakses value juga bisa menggunakan method get
print(customer.get("name"))
# Apabila tidak ada
print(customer.get("birthdate"))
# Untuk memunculkan value dari key yang tidak ada di dictionaries
# Apabila key tersebut ada maka value tidak akan mengubah value awal key tersebut
# Lihat dictionaries_exercise untuk lebih lengkapnya
print(customer.get("birthdate","13 oktober 2001"))
# Mengubah value
customer["name"]="Mic"
print(customer)
# Menambahkan key dan value
customer["birthdate"]="13 oktober 2001"
print(customer)
# Menghapus satu element dari dict berdasarkan key dan apabila elemen tersebut tidak ada maka condition setelah , dijalankan
print(customer.pop('test',customer.pop('age')))
print(customer)
