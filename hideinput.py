from getpass import getpass
password=getpass(prompt='Input Password : ')
try:
    if(len(password)>1):
        raise Exception("Panjang kali tott")
except Exception as e:
    print(e)