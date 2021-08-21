from requests_html import HTMLSession
import time

url = "https://cluster.mu/w/93518ff8-e020-4224-bd28-5b91d6b49a2c"

def main():
    session_link = HTMLSession()
    r_ = session_link.get(url)
    r_.html.render(wait=5, sleep=5)


    h2 = r_.html.find('h2')
    h6 = r_.html.find('h6')
    info_list = r_.html.find('.MuiList-root')
    play_list = r_.html.find('.WorldStats__Container-sc-17lod9z-0')
    p_play = play_list[0].find('p')
    p_info = info_list[0].find('p')
    description_list = r_.html.find('.Description__Container-sc-168rmxs-0')
    description_info = description_list[0].find('p')

    name_r = h2[0].text
    play_r = p_play[0].text
    like_r = p_play[1].text
    creator_r = h6[0].text
    size_r = p_info[1].text
    date_r = p_info[3].text
    description_r = description_info[0].text

    row = [name_r, like_r, play_r, creator_r, size_r, date_r, description_r]
    print(row)

if __name__ == "__main__":
    try:
        main()
    except:
        pass
    