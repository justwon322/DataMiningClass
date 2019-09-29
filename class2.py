import nltk;
from nltk.corpus import brown
def generate_model(cfdist,word,num=15):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()

text = nltk.corpus.genesis.word('english-kjv.txt')
bigrams = nltk.bigrams(text)
#cfd
#generate_model(cfd,'living')


