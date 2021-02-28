from requests_html import HTMLSession
import csv

url = "https://cluster.mu/w/4ec2b9d7-f287-4347-8dfe-338fa2738b2f"

session = HTMLSession()
r = session.get(url)

r.html.render()

h2 = r.html.find('h2')
h6 = r.html.find('h6')
info_list = r.html.find('.MuiList-root')
p = info_list[0].find('p')

name = h2[0].text
like = h6[0].text
creator = h6[1].text
size = p[1].text
date = p[3].text

if len(info_list) > 0:
    print(name)
    print(like)
    print(creator)
    print(size)
    print(date)
    row = [name, like, creator, size, date]
with open('data/sample.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(row)
    