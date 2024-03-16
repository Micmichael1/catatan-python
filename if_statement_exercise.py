# Cara Pertama
good_credit=True
put_down10=int(1000000*0.1)
if(good_credit):
    print("They Need To Put Down",put_down10)
else:
    print(f'They Need To Put Down {int(1000000*0.2)}')

# Cara Kedua
price=1000000
has_good_credit=True
if has_good_credit:
    down_payment=0.1*price
else:
    down_payment=0.2*price
print(f"Down Payment:${int(down_payment)}")
