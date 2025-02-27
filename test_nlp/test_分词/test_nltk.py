import jieba
import jieba.posseg as pseg


text = "我正在研究人工智能和深度学习。"
words = jieba.cut(text, cut_all=False)
print(list(words))

# 词性标注
seg_words = pseg.cut(text)
for word,flag in seg_words:
    print(word)
    print(flag)

jieba.add_word("人工智能")
jieba.add_word("深度学习")
print(list(jieba.cut(text)))

