class A:
    def __init__(self,umur,stambuk):
        self.umur=umur
        print(self.umur)
        self.umur+=1
        self.stambuk=stambuk
        print(self.stambuk)
        self.stambuk += 1
    def __str__(self):
        return str(self.stambuk)
class B(A):
    def __init__(self,depan,belakang,umur,stambuk):
        self.depan=depan
        print(self.depan)
        self.depan+="s"
        self.belakang=belakang
        print(self.belakang)
        self.belakang+="s"
        super().__init__(umur,stambuk)

test = B('Michael','lim',20,2019)

# Memanggil __str__ pada class A (bisa dikarenakan class b inheritence class a)
print(test)

print(test.depan,test.belakang,test.umur,test.stambuk)

# class A:
#     angka = 69
#     def kelas(self):
#         return 'Mike'
#
# class B(A):
#     def __init__(self):
#         print(super().angka)
#         print(super().kelas())
#
# kelas = B()
# print(kelas.angka)