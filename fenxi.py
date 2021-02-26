import jieba
import re
from collections import Counter
import json

cut_words=""
for line in open('腾讯评论.json',encoding='utf-8'):
    line.strip('\n')
    line = re.sub("[A-Za-z0-9\：\·\—\，\。\“ \”]", "", line)
    seg_list=jieba.cut(line,cut_all=False)
    cut_words+=(" ".join(seg_list))
all_words=cut_words.split()
c = Counter()
#print(all_words)
for x in all_words:
    if len(x) > 1 and x != '\r\n':
        c[x] += 1

for (k, v) in c.most_common(50):
    datas = []
    data = {}
    data["name"] = k
    data["value"] = v
    datas.append(data)
    print(datas)
    with open('分词.json ', 'a', encoding=' utf-8 ') as f:
        f.write(json.dumps(datas, indent=2, ensure_ascii=False))
