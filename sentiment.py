from textblob import TextBlob
from errorHandler import jsonErrorHandler
import conversations
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentimentText(chatname):
    text = conversations.getListChat(chatname)
    sia = SentimentIntensityAnalyzer()
    #Needs to be a string of phrases
    if type(text) != str():
        raise ValueError("Text needs to be a string") 
    else:
        return sia.polarity_scores(text)
