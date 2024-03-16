# @micmichael1
# Tujuan program : Dari list berisi integer yang diinput, program akan mencari subset dari elemen yang TIDAK BERSEBELAHAN
# yang jika di total, memiliki jumlah terbesar dan kemudian memunculkan jumlah dari subset tersebut.

# Mengimport fungsi ceil dari module math
from math import ceil
# Membuat fungsi subsetTerbesar yang berisi fungsi mencari jumlah subset terbesar
def subsetTerbesar(inputList):
    # variable max untuk menampung penjumlahan subset terbesar
    max = 0
    # melakukan perulangan untuk tiap inputList
    for i in range (len(inputList) - 2):
        # note : dalam membentuk subset, pengambilan dibagi menjadi 2 yaitu:
        # 1.bagian depan (i) dimana angka selalu sama
        # 2.bagian belakang dimana angka diambil melakukan perulangan
        # mencari panjang subset terpanjang yang memungkinkan dengan elemen awal berupa i
        terpanjang = ceil((len(inputList) - i) / 2)
        # mencari batas angka terakhir yang memungkinkan sebelum mengambil angka bagian belakang
        batas = ((terpanjang-1)*2)+i
        # melakukan perulangan untuk mengurangi batas sehingga dapat megambil lebih banyak angka bagian belakang
        for batas1 in range(batas,i,-2):
            # melakukan perulangan +1 untuk mengambil angka bagian belakang
            for n in range(batas1, len(inputList), 1):
                # jika jumlah subset yang mana merupakan gabungan subset bagian depan dan bagian belakang lebih besar dari max maka subset tersebut akan menjadi max
                if(sum(inputList[i:batas1:2] + inputList[n::2])>max):
                    max = sum(inputList[i:batas1:2] + inputList[n::2])
    # Mengembalikan nilai max subset terbesar
    return max
# meminta inputList dan membuat exception handling untuk mencegah input yang tidak diinginkan
try:
    inputList=list(map(int,input('''
Silahkan masukkan list angka yang ingin dicari subset terbesarnya dimana element nya tidak bersebelahan
Format input list : 1,2,3,4,5
Input anda : ''').split(",")))
except ValueError:
    print("Element list yang dimasukkan wajib merupakan data bertipe integer")
else:
    # Hanya menjalankan program apabila jumlah element dalam list lebih banyak dari 2
    if(len(inputList)>2):
        print("Jumlah Terbesar dari subset yang element nya tidak bersebelahan dari list yang diberikan adalah",subsetTerbesar(inputList))
    else:
        print("Jumlah element dalam list yang dimasukkan wajib lebih banyak dari 2")