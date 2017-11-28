# import modules & set up logging
import gensim, logging
from fileObject import FileObj
from gensim.models import Word2Vec


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


if __name__ == '__main__':

    file_obj = FileObj(r"testSet/data")
    sentences = file_obj.read_lines_1_words()
    #model = Word2Vec(sentences, sg=1, size=100, window=5, min_count=5, negative=3, sample=0.001, hs=1, workers=4)
    #model.save('w2v_model')
    model = Word2Vec.load('w2v_model')
    print(model.most_similar(['怀孕']))
    print(model.similarity('怀孕', '孕妇'))