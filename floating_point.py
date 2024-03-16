test=2.56*7.89
# metode format() akan membulatkan floatnya hingga precision yang ditentukan
print(format(test,'.50f'))
print('{:.2f}'.format(test))
angka=1
print('{:03d}'.format(angka))
# metode round() juga akan membulatkan floatnya hingga precision yang ditentukan
test1=round(1.239567890,50)
print(test1)