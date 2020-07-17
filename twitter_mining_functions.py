import re
import csv
import nltk as nltk
from nltk.util import ngrams
#from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from contractions import CONTRACTION_MAP
from gensim.models.word2vec import Word2Vec
from gensim.models import Doc2Vec
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import itertools
import pickle
w2vpath = '/home/dmnte/mysite/10vector_50full_stemmer'
d2vpath = '/home/dmnte/mysite/100vector_25security_tweets_d2v_dbow_mincount=1_new_processor'
kmodel = '/home/dmnte/mysite/kmeans_model_mycomp_save.sav'
modelw1v = Word2Vec.load(w2vpath)
model = Doc2Vec.load(d2vpath)
kmeans_model = pickle.load(open(kmodel, 'rb'))

stopwords = ["youour","got","tho","im","u","ur",'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", "ain't","can't","can't've","'cause","could've","couldn't've","hadn't've","he'd","he'd've","he'll","he'll've","he's","how'd","how'd'y","how'll","how's","I'd","I'd've","I'll","I'll've","I'm","I've","i'd","i'd've","i'll","i'll've","i'm","i've","it'd","it'd've","it'll","it'll've","let's","ma'am","mayn't","might've","mightn't've","must've","mustn't've","needn't've","o'clock","oughtn't","oughtn't've","sha'n't","shan't've","she'd","she'd've","she'll","she'll've","shouldn't've","so've","so's","that'd","that'd've","that's","there'd","there'd've","there's","they'd","they'd've","they'll","they'll've","they're","they've","to've","we'd","we'd've","we'll","we'll've","we're","we've","what'll","what'll've","what're","what's","what've","when's","when've","where'd","where's","where've","who'll","who'll've","who's","who've","why's","why've","will've","won't've","would've","wouldn't've","y'all","y'all'd","y'all'd've","y'all're","y'all've","you'd've","you'll've"]
double_meaning_words = ['mitm','dos', 'worm', 'trojan', 'dns', 'hacker', 'xss', 'mirai', 'rat',  'spammer', 'exploit', 'cybersecur', 'petya', 'apt', 'scammer', 'exodus', 'backdoor', 'trojan', 'infosec', 'locki']
#gen_words = {'encrypted','scan','cve', 'spammer', 'RAT', 'zeroday', 'hit', 'hacker', 'data', 'stuxnet', 'phreaking', 'password', 'adware', 'cyberattacks', 'exploit', 'notpetya', 'antivrus', 'xss', 'virus', 'mirai', 'locky', 'scammers', 'flaw', 'cybersecurity', 'ransomware', 'keylogger', 'spamware', 'websites', 'brute', 'spam', 'phishing', 'detected', 'threat', 'dns', 'infosec', 'conficker', 'heartbleed', 'bug', 'hijack', 'samsam', 'wannacry', 'worm', 'dos', 'vulnerability', 'hijacking', 'APT', 'iot', 'hacking', 'injection', 'malware', 'protect', 'eternalblue', 'trojan', 'stole', 'uiwix', 'sensitive', 'patch', 'botnet', 'router', 'security', 'attack', 'cyber', 'spyware', 'network', 'petya', 'rootkit', 'mitm', 'email', 'spoof', 'bluekeep'}
original_filter = ['wolfrat', 'revil', 'samsam', 'ransomwar', 'heartbl', 'infosec', 'wannacri', 'dos', 'worm', 'phreak', 'trojan', 'dns', 'hacker', 'xss', 'notpetya', 'mirai', 'uiwix', 'rat', 'spywar', 'botnet', 'keylogg', 'confick', 'spamwar', 'stuxnet', 'exodus', 'locki', 'exploit', 'phish', 'malwar', 'spammer', 'rootkit', 'mitm', 'cybersecur', 'petya', 'ddos', 'apt', 'cybercrim', 'scammer', 'eternalblu', 'zero day']
snowballstemmer = SnowballStemmer("english")




def set_general_field(entobj):
############################################################################################################################################################################################################################################
#created_at : UTC time when this Tweet was created
#text : the actual UTF-8 text of the status update.
############################################################################################################################################################################################################################################
    general_field_dict = {}
    general_field_dict["tweet_created_at"] = (entobj["created_at"])
    general_field_dict["tweet_text"] = (entobj["text"])
    return general_field_dict

def expand_contractions(text, contraction_mapping=CONTRACTION_MAP):

    contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())),
                                      flags=re.IGNORECASE|re.DOTALL)
    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = contraction_mapping.get(match)\
                                if contraction_mapping.get(match)\
                                else contraction_mapping.get(match.lower())
        expanded_contraction = first_char+expanded_contraction[1:]
        return expanded_contraction

    expanded_text = contractions_pattern.sub(expand_match, text)
    expanded_text = re.sub("'", "", expanded_text)
    return expanded_text

