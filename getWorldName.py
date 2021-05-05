from requests_html import HTMLSession

url = "https://cluster.mu/w?page=2"

session = HTMLSession()
r = session.get(url)

r.html.render()

cards = r.html.find('.MuiCardContent-root')

if len(cards) > 0:
    for card in cards:
        title = card.find('h6')
        print(title[0].text)