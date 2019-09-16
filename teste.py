import unicodedata
import itertools
import re

import nltk
import spacy
from spacy.language import Language
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from multiprocessing import Pool


pt_nlp = spacy.load('pt_core_news_sm')
nltk.download('stopwords')
import pandas as pd
df_data = pd.read_csv('/Users/LauraDamacenodeAlmei/Desktop/clientes.example_shaped.csv')
df_data.head()

def vectorize(exemplos):
    nlp = spacy.load('pt_core_news_sm')
    docs = nlp.pipe(list(exemplos), n_threads=5)

    # docs_permuted = itertools.combinations(docs, 2)
    return docs

# Geração do modelo
frases = df_data['clean_content']
docs = vectorize(frases)

docs_with_index = list(zip(df_data.index, docs))
docs_permuted = itertools.combinations(docs_with_index, 2)

result = pd.DataFrame(columns=['classe_a', 'frase_a', 'classe_b', 'frase_b', 'semelhança'])

#Retorna a similaridade das frases
def get_similarity(tup):
    index1 = tup[0][0]
    index2 = tup[1][0]
    similarity = tup[0][1].similarity(tup[1][1])
    return index1, index2, similarity



tups = [doc for _, doc in enumerate(docs_permuted)]

result_df = []
import datetime

# Carregamento das threads
if __name__ == "__main__":
    start = datetime.datetime.now()
    p = Pool(7)
    result = p.map(get_similarity, tups)
#recebe o index da primeira tuple e o indice da segunda e faz a busca no dataframe.
    for i, j, similarity in result:
        if similarity >= 0.94:
            result_df.append(
                {
                    'classe_a': df_data.at[i,'class'],
                    'frase_a': df_data.at[i,'content'],
                    'classe_b': df_data.at[j,'class'],
                    'frase_b': df_data.at[j,'content'],
                    'semelhanca': similarity,
                }
            )
    result_df = pd.DataFrame(result_df)
    #print(result_df.head())
    end = datetime.datetime.now()
    print(end-start)

# Para fazer rodar no windows, colocar o trecho do código que está sendo paralelizado (exemplo windows.py):

# Carregamento das threads com windows
#import windows
# if __name__ == "__main__":
#     start = datetime.datetime.now()
#     p = Pool(7)
#     result = p.map(windows.get_similarity, tups)
# #recebe o index da primeira tuple e o indice da segunda e faz a busca no dataframe.
#     for i, j, similarity in result:
#         if similarity >= 0.94:
#             result_df.append(
#                 {
#                     'classe_a': df_data.at[i,'class'],
#                     'frase_a': df_data.at[i,'content'],
#                     'classe_b': df_data.at[j,'class'],
#                     'frase_b': df_data.at[j,'content'],
#                     'semelhanca': similarity,
#                 }
#             )
#     result_df = pd.DataFrame(result_df)
#     #print(result_df.head())
#     end = datetime.datetime.now()
#     print(end-start)


