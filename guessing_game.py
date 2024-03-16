ans=9
chance=3
while(chance!=0):
    guess=int(input("Guess a number (1-10) You have 3 chance:"))
    if(guess==ans):
        print("You Win!!!You win with",chance,"chance left")
        break
    chance -= 1
else:
    print("You Lose!!! The Answer is",ans)
