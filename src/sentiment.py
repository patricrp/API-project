from pymongo import MongoClient
from errorHandler import jsonErrorHandler
from conversations import getListChat
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

client = MongoClient("mongodb://localhost/Conversations")
db = client.get_database()

def sentimentText(chatname):
    #Text group sentiment
    text = getListChat(chatname)
    sia = SentimentIntensityAnalyzer()
    #Needs to be a string of phrases
    return sia.polarity_scores(text)

def sentimentCharacter(username):
    #Character sentiment
    sia = SentimentIntensityAnalyzer()
    conversation = list(db['Conversations'].find({}))[0]['Message']
    characConv = []
    for dic in conversation:
        if dic['username'] == username:
            characConv.append(dic['message'])
    phrases = ''.join(str(word) for word in characConv)
    return sia.polarity_scores(phrases)