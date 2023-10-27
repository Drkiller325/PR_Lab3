import requests
from bs4 import BeautifulSoup


def get_content():

    url = "http://127.0.0.1:5000/"

    response = requests.get(url)

    if response.status_code == 200:
        print("GET request successful!")

        soup = BeautifulSoup(response.text, 'html.parser')

    links = []
    visited = []
    for link in soup.find_all('a'):
        links.append(url + link.get('href'))
        visited.append(link.get('href'))
    for link in links:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        for tag in soup.find_all('a'):
            if tag.get('href') not in visited:
                links.append(url + tag.get('href'))
                visited.append(tag.get('href'))

        if link[-1].isnumeric():
            desc = {}
            l = soup.find_all('p')
            for item in l:
                index = item.text.index(":")
                desc[item.text[:index]] = item.text[index+2:]
            print(desc)

        else:
            print(f"{soup.find('h1').text} : {soup.find('p').text}")


get_content()