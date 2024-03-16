# Penghitungan Kmeans dengan data yang dimasukkan manual ke dalam codingan
# Data dengan dimensi X,Y,Z serta 3 cluster (bisa ditambah dengan sedikit modifikasi)

import random
import math
Perulangan = 0

# Data Bisa Diubah
Data = [[89, 90, 75], [90, 71, 95], [70, 75, 80], [45, 65, 59], [65, 75, 53], [80, 70, 75], [90, 85, 81], [70, 70, 73],
        [96, 93, 85], [60, 55, 48], [45, 60, 58], [60, 70, 72], [85, 90, 88], [52, 68, 55], [40, 60 ,70]]
# Data = [[2, 0, 1], [1, 3, 1], [3, 5, 1], [2, 2, 1], [4, 6, 1]]
Centroid=[]
# Centroid = [[45, 60, 58], [60, 70, 72], [85, 90, 88]]
# Centroid = [[89, 90, 75], [90, 71, 95], [70, 75, 80]]
while len(Centroid) != 3:
    dum=Data[random.randint(0,len(Data) - 1)]
    if dum not in Centroid:
        Centroid.append(dum)
    elif dum in Centroid:
        continue
# Centroid = [[2, 0, 1], [1, 3, 1], [3, 5, 1]]

# print(Data[0].index(min(Data[0])))    Cari index data terkecil dari array 2D

# Pilih Centroid secara Random (jumlah centroid/cluster bisa diubah untuk skrng pakai 2 cluster)
# while len(Centroid) != 3:
#     dum=Data[random.randint(0,len(Data) - 1)]
#     if dum not in Centroid:
#         Centroid.append(dum)
#     elif dum in Centroid:
#         continue

print("Centroid Awal :", Centroid)

# Mulai penghitungan Kmeans
while True:
    Perulangan = Perulangan + 1
    print("Perulangan ke :", Perulangan)
    print("Centroid Yang Dipakai :", Centroid)

    # A adalah Cluster 1
    A = []

    # B adalah Cluster 2
    B = []

    # C adalah Cluster 3
    C = []

    ScrapEcludian = []

    # Hitung Ecludian Distance untuk pengelompokkan ke cluster terdekat yang mana
    # (Jika jumlah cluster diubah maka disini perlu ditambah)
    DataKe=0
    for d in Data:
        centroidA = math.sqrt((math.pow(d[0] - Centroid[0][0], 2)) + (math.pow(d[1] - Centroid[0][1], 2)) + (math.pow(d[2] - Centroid[0][2], 2)))
        centroidB = math.sqrt((math.pow(d[0] - Centroid[1][0], 2)) + (math.pow(d[1] - Centroid[1][1], 2)) + (math.pow(d[2] - Centroid[1][2], 2)))
        centroidC = math.sqrt((math.pow(d[0] - Centroid[2][0], 2)) + (math.pow(d[1] - Centroid[2][1], 2)) + (math.pow(d[2] - Centroid[2][2], 2)))
        ScrapEcludian.append([centroidA,centroidB,centroidC])
        if(ScrapEcludian[DataKe].index(min(ScrapEcludian[DataKe]))==0):
            A.append(d)
        elif(ScrapEcludian[DataKe].index(min(ScrapEcludian[DataKe]))==1):
            B.append(d)
        elif(ScrapEcludian[DataKe].index(min(ScrapEcludian[DataKe]))==2):
            C.append(d)
        DataKe+=1
    print("Team A :", A)
    print("Team B :", B)
    print("Team C :", C)
    print("Scrap :", ScrapEcludian)

    # Hitung Means
    # (Jika jumlah cluster diubah maka disini perlu ditambah)
    XTotalA = 0
    YTotalA = 0
    ZTotalA = 0
    XTotalB = 0
    YTotalB = 0
    ZTotalB = 0
    XTotalC = 0
    YTotalC = 0
    ZTotalC = 0

    for i in A:
        XTotalA = XTotalA + i[0]
        YTotalA = YTotalA + i[1]
        ZTotalA = ZTotalA + i[2]
    for i in B:
        XTotalB = XTotalB + i[0]
        YTotalB = YTotalB + i[1]
        ZTotalB = ZTotalB + i[2]
    for i in C:
        XTotalC = XTotalC + i[0]
        YTotalC = YTotalC + i[1]
        ZTotalC = ZTotalC + i[2]

    XMeanA = XTotalA / len(A)
    YMeanA = YTotalA / len(A)
    ZMeanA = ZTotalA / len(A)

    XMeanB = XTotalB / len(B)
    YMeanB = YTotalB / len(B)
    ZMeanB = ZTotalB / len(B)

    XMeanC = XTotalC / len(C)
    YMeanC = YTotalC / len(C)
    ZMeanC = ZTotalC / len(C)

    DumCentroid = []
    DumCentroid.append([XMeanA, YMeanA, ZMeanA])
    DumCentroid.append([XMeanB, YMeanB, ZMeanB])
    DumCentroid.append([XMeanC, YMeanC, ZMeanC])

    if((Centroid[0] == DumCentroid[0] or Centroid[1] == DumCentroid[0] or Centroid[2] == DumCentroid[0]) and
            (Centroid[0] == DumCentroid[1] or Centroid[1] == DumCentroid[1] or Centroid[2] == DumCentroid[1]) and
            (Centroid[0] == DumCentroid[2] or Centroid[1] == DumCentroid[2] or Centroid[2] == DumCentroid[2])):
        print("Final :", Centroid)
        break

    else:
        Centroid = DumCentroid
        print("Centroid :", Centroid, "\n")
