import random
import csv
with open('komentar_guru.csv','w',newline='')as file:
    writer=csv.writer(file)
    id=1
    id_guru=[93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104,180,181,182,183,184]
    semester = ['a', 'b']
    fase=['h1','h2']
    komentar="Tingkatkan Prestasimu!!!"
    kerajinan=['a','b','c','d']
    kesopanan=['a','b','c','d']
    kerapian=['a','b','c','d']
    dummy=0
    for id_siswa in range(12, 22):
        for semesters in semester:
            for fase_siswa in fase:
                    writer.writerow([id,id_siswa,id_guru[dummy],1,semesters,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
                    id=id+1
    for id_siswa in range(28, 30):
        for semesters in semester:
            for fase_siswa in fase:
                    writer.writerow([id,id_siswa,id_guru[dummy],1,semesters,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
                    id=id+1
    dummy+=1

    for id_siswa in range(30, 43):
        for semesters in semester:
            for fase_siswa in fase:
                    writer.writerow([id,id_siswa,id_guru[dummy],1,semesters,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
                    id=id+1
    dummy+=1

    for id_siswa in range(43, 55):
        for semesters in semester:
            for fase_siswa in fase:
                    writer.writerow([id,id_siswa,id_guru[dummy],1,semesters,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
                    id=id+1
    dummy+=1

    for id_siswa in range(55, 68):
        for semesters in semester:
            for fase_siswa in fase:
                    writer.writerow([id,id_siswa,id_guru[dummy],1,semesters,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
                    id=id+1
    dummy+=1

    for id_siswa in range(68, 80):
        for semesters in semester:
            for fase_siswa in fase:
                    writer.writerow([id,id_siswa,id_guru[dummy],1,semesters,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
                    id=id+1
    dummy+=1

    for id_siswa in range(80, 87):
        for semesters in semester:
            for fase_siswa in fase:
                    writer.writerow([id,id_siswa,id_guru[dummy],1,semesters,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
                    id=id+1
    dummy+=1

    for id_siswa in range(87, 92):
        for semesters in semester:
            for fase_siswa in fase:
                    writer.writerow([id,id_siswa,id_guru[dummy],1,semesters,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
                    id=id+1
    dummy+=1

    for id_siswa in range(105, 111):
        for semesters in semester:
            for fase_siswa in fase:
                    writer.writerow([id,id_siswa,id_guru[dummy],1,semesters,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
                    id=id+1
    dummy+=1

    for id_siswa in range(111, 117):
        for semesters in semester:
            for fase_siswa in fase:
                    writer.writerow([id,id_siswa,id_guru[dummy],1,semesters,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
                    id=id+1
    dummy+=1

    for id_siswa in range(117, 124):
        for semesters in semester:
            for fase_siswa in fase:
                    writer.writerow([id,id_siswa,id_guru[dummy],1,semesters,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
                    id=id+1
    dummy+=1

    for id_siswa in range(124, 130):
        for semesters in semester:
            for fase_siswa in fase:
                    writer.writerow([id,id_siswa,id_guru[dummy],1,semesters,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
                    id=id+1
    dummy+=1

    for id_siswa in range(130, 142):
        for semesters in semester:
            for fase_siswa in fase:
                    writer.writerow([id,id_siswa,id_guru[dummy],1,semesters,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
                    id=id+1
    dummy+=1

    for id_siswa in range(142, 155):
        for semesters in semester:
            for fase_siswa in fase:
                    writer.writerow([id,id_siswa,id_guru[dummy],1,semesters,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
                    id=id+1
    dummy+=1

    for id_siswa in range(155, 161):
        for semesters in semester:
            for fase_siswa in fase:
                    writer.writerow([id,id_siswa,id_guru[dummy],1,semesters,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
                    id=id+1
    dummy+=1

    for id_siswa in range(161, 167):
        for semesters in semester:
            for fase_siswa in fase:
                    writer.writerow([id,id_siswa,id_guru[dummy],1,semesters,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
                    id=id+1
    dummy+=1

    for id_siswa in range(167, 173):
        for semesters in semester:
            for fase_siswa in fase:
                    writer.writerow([id,id_siswa,id_guru[dummy],1,semesters,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
                    id=id+1
    dummy+=1

    for id_siswa in range(173, 180):
        for semesters in semester:
            for fase_siswa in fase:
                    writer.writerow([id,id_siswa,id_guru[dummy],1,semesters,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
                    id=id+1
    # # SMA-3 IPA-1
    # for id_siswa in range(12, 22):
    #     for semester in sma3:
    #         for fase_siswa in fase:
    #                 writer.writerow([id,id_siswa,id_guru,1,semester,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
    #                 id=id+1
    #
    # for id_siswa in range(28, 30):
    #     for semester in sma3:
    #         for fase_siswa in fase:
    #                 writer.writerow([id,id_siswa,id_guru,semester,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
    #                 id=id+1
    # id_guru = id_guru+1
    #
    # # SMA-3 IPA-2
    # for id_siswa in range(30, 43):
    #     for semester in sma3:
    #         for fase_siswa in fase:
    #                 writer.writerow([id,id_siswa,id_guru,semester,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
    #                 id=id+1
    # id_guru = id_guru+1
    #
    # # SMA-3 IPS-1
    # for id_siswa in range(43, 55):
    #     for semester in sma3:
    #         for fase_siswa in fase:
    #                 writer.writerow([id,id_siswa,id_guru,semester,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
    #                 id=id+1
    # id_guru = id_guru+1
    #
    # # SMA-3 IPS-2
    # for id_siswa in range(55, 68):
    #     for semester in sma3:
    #         for fase_siswa in fase:
    #                 writer.writerow([id,id_siswa,id_guru,semester,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
    #                 id=id+1
    # id_guru = id_guru+1
    #
    # # SMA-2 IPA-1
    # for id_siswa in range(68, 80):
    #     for semester in sma2:
    #         for fase_siswa in fase:
    #                 writer.writerow([id,id_siswa,id_guru,semester,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
    #                 id=id+1
    # id_guru = id_guru+1
    #
    # # SMA-2 IPA-2
    # for id_siswa in range(80, 93):
    #     for semester in sma2:
    #         for fase_siswa in fase:
    #                 writer.writerow([id,id_siswa,id_guru,semester,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
    #                 id=id+1
    # id_guru = id_guru+1
    #
    # # SMA-2 IPS-1
    # for id_siswa in range(105, 117):
    #     for semester in sma2:
    #         for fase_siswa in fase:
    #                 writer.writerow([id,id_siswa,id_guru,semester,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
    #                 id=id+1
    # id_guru = id_guru+1
    #
    # # SMA-2 IPS-2
    # for id_siswa in range(117, 130):
    #     for semester in sma2:
    #         for fase_siswa in fase:
    #                 writer.writerow([id,id_siswa,id_guru,semester,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
    #                 id=id+1
    # id_guru = id_guru+1
    #
    # # SMA-1 IPA-1
    # for id_siswa in range(130, 142):
    #     for semester in sma1:
    #         for fase_siswa in fase:
    #                 writer.writerow([id,id_siswa,id_guru,semester,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
    #                 id=id+1
    # id_guru = id_guru+1
    #
    # # SMA-1 IPA-2
    # for id_siswa in range(142, 155):
    #     for semester in sma1:
    #         for fase_siswa in fase:
    #                 writer.writerow([id,id_siswa,id_guru,semester,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
    #                 id=id+1
    # id_guru = id_guru+1
    #
    # # SMA-1 IPS-1
    # for id_siswa in range(155, 167):
    #     for semester in sma1:
    #         for fase_siswa in fase:
    #                 writer.writerow([id,id_siswa,id_guru,semester,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
    #                 id=id+1
    # id_guru = id_guru+1
    #
    # # SMA-1 IPS-2
    # for id_siswa in range(167, 180):
    #     for semester in sma1:
    #         for fase_siswa in fase:
    #                 writer.writerow([id,id_siswa,id_guru,semester,fase_siswa,komentar,random.choice(kerajinan),random.choice(kesopanan),random.choice(kerapian)])
    #                 id=id+1
    # id_guru = id_guru+1