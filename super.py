class A():
    def tambah(self):
        self.test="Mantap"

class B(A):
    test=0
    def method(self):
        super().tambah()
        print(self.test)

dum = B()
dum.method()

