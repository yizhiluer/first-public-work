import urllib.request
import re
import time
import random
import json

userpools = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
]
user = random.choice(userpools)
headers = ("User-Agent", user)
open = urllib.request.build_opener()
open.addheaders = [headers]
urllib.request.install_opener(open)

first_id = 1613573389059
comment_id = "0"
commentslist = []
for i in range(1, 1000):
    url = "https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + str(
        comment_id) + "&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=" + str(first_id)
    content_path = '"content":"(.*?)",'
    last_path = '"last":"(.*?)",'
    content_data = urllib.request.urlopen(url).read().decode("utf-8")
    content = re.compile(content_path).findall(content_data)
    last_id = re.compile(last_path).findall(content_data)
    for j in last_id:
        comment_id = j
        first_id += 1

    for j in range(1, len(content)):
        dict_word = {}
        dict_word["评论"] = content[j]
        commentlist.append(dict_word)
print(comments_list)

with open('comments.json', 'a', encoding='utf-8') as fi:
    fi.write(json.dumps(comments_list, ensure_ascii=False))