from sklearn.neighbors import LSHForest
from sklearn.feature_extraction.text import  TfidfVectorizer
import jieba

class Model(object):
    def __init__(self, file):
        self.corpus = self.getCorp(self.readData(file))
        self.tfidf = TfidfVectorizer(min_df=3, max_features=None, ngram_range=(1, 2),
                                     use_idf=1, smooth_idf=1,sublinear_tf=1)
        self.lshf = LSHForest(random_state=42)
        self.train(self.corpus)

    def readData(self,file):
        corpora_documents = []
        with open(file, 'rb') as f:
            for line in f.readlines():
                items = line.decode('utf-8').strip().split('\t')
                if items.__len__() < 2:
                    continue
                corpora_documents.append(items[1])
        return corpora_documents

    def getCorp(self, raw_documents):
        train_documents = []
        for item_text in raw_documents:
            item_str = " ".join(list(jieba.cut(item_text)))
            train_documents.append(item_str)
        return train_documents

    def train(self,train_documents):
        x_train = self.tfidf.fit_transform(train_documents)
        self.lshf.fit(x_train.toarray())

    def predict(self,test_data_1):
        test_cut_raw_1 = " ".join(list(jieba.cut(test_data_1)))
        x_test = self.tfidf.transform([test_cut_raw_1])
        distances, indices = self.lshf.kneighbors(x_test.toarray(), n_neighbors=3)
        print(distances)
        print(indices)
        for inx in indices[0]:
            print(self.corpus[inx])