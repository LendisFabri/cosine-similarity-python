import re, json, string, math
# from sqlalchemy import create_engine, Table, Column, Integer, Text, MetaData
# from sqlalchemy.sql import select 
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# metadata.create_all(engine)
tokenize = lambda doc: doc.lower().split(" ")
stemmer = StemmerFactory().create_stemmer()
stopword = StopWordRemoverFactory().create_stop_word_remover()

def normalize_text(text):
	# url = re.sub(r"http\S+", "", text)
	stem = stemmer.stem(url)
	stop = stopword.remove(stem)
	punct = stop.translate(str.maketrans('','',string.punctuation+'0123456789'))
	return punct

query = ['batik bangkalan di madura cantik sekali']
tweets = [x[2] for x in result] #dataset dokumen
corpus = query+tweets
tfidf_vectorizer = TfidfVectorizer(norm='l2',min_df=0, use_idf=True, smooth_idf=True, sublinear_tf=True, preprocessor=normalize_text, tokenizer=tokenize)
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
similarity = np.array(cosine_similarity(tfidf_matrix[0], tfidf_matrix)[0])
srt_idx = np.argsort(-similarity)
print(similarity.shape)
for n, idx in enumerate(srt_idx):
	print(n,'. (',idx,') ',similarity[idx],': ',corpus[idx])

result.close()