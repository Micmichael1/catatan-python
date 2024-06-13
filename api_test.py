import requests

# Define the API endpoint
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=7D1LJEFN59GV1T10'

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()

    # Print the JSON data (for demonstration purposes)
    # print(data)

    # Work with the JSON data (for example, extracting specific fields)
    # For example, if the JSON data is a list of dictionaries:
    list_jenis = []
    for jenis in data:
        list_jenis.append(jenis)
    list_waktu = []
    for i in data[list_jenis[1]]:
        list_waktu.append(i)
    print(list(data[list_jenis[1]].keys()))
    for i in list_waktu:
        print(i)
        print(data[list_jenis[1]][i])
else:
    print(f"Failed to retrieve data: {response.status_code}")
