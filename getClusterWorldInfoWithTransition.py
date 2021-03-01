from requests_html import HTMLSession
import time
import csv

url_base = "https://cluster.mu/w?page="
base = "https://cluster.mu"
start_page_num = 2
end_page_num = 5

for i in range(start_page_num, end_page_num):
    url = url_base + str(i)
    links = []
    count = 0

    session = HTMLSession()
    r = session.get(url)
    time.sleep(1)
    r.html.render()
    time.sleep(1)

    cards = r.html.find('.MuiCardActionArea-root')
    
    del session
    del r

    if len(cards) > 0:
        
        for link in cards:
            tmp = base + link.attrs['href']
            links.append(tmp)
        
        print(len(links))

        with open('data/sample.csv', 'a') as f:
            writer = csv.writer(f)
            
            for link in links:
                try:
                    
                    session_link = HTMLSession()
                    r_ = session_link.get(link)
                    r_.html.render()

                    h2 = r_.html.find('h2')
                    h6 = r_.html.find('h6')
                    info_list = r_.html.find('.MuiList-root')
                    p = info_list[0].find('p')

                    del session_link
                    del r_

                    name_r = h2[0].text
                    if len(h6) == 2:
                        like_r = h6[0].text
                        creator_r = h6[1].text
                    else:
                        like_r = "0 いいね"
                        creator_r = h6[0].text
                    size_r = p[1].text
                    date_r = p[3].text

                    row = [name_r, like_r, creator_r, size_r, date_r]

                    count += 1
                    print(count)

                    writer.writerow(row)
                    print(row)

                    time.sleep(2)
                        
                except:
                    pass
    else:
        print("error")
