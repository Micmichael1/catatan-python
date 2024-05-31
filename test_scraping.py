import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the Wikipedia page you want to scrape
url = 'https://id.wikipedia.org/wiki/Daftar_kota_di_Indonesia'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the main content of the page (usually within <div id="content"> or <div class="mw-parser-output">)
    content = soup.find(id='bodyContent')  # You may need to inspect the page source to find the appropriate element
    list_kota = []
    table = content.find('table', class_='nowraplinks mw-collapsible autocollapsed navbox-inner')
    kota = table.find_all('li')
    link_kotor = []
    link_bersih = []
    combine_kota_link = []

    # clean code untuk kota
    for i in kota:
        link_kotor.append(i.find_all('a', href=True))
        list_kota.append(i.text)
        # print(i.text)
    list_kota = list_kota[3:]


    # clean code untuk link
    # print(link_kotor[0][0]['href'])
    for satu in link_kotor:
        # print(satu)
        for dua in satu:
            # print(dua)
            link_bersih.append("https://id.wikipedia.org/"+dua['href'])

    dict_kota_dan_link = dict(zip(list_kota, link_bersih))
    print(dict_kota_dan_link)

    for i in dict_kota_dan_link:
        combine_kota_link.append(i+","+dict_kota_dan_link[i])

    print(combine_kota_link)

    # Define the CSV file name
    # csv_file_name = 'wikipedia_table.csv'
    # Write the data to a CSV file
    # with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
    #     writer = csv.DictWriter(file, fieldnames=['kota','links'])
    #     writer.writeheader()
    #     for row in dict_kota_dan_link:
    #         writer.writerow(row)

    # Extract the desired data from the content
    # For example, let's extract the title of the page
    # title = content.find('h1').text
    # table = content.find('table', class_='wikitable sortable')
    # print(i.text.strip() for i in content.find_all('p'))
    # for element in content.find_all(['p', 'h2', 'h3', 'ul', 'ol', 'table']):
    #     print(element.text.strip())
    # print('Title:', title)

    # Let's extract the first paragraph of the main content
    # first_paragraph = content.find('p').text
    # print('First paragraph:', first_paragraph)
# if response.status_code == 200:
#     # Parse the HTML content of the page using BeautifulSoup
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     # Find the first table in the main content of the page
#     table = soup.find('table', class_='wikitable')
#
#     # Extract the table headers
#     headers = [header.text.strip() for header in table.find_all('th')]
#
#     # Extract the table rows
#     rows = table.find_all('tr')[1:]  # Skip the header row
#
#     # Extract the table data and store it in a list of dictionaries
#     table_data = []
#     for row in rows:
#         cells = row.find_all(['td', 'th'])
#         cell_data = [cell.text.strip() for cell in cells]
#         row_dict = dict(zip(headers, cell_data))
#         table_data.append(row_dict)
#
#     # Print the table data
#     for row in table_data:
#         print(row)
else:
    print('Failed to fetch the page:', response.status_code)
