import pandas as pd
from collections import Counter
from nltk.stem import WordNetLemmatizer
from contractions import CONTRACTION_MAP
import nltk
#from sqlalchemy import create_engine
import creds
import mysql.connector
import sshtunnel

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0
stop = ["look","daily","changing","thanks","meet","latest","new","youour","got","tho","im","u","ur",'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", "ain't","can't","can't've","'cause","could've","couldn't've","hadn't've","he'd","he'd've","he'll","he'll've","he's","how'd","how'd'y","how'll","how's","I'd","I'd've","I'll","I'll've","I'm","I've","i'd","i'd've","i'll","i'll've","i'm","i've","it'd","it'd've","it'll","it'll've","let's","ma'am","mayn't","might've","mightn't've","must've","mustn't've","needn't've","o'clock","oughtn't","oughtn't've","sha'n't","shan't've","she'd","she'd've","she'll","she'll've","shouldn't've","so've","so's","that'd","that'd've","that's","there'd","there'd've","there's","they'd","they'd've","they'll","they'll've","they're","they've","to've","we'd","we'd've","we'll","we'll've","we're","we've","what'll","what'll've","what're","what's","what've","when's","when've","where'd","where's","where've","who'll","who'll've","who's","who've","why's","why've","will've","won't've","would've","wouldn't've","y'all","y'all'd","y'all'd've","y'all're","y'all've","you'd've","you'll've"]
lemmatizer = WordNetLemmatizer()

connection = mysql.connector.connect(user='newuser', password='password',host='127.0.0.1', port=3306,database='dmnte$security_tweet_data',)    	
static_df = pd.read_sql('SELECT * FROM security_tweet_data', con=connection)
connection.close()
static_df["sql_tweet_text"] = static_df["sql_tweet_text"].replace('[^a-zA-Z0-9 ]', '', regex=True)
static_df["sql_tweet_text"] = static_df['sql_tweet_text'].apply(lambda x: [item.lower() for item in str(x).split() if item.isalpha() == True and item not in stop])
static_df["sql_tweet_text"] = static_df["sql_tweet_text"].str.join(" ")



#def get_dataframe():

#	#with sshtunnel.SSHTunnelForwarder(('ssh.pythonanywhere.com'),ssh_username='dmnte', ssh_password='1{B)j#_A<0w/',remote_bind_address=('dmnte.mysql.pythonanywhere-services.com', 3306)) as tunnel:
#	connection = mysql.connector.connect(user='newuser', password='password',host='127.0.0.1', port=3306,database='dmnte$security_tweet_data',)    	
			
#	df = pd.read_sql('SELECT * FROM security_tweet_data', con=connection)

#	connection.close()
	
#	return (df)


def make_ngram_list(item):
    unigrams = set(item)
    token = nltk.word_tokenize(" ".join(item))
    bigrams = list(ngrams(token, 2))
    bigrams = [" ".join(x) for x in bigrams]
    bigrams = set(bigrams)
    unigrams_and_bigrams = list(unigrams) + list(bigrams)
    return (unigrams_and_bigrams)

#def get_cleaned_text_data():

	#with sshtunnel.SSHTunnelForwarder(('ssh.pythonanywhere.com'),ssh_username='dmnte', ssh_password='1{B)j#_A<0w/',remote_bind_address=('dmnte.mysql.pythonanywhere-services.com', 3306)) as tunnel:
	#connection = mysql.connector.connect(user='newuser', password='password',host='127.0.0.1', port=3306,database='dmnte$security_tweet_data',)    	
			
	#df = pd.read_sql('SELECT * FROM security_tweet_data', con=connection)
	#df = static_df
	##########################preprocessing#######################################################################################################
	#df['sql_tweet_text'] = df['sql_tweet_text'].replace(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''','',regex=True)
	#df['sql_tweet_text'] = df['sql_tweet_text'].replace(r'\B@\w+', '', regex=True)
	#df["sql_tweet_text"] = df['sql_tweet_text'].apply(lambda x: [CONTRACTION_MAP[item.lower()] if item.lower() in CONTRACTION_MAP.keys() else item for item in str(x).split()])
	#df["sql_tweet_text"] = df["sql_tweet_text"].replace('[^a-zA-Z0-9 ]', '', regex=True)

	#df["sql_tweet_text"] = df['sql_tweet_text'].apply(lambda x: [item.lower() for item in str(x).split() if any(item.isdigit()) == False and item not in stop])
	#df["sql_tweet_text"] = df['sql_tweet_text'].apply(lambda x: [item[:-2] if item[-2:] == "'s" or item[-2:] == "’s" else item for item in x])
	#df["sql_tweet_text"] = df["sql_tweet_text"].str.join(" ")
	#df["sql_tweet_text"] = df["sql_tweet_text"].str.join(" ")
	#df["sql_tweet_text"] = df['sql_tweet_text'].apply(lambda x: " ".join([lemmatizer.lemmatize(item.lower()) for item in str(x).split() if len(item) <= 10 and len(item) > 2 and item not in stop]))
	##############################################################################################################################################
	

	#connection.close()
#	return (df)


def get_word_list(df):
	return (' '.join([(item) for item in df['sql_tweet_text']]).split())


def get_bigram_rank(list_comment):
	bigramFinder = nltk.collocations.BigramCollocationFinder.from_words(list_comment)
	bigramFinder.apply_freq_filter(2)
	bigram_freq = bigramFinder.ngram_fd.items()
	bigram_rank_list = [(" ".join(k), v) for k,v in bigram_freq]
	return (bigram_rank_list)


def get_trigram_rank(list_comment):
	trigramFinder = nltk.collocations.TrigramCollocationFinder.from_words(list_comment)
	trigramFinder.apply_freq_filter(2)
	trigram_freq = trigramFinder.ngram_fd.items()
	trigram_rank_list = [(" ".join(k), v) for k,v in trigram_freq]
	return (trigram_rank_list)


def get_mostfrequent_data_all(ngram):
	df = get_cleaned_text_data()
	word_list = get_word_list(df)
	top_cs_words = Counter(word_list).most_common(100)

	if ngram == "unigram":
		full_list = (top_cs_words)
	elif ngram == "bigram":
		full_list = (get_bigram_rank(word_list))
	elif ngram == "trigram":
		full_list = (get_trigram_rank(word_list))
	else:
		full_list = (top_cs_words+get_bigram_rank(word_list)+get_trigram_rank(word_list))

	sorted_uni_bi_tri_gram_list = sorted(full_list, key=lambda tup: tup[1],reverse=True)
	x_values = [mf_word[0] for mf_word in sorted_uni_bi_tri_gram_list]
	y_values = [mf_val[1] for mf_val in sorted_uni_bi_tri_gram_list]
	return (x_values,y_values)

def get_mostfrequent_data_all_daterange(ngram,start_date,end_date):
	df = static_df

	df_dated = df[(df['sql_datetime_object'] >= start_date) & (df['sql_datetime_object'] <= end_date)]
	word_list = get_word_list(df_dated)

	if ngram == "unigram":
		top_cs_words = Counter(word_list).most_common(31)
		full_list = (top_cs_words)
	elif ngram == "bigram":
		full_list = (get_bigram_rank(word_list))
	elif ngram == "trigram":
		full_list = (get_trigram_rank(word_list))
	else:
		top_cs_words = Counter(word_list).most_common(31)
		full_list = (top_cs_words+get_bigram_rank(word_list)+get_trigram_rank(word_list))

	sorted_uni_bi_tri_gram_list = sorted(full_list, key=lambda tup: tup[1],reverse=True)
	x_values = [mf_word[0] for mf_word in sorted_uni_bi_tri_gram_list]
	y_values = [mf_val[1] for mf_val in sorted_uni_bi_tri_gram_list]
	return (x_values,y_values)

def get_cleaned_text_data_original(word):
	df_tweet_graph = pd.DataFrame()
	#df_tweet_graph = static_df
	###########################preprocessing#######################################################################################################
	#df['ptext'] = df['sql_tweet_text'].replace(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''','',regex=True)
	#df['ptext'] = df['sql_tweet_text'].replace(r'\B@\w+', '', regex=True)
	#df["ptext"] = df['sql_tweet_text'].apply(lambda x: [CONTRACTION_MAP[item.lower()] if item.lower() in CONTRACTION_MAP.keys() else item for item in str(x).split()])
	#df["ptext"] = df['sql_tweet_text'].apply(lambda x: [item[:-2] if item[-2:] == "'s" or item[-2:] == "’s" else item for item in x])
	#df["ptext"] = df["sql_tweet_text"].str.join(" ")
	#df["ptext"] = df["sql_tweet_text"].replace('[^a-zA-Z0-9 ]', '', regex=True)
	#df["ptext"] = df['sql_tweet_text'].apply(lambda x: [item.lower() for item in str(x).split() if item.isdigit() == False and item not in stop])
	#df["ptext"] = df["sql_tweet_text"].str.join(" ")
	#df["ptext"] = df['sql_tweet_text'].apply(lambda x: " ".join([lemmatizer.lemmatize(item.lower()) for item in str(x).split() if len(item) <= 10 and len(item) > 2 and item not in stop]))
	##############################################################################################################################################
	#connection.close()
	
	df_tweet_graph = static_df[static_df['sql_tweet_text'].str.contains(word)]

	return (df_tweet_graph)

def get_novice_view_data():

	df_n = pd.DataFrame()
	
	df_n['sql_tweet_text'] = static_df['sql_tweet_text'].str.lower() #change column to lower case to normalize words
	df_n["spyware"] = df_n['sql_tweet_text'].str.count("spyware")    #get count of various strings from dataset
	df_n["malware"] = df_n['sql_tweet_text'].str.count("malware")
	df_n["trojan"] = df_n['sql_tweet_text'].str.count("trojan")
	df_n["ransomware"] = df_n['sql_tweet_text'].str.count("ransomware")
	df_n["phishing"] = df_n['sql_tweet_text'].str.count("phishing")
	df_n["scam"] = df_n['sql_tweet_text'].str.count("scam")
	df_n["password"] = df_n['sql_tweet_text'].str.count("password")
	df_n["botnet"] = df_n['sql_tweet_text'].str.count("botnet")

	df_n['sql_datetime_object'] = static_df['sql_datetime_object'].astype('datetime64[ns]').dt.normalize()  #normalize datetime so can use groupby
	df1 = df_n.groupby('sql_datetime_object')[['spyware', 'malware', 'trojan', 'ransomware', 'phishing', 'scam','password', 'botnet']].agg(sum) #sum string tallies

	return (df1)
