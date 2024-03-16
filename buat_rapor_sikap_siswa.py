import random
import csv
with open('rapor_sikap.csv','w',newline='')as file:
    writer=csv.writer(file)
    sma = ['a', 'b']
    tipe = ['spiritual','sosial']
    predikat = ['a','b','c']
    spirit = {'a':'Menunjukkan sikap yang sangat baik dalam beribadah (berdoa, memuji Tuhan, membaca dan merenungkan firman Tuhan dalam Alkitab) di sekolah dan gereja',
              'b':'Menunjukkan sikap yang baik dalam beribadah (berdoa, memuji Tuhan, membaca dan merenungkan firman Tuhan dalam Alkitab) di sekolah dan gereja',
              'c':'Menunjukkan sikap yang cukup baik dalam beribadah (berdoa, memuji Tuhan, membaca dan merenungkan firman Tuhan dalam Alkitab) di sekolah dan gereja',
    }
    soci = {'a':'Sangat baik dan disiplin dan dalam hal berinteraksi secara efektif dengan lingkungan socail dan alam dalam jangkauan pergaulan serta keberadaanya',
            'b':'Baik dan disiplin dan dalam hal berinteraksi secara efektif dengan lingkungan socail dan alam dalam jangkauan pergaulan serta keberadaanya',
            'c':'Cukup baik dan disiplin dan dalam hal berinteraksi secara efektif dengan lingkungan socail dan alam dalam jangkauan pergaulan serta keberadaanya'}

    #spirit
    # SMA-3
    for id in range(12, 22):
        for semester in sma:
            dum = random.choice(predikat)
            writer.writerow([id, 1, semester, tipe[0], dum, spirit[dum]])

    for id in range(28, 68):
        for semester in sma:
            dum = random.choice(predikat)
            writer.writerow([id, 1, semester, tipe[0], dum, spirit[dum]])

    # SMA-2
    for id in range(68, 93):
        for semester in sma:
            dum = random.choice(predikat)
            writer.writerow([id, 1, semester, tipe[0], dum, spirit[dum]])

    for id in range(105, 130):
        for semester in sma:
            dum = random.choice(predikat)
            writer.writerow([id, 1, semester, tipe[0], dum, spirit[dum]])

    # SMA-1
    for id in range(130, 180):
        for semester in sma:
            dum = random.choice(predikat)
            writer.writerow([id, 1, semester, tipe[0], dum, spirit[dum]])




    #sosial
    for id in range(12, 22):
        for semester in sma:
            dum = random.choice(predikat)
            writer.writerow([id, 1, semester, tipe[1], dum, soci[dum]])

    for id in range(28, 68):
        for semester in sma:
            dum = random.choice(predikat)
            writer.writerow([id, 1, semester, tipe[1], dum, soci[dum]])

    # SMA-2
    for id in range(68, 93):
        for semester in sma:
            dum = random.choice(predikat)
            writer.writerow([id, 1, semester, tipe[1], dum, soci[dum]])

    for id in range(105, 130):
        for semester in sma:
            dum = random.choice(predikat)
            writer.writerow([id, 1, semester, tipe[1], dum, soci[dum]])

    # SMA-1
    for id in range(130, 180):
        for semester in sma:
            dum = random.choice(predikat)
            writer.writerow([id, 1, semester, tipe[1], dum, soci[dum]])

