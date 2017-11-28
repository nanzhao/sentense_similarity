#encoding=utf-8


import gc
import os
from gensim import corpora, models, similarities
from sentence import Sentence
from collections import defaultdict
from gensim.models.fasttext import FastText as FT_gensim

class SentenceSimilarity():

    def __init__(self,seg):
        self.seg = seg

    def set_sentences(self,sentences):
        self.sentences = []

        for i in range(0,len(sentences)):
            self.sentences.append(Sentence(sentences[i],self.seg,i))

    # 获取切过词的句子
    def get_cuted_sentences(self):
        cuted_sentences = []

        for sentence in self.sentences:
            cuted_sentences.append(sentence.get_cuted_sentence())

        return cuted_sentences

    # 构建其他复杂模型前需要的简单模型
    def simple_model(self,min_frequency = 1):
        self.texts = self.get_cuted_sentences()

        # 删除低频词
        frequency = defaultdict(int)
        for text in self.texts:
            for token in text:
                frequency[token] += 1

        self.texts = [[token for token in text if frequency[token] > min_frequency] for text in self.texts]

        self.dictionary = corpora.Dictionary(self.texts)
        self.corpus_simple = [self.dictionary.doc2bow(text) for text in self.texts]

    # tfidf模型
    def TfidfModel(self):
        self.simple_model()

        # 转换模型
        self.model = models.TfidfModel(self.corpus_simple)
        self.corpus = self.model[self.corpus_simple]

        # 创建相似度矩阵
        self.index = similarities.MatrixSimilarity(self.corpus)

    # lsi模型
    def LsiModel(self):
        self.simple_model()

        # 转换模型
        self.model = models.LsiModel(self.corpus_simple)
        self.corpus = self.model[self.corpus_simple]

        # 创建相似度矩阵
        self.index = similarities.MatrixSimilarity(self.corpus)

    #lda模型
    def LdaModel(self):
        self.simple_model()

        # 转换模型
        self.model = models.LdaModel(self.corpus_simple)
        self.corpus = self.model[self.corpus_simple]

        # 创建相似度矩阵
        self.index = similarities.MatrixSimilarity(self.corpus)

    # FastText模型
    def FasttxModel(self):
        self.simple_model()
        # 转换模型
        if os.path.exists('saved_model_gensim'):
            self.model =  FT_gensim.load('saved_model_gensim')
        else:
            self.model = FT_gensim(size=100)
            self.model.build_vocab(self.sentences)
            self.model.train(self.sentences, total_examples= self.model.corpus_count, epochs= self.model.iter)
            self.model.save('saved_model_gensim')


    def sentence2vec(self,sentence):
        sentence = Sentence(sentence,self.seg)
        vec_bow = self.dictionary.doc2bow(sentence.get_cuted_sentence())
        return self.model[vec_bow]

    # 求最相似的句子
    def similarity(self,sentence):
        sentence_vec = self.sentence2vec(sentence)

        sims = self.index[sentence_vec]
        sim = sorted(enumerate(sims), key=lambda item: -item[1])

        for i in range (0,5):
            index = sim[i][0]
            score = sim[i][1]
            sentence = self.sentences[index]
            print(sentence.get_origin_sentence()+' '+str(score))

    def similarity2(self,sentence):
        sentence = Sentence(sentence, self.seg)
        sentence_query = sentence.get_cuted_sentence()

        sim_list = []
        for i in range(0, self.sentences.__len__()):
            distance = self.model.wmdistance(sentence_query, self.sentences[i].get_cuted_sentence())
            sim_list.append((distance, i))

        sim_sort = sorted(sim_list, key=lambda sim: sim[0])

        for i in range(0, 5):
            print("sim_max is %d", sim_sort[i][0])
            print(self.sentences[sim_sort[i][1]].get_cuted_sentence())



