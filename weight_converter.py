import math
berat=int(input("weight: "))
satuan=input("(L)bs or (K)g: ")
if(satuan.lower()=='l'):
    hasil=berat*0.454
    satuan="kg"
elif(satuan.lower()=='k'):
    hasil=berat*2.205
    satuan="lbs"
print(f"You Are {format(hasil,'.5f')} {satuan}")