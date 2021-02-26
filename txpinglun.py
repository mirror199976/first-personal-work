import re
import requests
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36'}

data = []
datas = []
page = '1614254272912'
cursor = '0'

for i in range(0, 1000):
   url = 'https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=' + cursor + '&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=' + str(page)
   source = requests.get(url, headers=headers).content.decode()
   x ='"content":"(.*?)"'
   data = re.compile(x, re.S).findall(source)
   datas.append(data)
   id='"last":"(.*?)"'
   cursor = re.compile(id, re.S).findall(source)[0]
   page = str(int(page) + 1)

with open('腾讯评论.json', 'a', encoding='utf-8') as f:
    f.write(json.dumps(datas, indent=2, ensure_ascii=False))
    print(datas)