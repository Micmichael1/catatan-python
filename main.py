# import main_method
# nama=input("Masukkan nama anda : ")
# objek=main_method.kalkulator(nama)
# type=input("simple/rumit : ")
# if(type=="simple"):
#     operasi=input("Operasi yang ingin dilakukan + atau - : ")
#     a=int(input("Masukkan angka pertama : "))
#     b=int(input("Masukkan angka kedua : "))
#     if(operasi=="+"):
#         print(objek.jumlah(a,b))
#     elif(operasi=="-"):
#         print(objek.kurang(a,b))
# else:
#     perhitungan=input("Masukkan rentetan perhitungan : ")
def tambah_kurang(a):
    simbol = ["+", "-"]
    for s in simbol:
        for i in range(a.count(s)):
            index = a.index(s)
            if (s == "+"):
                result = float(a[index - 1]) + float(a[index + 1])
            else:
                result = float(a[index - 1]) - float(a[index + 1])
            for indek in [index + 1, index, index - 1]:
                a.pop(indek)
            a.insert(index - 1, result)
    return a

def kali_bagi(a):
    simbol = ["*", "/"]
    for s in simbol:
        for i in range(a.count(s)):
            index = a.index(s)
            if (s == "*"):
                result = float(a[index - 1]) * float(a[index + 1])
            else:
                result = float(a[index - 1]) / float(a[index + 1])
            for indek in [index + 1, index, index - 1]:
                a.pop(indek)
            a.insert(index - 1, result)
    tambah_kurang(a)
a=list("1+2-1*3/6")
if("*" in a or "/" in a):
    kali_bagi(a)
else:
    a=tambah_kurang(a)
print(float("".join(map(str,a))))