def lang_retweet_check(tweetobj):
# check if tweet language field is english, it isnt truncated(cut off) and is not a retweet. if all these pass return object else return false
    try:
        language = (tweetobj["lang"])
    except:
        language = "None"
    try:
        is_truncated =  (tweetobj["truncated"])
    except:
        is_truncated = False

    try:
        text = (tweetobj["text"])
    except:
        text = False

    if "retweeted_status" not in tweetobj.keys() and is_truncated == False and language == "en" and text != False:
        return (tweetobj)
    else :
        return False

def filter_sec_data(tweetobj):
    texting = tweetobj["tweet_text"]
    preprocessed_text = processing_text(texting)
    return (preprocessed_text)

def processing_text(tweetobj):
##make a list of the main words in the tweet, minus punctuation, links, @ mentions, stop words, does have hashtags

    no_links = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''','', tweetobj)
    no_hashtags_ats = re.sub(r'\B@\w+', '', no_links)
    expand_contractions = [CONTRACTION_MAP[item.lower()] if item.lower() in CONTRACTION_MAP.keys() else item for item in str(no_hashtags_ats).split()]
    remove_extra_contractions = " ".join([item[:-2] if item[-2:] == "'s" or item[-2:] == "’s" else item for item in expand_contractions])
    alphanumeric_only = re.sub(r'[^a-zA-Z0-9 ]', '', remove_extra_contractions)
    minus_stopw_and_hashes = " ".join([item.lower() for item in str(alphanumeric_only).split() if item.isdigit() == False and item not in stopwords])
    minus_repeat_characters = ''.join(item[0] for item in itertools.groupby(minus_stopw_and_hashes))
    filtered_words = [snowballstemmer.stem(item.lower()) for item in str(minus_repeat_characters).split() if len(item) <= 10 and len(item) > 3]
    return (filtered_words)

def make_ngram_list(item):
    unigrams = set(item)
    token = nltk.word_tokenize(" ".join(item))
    bigrams = list(ngrams(token, 2))
    bigrams = [" ".join(x) for x in bigrams]
    bigrams = set(bigrams)
    unigrams_and_bigrams = list(unigrams) + list(bigrams)
    return (unigrams_and_bigrams)

def double_meaning_words_checking(keylist,status):
    ub_keylist = make_ngram_list(keylist)
    if set(ub_keylist).isdisjoint(original_filter) == False:
        dualmeanwordinboth = set(ub_keylist).intersection(double_meaning_words) # check it contains word from dual meaning words filter
        if bool(dualmeanwordinboth) == True:
            if len(list(dualmeanwordinboth)) > 1: #if it contains more than 1 we assume its related and let it through otherwise process it
                return (' '.join(keylist))
            else:
                most_similar_words_list1 = modelw1v.wv.most_similar(positive=[list(dualmeanwordinboth)[0].replace(" ","_")], topn=50)
                similar_words = [x[0].replace("_"," ") for x in most_similar_words_list1]
                tweet_minus_word = set(ub_keylist) - set(dualmeanwordinboth) #remove that term from the tweet also
                if bool(tweet_minus_word.intersection(similar_words)) == True: # check if the tweets other terms match our associated words list, if yes there fine, else remove them
                    return (' '.join(keylist))
                else:
                    return None
        else:
            return (' '.join(keylist))
    else:
        return None

def sentiment_scores(sentence):
#get compound sentiment score using vader
#-1 most negative and +1 most positive 0 neutral
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    return (sentiment_dict['compound'])


def save2csv(elist):
#save csv
    for entry in elist:
        try:
            with open("csv_file_MLKF+C.csv", 'a', encoding='utf-8', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter= ',')
                values = [value for key,value in entry.items()]
                writer.writerow(values)
        except BaseException as e:
            print("error: ",e)

def cluster_removal(keylist):
#predict cluster and remove
    if keylist != None:
        vector = model.infer_vector(keylist.split())
        cluster = kmeans_model.predict(vector.reshape(1,-1))

        if cluster[0] in [2,5,6]:
            print ("cluster_removed",keylist, cluster[0])
            return None
        else:
            return keylist
    else:
        return None