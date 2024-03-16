import random
import os
import time
from collections import Counter
class BlackJack:
    CardScore = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "Jack": 10,
        "Queen": 10,
        "King": 10,
    }
    def ReadCard(self,PlayerCard):
        value=[]
        for i in range (len(PlayerCard)):
            dummy=PlayerCard[i].split()
            value.append(dummy[0])
        return value

    def PlayerCountScore(self, PlayerCard):
        card=BlackJack.ReadCard(self,PlayerCard)
        DummyScore=0
        if(len(card)==2 and "As" in card and 10 in card):
            DummyScore=21.5
        else:
            for AsCard in range(card.count("As")):
                while(True):
                    print("What is the value of your As card?(1/11)")
                    AsScore=int(input())
                    if(AsScore==1 or AsScore==11):
                        DummyScore+=AsScore
                        break
                    else:
                        print("I don't understand That Command,try again")
            for i in card:
                DummyScore+=BlackJack.CardScore.get(i,0)
            if(DummyScore>=22):
                DummyScore=0
        return DummyScore

    def DealerCountScore(self,DealerCard):
        card = BlackJack.ReadCard(self, DealerCard)
        DummyScore=0
        if (len(card) == 2 and "As" in card and 10 in card):
            DummyScore=21.5
        else:
            for AsCard in range(card.count("As")):
                if(DummyScore+11>21):
                    DummyScore+=1
                else:
                    DummyScore+=11
            for i in card:
                DummyScore+=BlackJack.CardScore.get(i,0)
            if (DummyScore >= 22):
                DummyScore=0
        return DummyScore

    def startercard(self,deck,TakenCard):
        StarterCard=2
        dummy_list=[]
        while StarterCard>0:
            dummy=random.choice(deck)
            if(dummy not in TakenCard):
                dummy_list.append(dummy)
                TakenCard.append(dummy)
                StarterCard=StarterCard-1
        self.Card=dummy_list

    def AddCard(self,deck,TakenCard):
        takecard=1
        dummy_list=list(self.Card)
        while takecard>0:
            dummy=random.choice(deck)
            if(dummy not in TakenCard):
                dummy_list.append(dummy)
                TakenCard.append(dummy)
                takecard-=1
        self.Card=dummy_list

class Player(BlackJack):
    Name=""
    Bet=0
    Money=1000000
    PlayStatus=True
    Card=[]
    Score=0
    def __init__(self,PlayerName):
        self.Name=PlayerName


class Dealer(BlackJack):
    Card = []
    Score=0

def NamePlayer(TotalPlayer):
    PlayerDict=[]
    for i in range(1,TotalPlayer+1):
        os.system('cls')
        print("What Do People Call You, Player",i)
        PlayerName=input()
        if(PlayerName in PlayerDict):
            status=False
            while(not status):
                PlayerName=input("That Name Is Taken, Try Another Name\n")
                if(PlayerName not in PlayerDict):
                    status=True
        PlayerDict.append(PlayerName)
    return PlayerDict



def MakeCard():
    type=["Hearts","Diamonds","Spades","Clubs"]
    number=["As","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    deck=[]
    for types in type:
        for numbers in number:
            deck.append(str(numbers)+" "+types)
    return deck



def Main():
    os.system('cls')
    print('''
    Welcome To BlackJack\n
    How Many Player Are Playing Today?\n
    ''')
    TotalPlayer=int(input('Total Player : '))
    player=NamePlayer(TotalPlayer)
    deck=MakeCard()
    TakenCard=[]
    playerstop=0
    # instantiate Player
    for i in range(0,TotalPlayer):
        player[i]=Player(player[i])
    # instantiate Dealer
    dealer=Dealer()
    dealer.startercard(deck,TakenCard)
    # Begin game
    BJ = BlackJack()
    while(playerstop!=len(player)):
        # Player Draw Card Turn
        for i in range(0,TotalPlayer):
            if(player[i].PlayStatus):
                os.system('cls')
                print(f'{player[i].Name} Turn')
                time.sleep(1)
                Play=True
                while(True):
                    os.system('cls')
                    print(f'{player[i].Name} Credits : {player[i].Money}')
                    dummyBet=int(input("How Much do You Want To bet in this round?\n"))
                    if(dummyBet>player[i].Money):
                        print("You can't bet more than your credits")
                        time.sleep(2)
                    else:
                        player[i].Bet=dummyBet
                        break
                player[i].startercard(deck,TakenCard)
                while(Play):
                    os.system('cls')
                    print(f'Dealer Card : {dealer.Card[0]} , ?')
                    print(f'{player[i].Name} Card : {player[i].Card}')
                    choice=input("1.Hit\n2.Stay\n")
                    if(int(choice)==1):
                        player[i].AddCard(deck,TakenCard)
                    elif(int(choice)==2):
                        Play=False
                        player[i].Score=BJ.PlayerCountScore(player[i].Card)
                    else:
                        print("I don't understand That Command,try again")
                        time.sleep(2)
        # Dealer Draw Card Turn
        os.system('cls')
        while (BJ.DealerCountScore(dealer.Card)<=16):
            dealer.AddCard(deck,TakenCard)
        dealer.Score=dealer.DealerCountScore(dealer.Card)

        # Player Score vs Dealer Score
        for i in range(0,TotalPlayer):
            if(player[i].PlayStatus):
                print(f'{player[i].Name} card : {player[i].Card}')
                print("Dealer Card : ",end="")
                for dc in (dealer.Card):
                    EndMark=" , "
                    if(dc==dealer.Card[len(dealer.Card)-1]):
                        EndMark="\n"
                    print(dc,end=EndMark)
                    time.sleep(1)
                if(player[i].Score>dealer.Score):
                    if(player[i].Score==21.5):
                        player[i].Money+=player[i].Bet*int((3/2))
                    else:
                        player[i].Money+=player[i].Bet
                    print("You win!!!")
                elif(player[i].Score==dealer.Score):
                    print("Its A draw!!!")
                    pass
                else:
                    player[i].Money-=player[i].Bet
                    print("You Lose!!!")
                # Ask Continue
                while (True):
                    if(player[i].Money==0):
                        print("You have gone bankrupt.You can't continue to play")
                        player[i].PlayStatus = False
                        playerstop += 1
                        break
                    else:
                        print(f'{player[i].Name} Credits : {player[i].Money}\nContinue Playing {player[i].Name} (Y/N)?')
                        playStatus = input().upper()
                        if (playStatus == "N"):
                            player[i].PlayStatus = False
                            playerstop += 1
                            break
                        elif (playStatus == "Y"):
                            break
                        else:
                            print("I don't understand That Command,try again")

Play=True
while(Play):
    Main()
    while(True):
        playagain=input("Do You Wanna Start Over Again?(Y/N)").upper()
        if(playagain=="N"):
            Play=False
            break
        elif(playagain=="Y"):
            break
        else:
            print("I Don't Understand that command")
print("Thank You For Playing!!!")