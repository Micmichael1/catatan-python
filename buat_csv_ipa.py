import random
import csv
with open('Mapel_IPA.csv','w',newline='')as file:
    writer=csv.writer(file)
    tahap = ['h1', 'h2', 'us', 't1', 't2']
    sma1 = ['a', 'b']
    sma2 = ['a', 'b']
    sma3 = ['a', 'b']
    matapelajaran=[11,12,13,14]

    # SMA-3
    for id in range(12, 22):
        for mapel in matapelajaran:
            for semester in sma3:
                for fase in tahap:
                    writer.writerow([id, mapel, 1, semester, fase, random.randint(75, 100)])

    for id in range(28, 43):
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


    # SMA-1
    for id in range(124, 155):
        for mapel in matapelajaran:
            for semester in sma1:
                for fase in tahap:
                    writer.writerow([id, mapel, 1, semester, fase, random.randint(75, 100)])

    for id in range(161, 167):
        for mapel in matapelajaran:
            for semester in sma1:
                for fase in tahap:
                    writer.writerow([id, mapel, 1, semester, fase, random.randint(75, 100)])

    for id in range(173, 180):
        for mapel in matapelajaran:
            for semester in sma1:
                for fase in tahap:
                    writer.writerow([id, mapel, 1, semester, fase, random.randint(75, 100)])
