import random
import csv
with open('rapor_ketidakhadiran.csv','w',newline='')as file:
    writer=csv.writer(file)
    sma = ['a', 'b']
    sakit = [0,0,0,0,0,0,0,0,1,2,3]
    izin = [0,0,0,0,0,0,0,0,1,2,3]
    alpha = [0,0,0,0,0,0,0,0,1,2,3]

    # SMA-3
    for id in range(12, 22):
        for semester in sma:
            writer.writerow([id, 1, semester, random.choice(sakit), random.choice(izin), random.choice(alpha)])

    for id in range(28, 68):
        for semester in sma:
            writer.writerow([id, 1, semester, random.choice(sakit), random.choice(izin), random.choice(alpha)])

    # SMA-2
    for id in range(68, 93):
        for semester in sma:
            writer.writerow([id, 1, semester, random.choice(sakit), random.choice(izin), random.choice(alpha)])

    for id in range(105, 130):
        for semester in sma:
            writer.writerow([id, 1, semester, random.choice(sakit), random.choice(izin), random.choice(alpha)])

    # SMA-1
    for id in range(130, 180):
        for semester in sma:
            writer.writerow([id, 1, semester, random.choice(sakit), random.choice(izin), random.choice(alpha)])