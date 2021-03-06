from gensim import corpora
from gensim.similarities import Similarity
import jieba

def readData(file):
    corpora_documents = []
    with open(file, 'rb') as f:
        for line in f.readlines():
            items = line.decode('utf-8').strip().split('\t')
            if items.__len__() < 2:
                continue
            corpora_documents.append(items[1])
    return corpora_documents

raw_documents = readData('data2')
print(raw_documents)

"""
raw_documents = [
    '0无偿居间介绍买卖毒品的行为应如何定性',
    '1吸毒男动态持有大量毒品的行为该如何认定',
    '2如何区分是非法种植毒品原植物罪还是非法制造毒品罪',
    '3为毒贩贩卖毒品提供帮助构成贩卖毒品罪',
    '4将自己吸食的毒品原价转让给朋友吸食的行为该如何认定',
    '5为获报酬帮人购买毒品的行为该如何认定',
    '6毒贩出狱后再次够买毒品途中被抓的行为认定',
    '7虚夸毒品功效劝人吸食毒品的行为该如何认定',
    '8妻子下落不明丈夫又与他人登记结婚是否为无效婚姻',
    '9一方未签字办理的结婚登记是否有效',
    '10夫妻双方1990年按农村习俗举办婚礼没有结婚证 一方可否起诉离婚',
    '11结婚前对方父母出资购买的住房写我们二人的名字有效吗',
    '12身份证被别人冒用无法登记结婚怎么办？',
    '13同居后又与他人登记结婚是否构成重婚罪',
    '14未办登记只举办结婚仪式可起诉离婚吗',
    '15同居多年未办理结婚登记，是否可以向法院起诉要求离婚'
]
"""


corpora_documents = []
for item_text in raw_documents:
    item_str = list(jieba.cut(item_text))
    corpora_documents.append(item_str)


# 生成字典和向量语料
dictionary = corpora.Dictionary(corpora_documents)
corpus = [dictionary.doc2bow(text) for text in corpora_documents]

similarity = Similarity('-Similarity-index', corpus, num_features=400)


test_data_1 = '流鼻涕要吃药吗'
#test_cut_raw_1 = util_words_cut.get_class_words_list(test_data_1)
test_cut_raw_1 = list(jieba.cut(test_data_1))
test_corpus_1 = dictionary.doc2bow(test_cut_raw_1)
similarity.num_best = 5
print(similarity[test_corpus_1])