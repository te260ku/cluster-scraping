from requests_html import HTMLSession
import time

url = "https://cluster.mu/w?page=2"

session = HTMLSession()
r = session.get(url)

r.html.render()

cards = r.html.find('.MuiCardActionArea-root')
links = []
base = "https://cluster.mu"

if len(cards) > 0:
    print(len(cards))
    for link in cards:
        tmp = base + link.attrs['href']
        links.append(tmp)

    for link in links:
        try:
            time.sleep(5)
            print(link)
            session_link = HTMLSession()
            r_ = session_link.get(link)
            r_.html.render()
            h2 = r_.html.find('h2')
            if len(h2) > 0:
                print(h2[0].text)
        except:
            pass
else:
    print("error")
