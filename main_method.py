class kalkulator:
    Nama=""
    def __init__(self,Nama):
        self.Nama=Nama
        print("Selamat Datang", self.Nama)

    def jumlah(self,a,b):
        print("Halo "+self.Nama)
        return a+b

    def kurang(self,a,b):
        print("Halo " + self.Nama)
        return a-b