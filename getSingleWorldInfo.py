from requests_html import HTMLSession
import time
import csv
import trimData

url = "https://cluster.mu/w/79e26b4f-d494-40b3-981f-ce4ca1e2a6ac"

def main():
    session = HTMLSession()
    r = session.get(url)

    r.html.render()


    h2 = r.html.find('h2')
    h6 = r.html.find('h6')
    info_list = r.html.find('.MuiList-root')
    play_list = r.html.find('.WorldStats__Container-sc-17lod9z-0')
    p_play = play_list[0].find('p')
    p_info = info_list[0].find('p')

    name_r = h2[0].text
    like_r = p_play[0].text
    play_r = p_play[1].text
    creator_r = h6[0].text
    size_r = p_info[1].text
    date_r = p_info[3].text

    if len(info_list) > 0:
        row = [name_r, like_r, play_r, creator_r, size_r, date_r]
        print(row)

if __name__ == "__main__":
    try:
        main()
    except:
        pass
    