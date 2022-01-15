import urllib.request as req
import json
import csv

url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with req.urlopen(url) as response :
    # data = response.read().decode("utf-8") #做中文的解碼
    data = json.load(response)
format_data = []
for i in data["result"]["results"]:
    format_data.append([i["stitle"],(i["address"][4:8]).replace(" ", ""),i["longitude"],i["latitude"],(i["file"]).lower().split("jpg")[0]+"jpg"])

with open('./data,csv', 'w', encoding='UTF8') as f:
    for data in format_data:
        writer = csv.writer(f)
        writer.writerow(data)

