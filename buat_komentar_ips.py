import random
import csv
with open('komentar_guru_IPS.csv','w',newline='')as file:
    writer=csv.writer(file)
    tahap = ['p', 'k']
    sma1 = ['a', 'b']
    sma2 = ['a', 'b']
    sma3 = ['a', 'b']
    matapelajaran=[1,2,3,4,5,6,7,8,9,10,15,16,17,18,19]
    komentar = ["Belajar lebih giat lagi", "Pertahankan prestasimu"]
    id_komen=5641

    # SMA-3
    for id in range(43,68):
        for mapel in matapelajaran:
            for semester in sma3:
                for fase in tahap:
                    writer.writerow([id_komen, mapel, id, 1, semester, fase,random.choice(komentar)])
                    id_komen += 1

    # SMA-2
    for id in range(105, 124):
        for mapel in matapelajaran:
            for semester in sma2:
                for fase in tahap:
                    writer.writerow([id_komen, mapel, id, 1, semester, fase,random.choice(komentar)])
                    id_komen += 1

    # SMA-1
    for id in range(155, 161):
        for mapel in matapelajaran:
            for semester in sma1:
                for fase in tahap:
                    writer.writerow([id_komen, mapel, id, 1, semester, fase,random.choice(komentar)])
                    id_komen += 1

    for id in range(167, 173):
        for mapel in matapelajaran:
            for semester in sma1:
                for fase in tahap:
                    writer.writerow([id_komen, mapel, id, 1, semester, fase,random.choice(komentar)])
                    id_komen += 1