status = False
while True:
    order = input(">").lower()
    if (order == "help"):
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
        # print("start - to start the car\nstop - to stop the car\nquit - to exit the car")
    elif(order == "start"):
        if status:
            print("Car already started.You don't need to start it again")
        else:
            print("Car Started...Ready to go!")
            status = True
    elif(order == "stop"):
        if status:
            print("Car stopped")
            status = False
        else:
            print("Car already stopped.You don't need to stop it again")
    elif (order == "quit"):
        break
    else:
        print("I don't understand that")


