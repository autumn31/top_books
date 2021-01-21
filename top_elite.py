import requests
import csv

url = "https://athena.eslite.com/api/v1/best_sellers/bookstore?tab="

tab = input('輸入分頁名稱(如中文、外文)：')
res = requests.get(url+tab).json()

with open('elite_output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['分類', '書名'])

    for k in res:
        for book in res[k]:
            writer.writerow([k, book['name']])
