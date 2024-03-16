import random
class dice:
    def roll(self):

        #Cara ke-1
        hasil=(random.randint(1,6),random.randint(1,6))
        return hasil

        #Cara Ke-2
        # pertama=random.randint(1,6)
        # kedua=random.randint(1,6)
        # return pertama,kedua
        # Langsung me-return dua value tersebut tanpa membuatnya menjadi tuple terlebih dahulu adalah legal
        # Phyton sudah memahami bahwa itu adalah tuple sehingga tidak perlu kita definsikan lagi

objek=dice()
print(objek.roll())