class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f'Hello my name is {self.name}')

michael=Person("Michael")
michael.talk()

michelle=Person("Michelle")
michelle.talk()