numbers=[0,0,1,2,2,3,3,4,5,1,5]
for dummy in numbers:
    while(numbers.count(dummy)>1):
        numbers.pop(numbers.index(dummy,numbers.index(dummy)+1))

print(numbers)
