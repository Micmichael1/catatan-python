# Cara 1
# Menghilangkan angka duplikat pertama
numbers=[0,0,1,2,2,3,3,4,5,1,5]
for item in numbers:
    while(numbers.count(item)>1):
        numbers.remove(item)
print(numbers)

# Cara 2
# Menghilangkan angka duplikat selain duplikat pertama
numbers=[0,0,1,2,2,3,3,4,5,1,5,1,5,2,3,4,5]
for item in numbers:
    while(numbers.count(item)>1):
        numbers.pop(numbers.index(item,numbers.index(item)+1))
print(numbers)

# Cara 3
numbers=[0,0,1,2,2,3,3,4,5,1,5,1,5,2,3,4,5]
uniques =[]
for number in numbers :
    if(number not in uniques):
        uniques.append(number)
print(uniques)
