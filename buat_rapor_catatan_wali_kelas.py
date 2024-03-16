import random
import csv
with open('rapor_catatan.csv','w',newline='')as file:
    writer=csv.writer(file)
    sma = ['a', 'b']
    komentar = ["Tingkatkan Prestasimu!!!","Pertahankan Prestasi Belajarmu!!!"]

    # SMA-3
    for id in range(12, 22):
        for semester in sma:
            writer.writerow([id, 1, semester, random.choice(komentar)])

    for id in range(28, 68):
        for semester in sma:
            writer.writerow([id, 1, semester, random.choice(komentar)])

    # SMA-2
    for id in range(68, 93):
        for semester in sma:
            writer.writerow([id, 1, semester, random.choice(komentar)])

    for id in range(105, 130):
        for semester in sma:
            writer.writerow([id, 1, semester, random.choice(komentar)])

    # SMA-1
    for id in range(130, 180):
        for semester in sma:
            writer.writerow([id, 1, semester, random.choice(komentar)])