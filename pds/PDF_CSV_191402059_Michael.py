# Mengambil data per baris sesuai dengan jumlah kolom per table
# Kemudian memasukkan ke list per table yang nantinya akan digabungkan dengan table lainnya
def split_line(columns, page, list_per_table) :
    page = page[:-1]
    for part in range(len(page) // columns) :
        list_per_line = []
        for i in range(columns) :
            list_per_line.append(page[part * columns + i])
        list_per_table.append(list_per_line)
    return list_per_table

# Mengambil data dari pdf dan kemudian dikirim ke fungsi split_line untuk dimasukkan kedalam list
from PyPDF2 import PdfFileReader
pdf_document = "ObesityAnalysis.pdf"
with open(pdf_document, "rb") as filehandle:
    pdf = PdfFileReader(filehandle)
    # Menampung data perbaris semua table
    all_table_list=[]
    # Menampung data sementara perbaris,pertable
    list_per_table=[]
    # Batas-batas halaman per table
    batas_halaman=[0,160,320,480,640]
    # Jumlah column per table
    columns_per_table=[7,9,8,8]
    for i in range(4):
        for page in range(batas_halaman[i],batas_halaman[i+1]):
            pages = pdf.getPage(page)
            halaman=pages.extractText().split("\n")
            list_per_table=split_line(columns_per_table[i], halaman, list_per_table)
        if(len(all_table_list)==0):
            all_table_list=list(list_per_table)
        else:
            # Menggabungkan data per table dengan data semua table
            for baris in range(len(all_table_list)):
                all_table_list[baris]= all_table_list[baris] + list_per_table[baris]
        list_per_table=[]

# Menuliskan list yang berisi data perbaris semua table yang sudah digabungkan ke csv
import csv
with open("191402059_Michael_CSV.csv", 'w',newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for i in range(len(all_table_list)):
        csvwriter.writerow(all_table_list[i])
print("done")