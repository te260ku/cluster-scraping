# coding: UTF-8
# reference -> https://qiita.com/Azunyan1111/items/9b3d16428d2bcc7c9406
import requests
from bs4 import BeautifulSoup

url = "http://www.nikkei.com/markets/kabu/"

html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

span = soup.findAll("span")

nikkei_heikin = ""

for tag in span:
    try:
        string_ = tag.get("class").pop(0)

        if string_ in "mkc-stock_prices":
                nikkei_heikin = tag.string
                break
    except:
        pass

print(nikkei_heikin)