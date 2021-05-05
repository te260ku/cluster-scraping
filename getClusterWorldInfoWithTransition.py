from requests_html import HTMLSession
from requests_html import AsyncHTMLSession
import time
import csv
import sys

url_base = "https://cluster.mu/w?page="
base = "https://cluster.mu"

args = sys.argv

# ページ番号
page_nums = ()
if not args[1] and not args[2]:
    page_nums = (10, 10)
else:
    page_nums = (int(args[1]), int(args[2]))

# 記録するファイル名
file_name = args[3]

# def wait_render(u):
#     assesion = AsyncHTMLSession()

#     async def process():
#         r = await assesion.get(u)
#         await r.html.arender(wait=5, sleep=5)
#         return r

#     r = assesion.run(process)[0]
#     cards = r.html.find('.MuiCardActionArea-root')

#     if len(cards) > 0:
#         print(len(cards))
#     else:
#         print("error")


for i in range(page_nums[0], page_nums[1]+1):
    try:
        url = url_base + str(i)
        links = []
        count = 0

        # wait_render(url)

        session = HTMLSession()
        r = session.get(url)
        r.html.render(wait=5, sleep=5)

        cards = r.html.find('.MuiCardActionArea-root')

        if len(cards) > 0:
            print(url)
            for link in cards:
                tmp = base + link.attrs['href']
                links.append(tmp)
            

            with open('data/' + file_name + '.csv', 'a', newline="") as f:
                time.sleep(5)
                writer = csv.writer(f)
                for link in links:
                    try:
                        
                        session_link = HTMLSession()
                        r_ = session_link.get(link)
                        r_.html.render(wait=5, sleep=5)


                        h2 = r_.html.find('h2')
                        h6 = r_.html.find('h6')
                        info_list = r_.html.find('.MuiList-root')
                        play_list = r_.html.find('.WorldStats__Container-sc-17lod9z-0')
                        p_play = play_list[0].find('p')
                        p_info = info_list[0].find('p')

                        name_r = h2[0].text
                        play_r = p_play[0].text
                        like_r = p_play[1].text
                        creator_r = h6[0].text
                        size_r = p_info[1].text
                        date_r = p_info[3].text

                        row = [name_r, play_r, like_r, creator_r, size_r, date_r]

                        count += 1
                        print(count)
                        
                        
                        writer.writerow(row)
                        time.sleep(5)

                    except:
                        pass
        else:
            print("error")
    except:
        pass
