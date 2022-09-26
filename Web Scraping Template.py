from bs4 import BeautifulSoup
import requests

URL = "path"
r = requests.get(URL)
print(r.content)

soup = BeautifulSoup(r.content, 'lxml')
print(soup.prettify())

feature1 = soup.find_all('div', {'class': ''})
feature2 = soup.find_all('a', {'itemprop': ''})
feature3 = soup.find_all('a', {'class': ''})

fet1 = []
fet2 = []
fet3 = []


for r in range(len(repos)):
    fet1.append(feature1[r].text)
    fet2.append(feature2[r].text)
    fet3.append(feature3[r].text)

with open('path', 'w') as f:
    wr = csv.writer(f)
    wr.writerow(['Feature1', 'Feature2', 'Feature3'])
    wr.writerows([fet1, fet2, fet3])