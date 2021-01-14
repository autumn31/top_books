import requests
from bs4 import BeautifulSoup
import sys
import csv

# if len(sys.argv) < 2:
#     print("need url")
#     exit()
# url = sys.argv[1]

url = input('輸入博客來書頁連結：')
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
items = soup.findAll("li", {"class": "item"})

print("found %s books" % len(items))

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['排名', '書名'])

    for item in items:
        name = item.select_one("img")["alt"]
        no = item.select_one("strong", {"class": "no"}).text
        writer.writerow([no, name])
