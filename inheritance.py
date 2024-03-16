class mamal:
    def walk(self):
        print("walk")


class dog(mamal):
    # Pass digunakan untuk class yang tidak memiliki method apapun
    pass


class cat(mamal):
    pass

dog_walk=dog()
cat_walk=cat()

dog_walk.walk()
cat_walk.walk()