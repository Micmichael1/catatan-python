import random
import csv
with open('Mapel_Umum.csv','w',newline='')as file:
    writer=csv.writer(file)
    tahap = ['h1', 'h2', 'us', 't1', 't2']
    sma1 = ['a', 'b']
    sma2 = ['a', 'b']
    sma3 = ['a', 'b']
    matapelajaran=[1,2,3,4,5,6,7,8,9,10,15]

    # SMA-3
    for id in range(12, 22):
        for mapel in matapelajaran:
            for semester in sma3:
                for fase in tahap:
                    writer.writerow([id, mapel, 1, semester, fase, random.randint(75, 100)])

    for id in range(28, 68):
        for mapel in matapelajaran:
            for semester in sma3:
                for fase in tahap:
                    writer.writerow([id, mapel, 1, semester, fase, random.randint(75, 100)])

    # SMA-2
    for id in range(68, 93):
        for mapel in matapelajaran:
            for semester in sma2:
                for fase in tahap:
                    writer.writerow([id, mapel, 1, semester, fase, random.randint(75, 100)])

    for id in range(105, 130):
        for mapel in matapelajaran:
            for semester in sma2:
                for fase in tahap:
                    writer.writerow([id, mapel, 1, semester, fase, random.randint(75, 100)])

    # SMA-1
    for id in range(130, 180):
        for mapel in matapelajaran:
            for semester in sma1:
                for fase in tahap:
                    writer.writerow([id, mapel, 1, semester, fase, random.randint(75, 100)])