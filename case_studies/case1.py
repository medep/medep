## the code corresponding to c1.
import json
import requests
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn
import nltk
from gensim import corpora
nltk.download('wordnet')
nltk.download('stopwords')
en_stop = set(nltk.corpus.stopwords.words('english'))
from gensim.models.ldamodel import LdaModel

def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma
    
def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)

def prepare_text_for_lda(text):
    tokens = text.split(" ")
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma(token) for token in tokens]
    return tokens

## make a query to internal database

interesting_keywords = ["covid-19","vaccines","treatment"]
json_data_all = []
for keyword in interesting_keywords:
    example_query = "http://covid19explorer.ijs.si/gp/api?keyword={}".format(keyword)
    response = requests.get(example_query)
    json_data = json.loads(response.text)
    json_data_all+=json_data

## get scores and titles
top_docs = []
for hit in json_data_all:
    title, abstract = hit['article_title'], hit['article_abstract']
    top_docs.append(abstract)

## clean
clean_text = []
for el in top_docs:
    tokens = prepare_text_for_lda(el)
    clean_text.append(tokens)

dictionary = corpora.Dictionary(clean_text)
corpus = [dictionary.doc2bow(text) for text in clean_text]

NUM_TOPICS = 3
ldamodel = LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)

topics = ldamodel.print_topics(num_words=5)
for topic in topics:
    print(topic)
