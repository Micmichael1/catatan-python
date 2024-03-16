def TakeCard(GraveYard)
import random
type=["Hearts","Diamonds","Spades","Clubs"]
number=["As",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
deck=[]
for types in type:
    for numbers in number:
        deck.append(str(numbers)+" "+types)
TotalPlayer=input('How many player is playing?')
GraveYard=[]
