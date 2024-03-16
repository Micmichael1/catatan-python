def tanya_jumlah_list():
    jumlah=int(input("Masukkan banyaknya angka : "))
    return jumlah

def buat_list(jumlah):
    list=[]
    for dummy in range (jumlah):
        list.append(int(input(f"Masukkan angka ke {dummy+1} : ")))
    return list

def find_max(list):
    max = list[0]
    for number in list:
        if(number>max):
            max=number
    print(max)
