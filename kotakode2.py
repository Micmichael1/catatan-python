# @micmichael1
# Tujuan Program :
# Diberikan 2 input: input pertama adalah sebuah list berisi integer dan input kedua adalah sebuah integer, x.
# Program akan menemukan semua kemungkinan kombinasi pasangan dari list tersebut yang dimana total jumlah dari setiap pasangan nya harus sama dengan x.
# Membuat fungsi cariPasangan untuk mencari kombinasi pasangan
def cariPasangan(inputList,inputInt):
    # list output untuk menampung kombinasi pasangan
    output=[]
    # list dummy1 berisi seluruh element dari list inputList
    # list dummy1 dibuat untuk menghindari kombinasi pasangan yang berulang contoh [1,2] dan [2,1]
    # apabila ditemukan pasangan yang dijumlahkan menghasilkan inputInt maka pasangan tersebut akan dihapus dari daftar
    # misal untuk penjumlahan 3 maka pasangan yang didapat adalah [1,2] maka element 1 dan 2 akan dihapus dari daftar
    dummy1=inputList[:]
    # melakukan perulangan untuk menggunakan element dari list inputList
    for i in inputList:
        # apabila i ditemukan dalam list dummy1 maka program akan dilanjutkan
        if(i in dummy1):
            # list dummy2 berisi seluruh element dari list inputList
            # list dummy2 dibuat untuk menyingkirkan data diri sendiri (i) dalam data daftar pencarian pasangannya
            # misal untuk list [1,2,3,4] dan sedang dilakukan pencarian untuk pasangan angka 1 maka angka 1 itu sendiri tidak akan ada dalam daftar pencarian
            # daftar pencarian pasangan hanya [2,3,4]
            dummy2=inputList[:]
            # Menghilangkan data i dari daftar pencarian pasangan agar tidak dianggap sebagai kemungkinan pasangan
            dummy2.remove(i)
            # jika pasangan untuk angka tersebut ditemukan dalam daftar pencarian pasangan (selain diri sendiri)
            if(inputInt-i in dummy2):
                # menghapus data pasangan tersebut dari daftar asli
                dummy1.remove(i)
                # jika pasangan untuk angka tersebut ditemukan dalam daftar pencarian pasangan (selain diri sendiri)
                if(inputInt-i in dummy1):
                    # Memasukkan data pasangan tersebut ke output untuk dikembalikan nantinya
                    output.append([i,inputInt-i])
                    # menghapus data pasangan tersebut dari daftar asli
                    dummy1.remove(inputInt - i)
            # Menghapus list sementara dummy2
            dummy2.clear()
    # Mengembalikan output
    return output
# meminta input list deretan angka
# Membuat exception handling guna memastikan inputList hanya berisi deretan integer
try:
    inputList=list(map(int,input("Masukkan sebuah List angka (Minimal 2 buah angka)\nContoh format penulisan : 1,2,3,4,5\nInput Anda : ").split(',')))
except ValueError :
    print("Mohon hanya memasukkan deretan angka")
else :
    # program hanya berjalan jika element di inputList minimal 2
    if(len(inputList)>=2):
        # meminta input angka sebagai target penjumlahan
        # Membuat exception handling guna memastikan inputInt merupakan data bertipe integer
        try:
            inputInt=int(input("Masukkan sebuah angka sebagai target penjumlahan : "))
        # Memunculkan peringatan error jika inputInt bukan merupakan data bertipe inhteger dan menghentikan program
        except ValueError:
            print("Mohon target penjumlahan yang dimasukkan hanya berupa data bertipe integer")
        else :
            # memunculkan pasangan yang ditemukan
            print(f'Pasangan dari list {inputList} dimana jumlah dari dua bilangan tersebut sama dengan integer {inputInt} adalah : {cariPasangan(inputList,inputInt)}')
    # memunculkan peringatan error jika element di inputList lebih sedikit dari 2 dan menghentikan program
    else:
        print("Jumlah Element (angka) dalam list (barisan angka) yang dimasukkan harus minimal berjumlah 2")

