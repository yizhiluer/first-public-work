import jieba
from pyecharts.charts import WordCloud

comments = open("comments.json", "r", encoding='utf-8').read()

# 使用精确模式对文本进行分词
words = jieba.lcut(comments)

# 通过键值对的形式存储词语及其出现的次数
counts = {}

for word in words:
    # 单个词语不计算在内
    if len(word) == 1:
        continue
    else:
        # 遍历所有词语，每出现一次其对应的值加 1
        counts[word] = counts.get(word, 0) + 1

        # 将键值对转换成列表
items = list(counts.items())

# 根据词语出现的次数进行从大到小排序
items.sort(key=lambda x: x[1], reverse=True)

word_cloud = WordCloud()
word_cloud.add("评论数：", items, word_size_range=[12, 55])
word_cloud.render('result.html')
