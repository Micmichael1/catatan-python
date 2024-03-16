# @micmichael1
# Tujuan Program :
# Membuat fungsi "hurufBergantian" yang akan menerima parameter "inputString" yang berisi string yang hanya memiliki dua huruf, P dan C.
# Kemudian akan mengubah string tersebut untuk menjadi sebuah string dimana tidak boleh ada huruf yang sama bersebelahan.
# Lalu akan mengembalikan jumlah huruf yang harus dihapus untuk memenuhi kebutuhan itu.

# Membuat perulangan untuk mempermudah user mengulang program tanpa mematikan program dan akan terus berjalan hingga user ingin berhenti.
on=True
while(on):
    # Membuat fungsi hurufBergantian yang menerima input string dan mengembalikan output berupa jumlah huruf minimal yang perlu dihilangkan guna menghilangkan huruf yang sama bersebelahan.
    def hurufBergantian(inputString):
        # Membuat variable output untuk menampung jumlah minimal huruf yang perlu dihilangkan
        output=0
        # Melakukan perulangan angka mulai dari 0 sampai satu angka sebelum panjang string yang diinput dikurangi 1
        for check in range(len(inputString)-1):
            # Jika ditemukan huruf yang sama antara huruf dalam string dengan index berupa angka yang sedang dilakukan perulangan
            # dengan huruf dalam string dengan index berupa angka yang sedang dilakukan perulangan+1
            if(inputString[check]==inputString[check+1]):
                # Maka output akan ditambah 1 (huruf yang harus dihapus bertambah 1)
                output+=1
        # Mengembalikan output jumlah angka minimum yang harus dihapus yang sudah dihitung tadi
        return output
    # Fungsi checkString digunakan untuk mengecheck apakah ada huruf selain P & C dalam string yang diinput user
    def checkString(inputString):
        # Melakukan perulangan angka mulai dari 0 sampai satu angka sebelum panjang string yang diinput dikurangi 1
        for check in range(len(inputString)-1):
            # Mengecheck apakah huruf dalam string dengan index berupa angka yang sedang dilakukan perulangan merupakan huruf p maupun huruf c
            if (inputString[check] != "P" and inputString[check] !="C"):
                # apabila mengandung huruf bukan huruf P maupun C maka akan mengembalikan False
                return False
        # Apabila string tersebut hanya mengandung huruf P dan C maka akan mengembalikan nilai True
        return True
    # Meminta input string dan juga memberikan arahan kepada user agar tidak kebingungan dalam menjalankan program
    # Input juga dilengkapi dengan methode upper guna menyelaraskan input agar sama sama berhuruf besar
    inputString = input("Program ini dibuat untuk memberi taukan jumlah huruf yang harus dihilangkan "
                        "untuk mengubah inputan string yang hanya berisi huruf P & C menjadi sebuah string dimana "
                        "tidak boleh ada huruf yang sama bersebelahan.\nContoh :\nInput: PCCPC\nOutput: 1\n"
                        "Masukkan string yang hanya berisi huruf P & C : ").upper()
    if(len(inputString)>1):
        # Memanggil fungsi checkString untuk memastikan hanya huruf P dan C yang diinput
        # Dan jika True maka fungsi hurufBergantian akan dijalankan
        if(checkString(inputString)):
            # Memunculkan output
            print(f'Jumlah minimum huruf yang harus dihilangkan sebanyak : {hurufBergantian(inputString)}')
        # Dan Jika False maka program akan meminta user untuk mengulang memberikan input ataupun mematikan program
        else:
            print("Mohon hanya memasukkan string yang hanya berisi huruf P dan C")
    else:
        print("Mohon memasukkan string dengan jumlah huruf lebih dari satu")
    # Bertanya kepada user untuk melanjutkan program
    on="none"
    while(on=="none"):
        dummy = input("Try again?(y/n)\n").lower()
        if(dummy=="y"):
            on=True
        elif(dummy=="n"):
            on=False
        else:
            print("Input tidak dimengerti mohon diulang")

