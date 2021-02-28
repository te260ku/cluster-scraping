from requests_html import HTMLSession
import csv
import trimData

url = "https://cluster.mu/w/4ec2b9d7-f287-4347-8dfe-338fa2738b2f"

session = HTMLSession()
r = session.get(url)

r.html.render()

h2 = r.html.find('h2')
h6 = r.html.find('h6')
info_list = r.html.find('.MuiList-root')
p = info_list[0].find('p')

name_r = h2[0].text
like_r = h6[0].text
creator_r = h6[1].text
size_r = p[1].text
date_r = p[3].text

if len(info_list) > 0:
    row = trimData.trim_all_data(name_r, like_r, creator_r, size_r, date_r)
    print(row)

with open('data/sample.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(row)
    