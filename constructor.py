class Point:
    # membuat costructor yang menerima parameter
    def __init__(self,x,y):
        # self merupakan object yang kita pakai nantinya untuk memanggil class
        self.x=x
        self.y=y

    def move(self):
        print("move",self.x)
    def draw(self):
        print("draw",self.y)

# Membuat object dan mengirim argumen menuju class yang akan diolah oleh constructor
point=Point(10,20)
# Mengubah atribut(variable) constructor
point.x=11
# Memanggil variable x dan y
print(point.x,point.y)
point.move()
point.draw()