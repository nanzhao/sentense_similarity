#encoding=utf-8
import gensim
import os
from gensim.models.word2vec import LineSentence
from gensim.models.fasttext import FastText as FT_gensim

from fileObject import FileObj

file_obj = FileObj(r"testSet/data")
sentences = file_obj.read_lines_1_words()

"""
model_gensim = FT_gensim(size=100)
model_gensim.build_vocab(sentences)
model_gensim.train(sentences, total_examples=model_gensim.corpus_count, epochs=model_gensim.iter)
model_gensim.save('saved_model_gensim')
"""


loaded_model = FT_gensim.load('saved_model_gensim')
print(loaded_model)
print(loaded_model.most_similar('老人'))
print(loaded_model.doesnt_match("老人 小孩 孕妇 胃疼".split(" ")))

#sentence_obama = ["老人","高血压","怎么办"]
#sentence_president = ["青年","高血压","怎么办"]
#distance = loaded_model.wmdistance(sentence_obama, sentence_president)
#print(distance)

sentence_query = ["晚上","经常","失眠","怎么办"]

sim_max = 0
sim_index = 0
sim_list = []
for i in range (0,sentences.__len__()):
    distance = loaded_model.wmdistance(sentence_query, sentences[i])
    sim_list.append((distance,i))

sim_sort = sorted(sim_list, key=lambda sim : sim[0])

#    if distance> sim_max:
#        sim_max = distance
#        sim_index = i
#print ("sim_max is %d",sim_max)
#print (sentences[sim_index])

for i in range(0,5):
    print("sim_max is %d", sim_sort[i][0])
    print(sentences[sim_sort[i][1]])