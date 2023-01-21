import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes"
response = requests.get(url)
content = BeautifulSoup(response.text, "html.parser")
episodes = []
ep_tables = content.find_all('table', class_='wikiepisodetable')

for table in ep_tables:
    headers = []
    rows = table.find_all('tr')
    # get headers
    for header in table.find('tr').find_all('th'):
        headers.append(header.text)
    # get rows
    for row in table.find_all('tr')[1:]:
        values = []
        # get values
        for col in row.find_all(['th', 'td']):
            values.append(col.text)
        # merge headers and values
        if values:
            episodes_dict = {headers[val]: values[val] for val in range(len(values))}
            episodes.append(episodes_dict)

for ep in episodes:
    print(ep)
