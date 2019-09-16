import nltk
import spacy

nlp = spacy.load('pt_core_news_sm')

#Retorna a similaridade das frases
def get_similarity(tup):
    index1 = tup[0][0]
    index2 = tup[1][0]
    similarity = tup[0][1].similarity(tup[1][1])
    return index1, index2, similarity

