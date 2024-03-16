number=input("Phone: ")
digits_mapping={
    "0":"zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine"
}

for index in number:
    # Apabila key tidak ada dalam dictionaries maka akan memunculkan !
    print(digits_mapping.get(index,"!"),end=" ")
print()
# map function
dum=[]
for i in number:
    dum+=i5
def translate(input):
    return digits_mapping[input]
print(' '.join(map(translate,dum)))

# map lambda
daftar=[]
for i in number:
    daftar += i
print(' '.join(map(lambda a:digits_mapping[a],daftar)))

