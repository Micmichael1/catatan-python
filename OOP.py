class car():
    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model
    def promote(self):
        print(self.brand,self.model)
    
    def secret(self):
        pass

class electric_car(car):
    def __init__(self, brand="tesla", model="tesla", battery="tesla") -> None:
        super().__init__(brand, model)
        self.battery = battery

    def promote(self):
        print(self.brand,str(self.battery),self.model)

    def secret(self):
        print("Bisa Berjalan Di Air")

class bekerja():
    def __init__(self,car) -> None:
        car.promote()
        car.secret()

jenis = [car("Mazda","RX8"),electric_car("tesla",model='Truck',battery='8V')]
for rekursif_jenis in jenis:
    bekerja(rekursif_jenis)
    print("Kita masuk reset")