number=[10,1,2,3,4,5,6,7,8,9]
# print(max(number))
max=number[0]
for x in number:
    if(max<x):
        max=x
print(max)
