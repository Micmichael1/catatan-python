high_income=False
good_credit=False

if (high_income and good_credit):
    print("Full True")
elif (high_income or good_credit):
    print("Half True")
else :
    print("False")


high_income=True
criminal_record=False

# Fungsi "and not" mirip dengan fungsi and dimana kedua statement harus true akan tetapi pada and not, statement yang berada dibelakang akan di reverse isinya contoh:
# Pada Statement diatas, criminal_record memiliki isi False dan ketika dimasukkan ke dalam fungsi and not maka criminal record akan menjadi True dan membuat statement tersebut menjadi true and true dan bisa dijalankan
if(high_income and not criminal_record):
    print("Punya High_Income dan Tidak Ada criminal record")
criminal_record=True
# Criminal record di negasikan menjadi false sehingga fungsi and dibawah tidak akan dijalankan/tidak dapat berjalan
if(high_income and not criminal_record):
    print("Punya High Income Dan Criminal Record")