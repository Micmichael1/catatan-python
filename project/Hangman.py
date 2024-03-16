import random
import os
import time
def ShowAnswer(blank):
    # Menampilkan jawaban
    print(end=" ")
    for i in range(len(blank)):
        print(blank[i], end=" ")
    print()
os.system('cls')
string=["michael","lim"]
blank=[]
answer=random.choice(string)
# Membuat blank kosong
for i in range(len(answer)):
    blank.append("_")
chance=3
while(chance!=0):
    os.system('cls')
    ShowAnswer(blank)
    print(f'You have {chance} chance left')
    try:
        tebakan=input("Letter Of Your Guess : ").lower()
        if(len(tebakan)>1):
            raise Exception("Only One Letter Per Input Is Allowed")
    except Exception as e:
        print(e)
        time.sleep(3)
        continue
    if(tebakan in answer):
        if(tebakan in blank):
            try:
                raise Exception("You have try that guess, try another guess")
            except Exception as e:
                print(e)
                time.sleep(3)
                continue
        for i in range(answer.count(tebakan)):
            blank[answer.index(tebakan)]=tebakan
    else:
        chance-=1
    if("_" not in blank):
        ShowAnswer(blank)
        print('\nYou Winnn')
        break
else:
    print("\nYou Loseee")
