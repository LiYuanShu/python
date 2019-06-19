
import re
import jieba
from gensim.models import word2vec
from nltk.classify import NaiveBayesClassifier
from sklearn import naive_bayes
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
def chinese_word_cut(mytext):
    return " ".join(jieba.cut(mytext))

#把停用词转换为一个列表存储
def get_custom_stopwords(stop_words_file):
    with open(stop_words_file) as f:
        stopwords = f.read()
    stopwords_list = stopwords.split('\n')
    custom_stopwords_list = [i for i in stopwords_list]
    return custom_stopwords_list
df = pd.read_csv('test.csv')
X = df[['text']]
y = df.type
X['cut_text'] = X.text.apply(chinese_word_cut)
print(X.cut_text[:5])
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.01, random_state=1)
stop_words_file = 'F:\python\数据分析结课实验\data/停用词.txt'
stopwords = get_custom_stopwords(stop_words_file)
vect = CountVectorizer()
print(type(X_train.cut_text))
term_matrix = pd.DataFrame(vect.fit_transform(X_train.cut_text[0:1000]).toarray(), columns=vect.get_feature_names())
for i in range(1000,len(X_train.cut_text),1000):
    if 1000+i<len(X_train.cut_text):
        term_matrix_temp = pd.DataFrame(vect.fit_transform(X_train.cut_text[i:1000+i]).toarray(), columns=vect.get_feature_names())
        term_matrix.append(term_matrix_temp)
print(type(X_train.cut_text))
# NB = naive_bayes.GaussianNB()
# NB.fit(X_train,X_test)
# print ("naive_bayes:",NB.predict(y_train))