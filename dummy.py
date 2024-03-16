# @micmichael1
# Tujuan program : Dari list berisi integer yang diinput, program akan mencari subset dari elemen yang TIDAK BERSEBELAHAN
# yang jika di total, memiliki jumlah terbesar dan kemudian memunculkan jumlah dari subset tersebut.

# Mengimport fungsi ceil dari module math
from math import ceil

# Membuat fungsi subsetTerbesar yang berisi fungsi mencari jumlah subset terbesar
def subsetTerbesar(inputList):
    # variable max untuk menampung penjumlahan subset terbesar
    max = 0
    for i in range (len(inputList) - 2):
        print("Untuk angka", inputList[i])
        terpanjang = ceil((len(inputList) - i) / 2)
        print("Dengan Panjang Maksimum",terpanjang)
        batas = ((terpanjang-1)*2)+i
        print("Dengan batas berupa angka", inputList[batas])
        for batas1 in range(batas,i,-2):
            print(inputList[batas1])
            for n in range(batas1, len(inputList), 1):
                print(sum(inputList[i:batas1:2] + inputList[n::2]))
                if(sum(inputList[i:batas1:2] + inputList[n::2])>max):
                    max = sum(inputList[i:batas1:2] + inputList[n::2])
    return max
# meminta inputList dan membuat exception handling untuk mencegah input yang tidak diinginkan
try:
    inputList=list(map(int,input('''
    Silahkan masukkan list angka yang ingin dicari subset terbesarnya dimana element nya tidak bersebelahan\n
    Format input list : 1,2,3,4,5\n
    Input anda : ''').split(",")))
except ValueError:
    print("Element list yang dimasukkan wajib merupakan data bertipe integer")
else:
    # Hanya menjalankan program apabila jumlah element dalam list lebih banyak dari 2
    if(len(inputList)>2):
        print("Jumlah Terbesar adalah ",subsetTerbesar(inputList))
    else:
        print("Jumlah element dalam list yang dimasukkan wajib lebih banyak dari 2")