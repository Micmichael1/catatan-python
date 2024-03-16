# Membuat class
# Huruf pertama setiap kata di nama class wajib menggunakan huruf besar
# Apabila lebih dari satu kata maka namanya disambung dengan huruf besar pada tiap huruf awal
# contoh:PointAwal
class Point:
    # Membuat method
    def move(self):
        print("move")
        print("Ini x",self.x)
    def draw(self):
        print("draw")
# Membuat object class point yaitu point1
point1=Point()
# Memanggil method dengan menggunakan object
point1.draw()
# Object dapat memiliki variable yang khusus berlaku untuk variable tersebut
point1.x=10
point1.y=20
print(point1.x,point1.y)
point1.move()
point2=Point()
# variable x tidak akan dikenal di object point2
# print(point2.x)

class Coba:
    def cobakuy(self,a):
        print(a)
object=Coba()
object.cobakuy('ini kelas Coba')
