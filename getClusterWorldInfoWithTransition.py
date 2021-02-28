from requests_html import HTMLSession

url = "https://cluster.mu/w?page=2"

session = HTMLSession()
r = session.get(url)

r.html.render()

cards = r.html.find('.MuiCardActionArea-root')
links = []

if len(cards) > 0:
    print(len(cards))
    for link in cards:
        tmp = link.attrs['href']
        links.append(tmp)
    print(len(links))
    print(links[0])