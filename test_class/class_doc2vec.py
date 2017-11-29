import jieba
import multiprocessing
from gensim.models.doc2vec import TaggedDocument
from gensim.models import Doc2Vec

class Model(object):
    def __init__(self,file):
        self.corpus = self.getCorp(self.readData(file))
        self.model = Doc2Vec(size=200, min_count=1, iter=10)
        self.predictor = self.train(self.corpus)

    def readData(self,file):
        corpora_documents = []
        with open(file, 'rb') as f:
            for line in f.readlines():
                items = line.decode('utf-8').strip().split('\t')
                if items.__len__() < 2:
                    continue
                corpora_documents.append(items[1])
        return corpora_documents

    def getCorp(self,raw_documents):
        cores = multiprocessing.cpu_count()
        print(cores)
        corpora_documents = []
        for i, item_text in enumerate(raw_documents):
            words_list = list(jieba.cut(item_text))
            document = TaggedDocument(words=words_list, tags=[i])
            corpora_documents.append(document)
        return corpora_documents

    def train(self,corpora_documents):
        self.model.build_vocab(corpora_documents)
        self.model.train(corpora_documents,total_examples=self.model.corpus_count, epochs=self.model.iter)
        return self.model


    def predict(self,test_data_1):
        print('#########', self.predictor.vector_size)
        test_cut_raw_1 = list(jieba.cut(test_data_1))
        print(test_cut_raw_1)
        inferred_vector = self.predictor.infer_vector(test_cut_raw_1)
        print(inferred_vector)
        sims = self.predictor.docvecs.most_similar([inferred_vector], topn=3)
        print(sims)

        for sim in sims:
            print (self.corpus[sim[0]])