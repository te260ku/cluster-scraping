import os
import pprint
import time
import urllib.error
import urllib.request

dst_dir = './tmp'
# <div class="MuiBox-root jss9 Hero__BlurImage-nj02o2-1 hqQcxu" imageurl="https://cluster-file-storage.imgix.net/uploads/group_511603d236751d853706fcf564/543da9b6-3845-46b2-8d1d-1e60e26f6f01/9090776b-f1f7-4004-87e3-1e902226d599.png?auto=format&amp;fit=crop&amp;h=1080&amp;w=1920"></div>
url = 'https://cluster-file-storage.imgix.net/uploads/group_511603d236751d853706fcf564/543da9b6-3845-46b2-8d1d-1e60e26f6f01/9090776b-f1f7-4004-87e3-1e902226d599.png'


# response.html.find("body .container .row .quote a", first=True).attrs['imageurl']


def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)

def download_file_to_dir(url, dst_dir):
    download_file(url, os.path.join(dst_dir, os.path.basename(url)))


if __name__ == "__main__":
    download_file_to_dir(url, dst_dir)