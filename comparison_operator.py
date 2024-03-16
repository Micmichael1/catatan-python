name=input("Please enter Your Name:")
if(len(name)<3):
    print("Name Must Be At Least 3 Characters")
elif(len(name)>50):
    print("Name Can Be a Maximum Of 50 Characters")
else:
    print("Name Looks Good!")