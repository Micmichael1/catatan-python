try:
    angka=input("Masukkan Sebuah Angka : ")
    print("{:.0f}".format(int(angka)/1))
except TypeError:
    print("Masukkan Sebuah Angka Loh Cokkkk")
try:
    huruf=input("Masukkan satu huruf : ")
    if(len(huruf)>1):
        raise Exception("Satu huruf ajalah cokkkk")
except Exception as e:
    print(e)
# angka=1/3
# print("{:0.2f}".format(angka))