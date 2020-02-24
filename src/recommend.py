import pandas as pd
import numpy as np
from pymongo import MongoClient
from errorHandler import jsonErrorHandler
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as distance

client = MongoClient("mongodb://localhost/Conversations")
db = client.get_database()

def recommendCharacter(username):
    #Dictionary with all conversations
    doc = {}
    characters = [character['username'] for character in list(db['Conversations'].distinct('Characters'))]
    for character in characters:
        i = list(list(db['Users'].find({'username': character}, {'_id':1, 'Group':1}))[0].values())
        conversation = list(db['Conversations'].find({'Group':i[1]}))[0]['Message']
        characConv = []
        for dic in conversation:
            if dic['username'] == character:
                characConv.append(dic['message'])
        phrases = ''.join(str(word) for word in characConv)

        dic = {character: phrases}
        doc.update(dic)
        
    #Vectorizer
    count_vectorizer = CountVectorizer()
    sparse_matrix = count_vectorizer.fit_transform(doc.values())
    doc_term_matrix = sparse_matrix.todense()
    df = pd.DataFrame(doc_term_matrix, 
              columns=count_vectorizer.get_feature_names(), 
              index=doc.keys())

    #Similarity
    similarity_matrix = distance(df,df)
    sim_df = pd.DataFrame(similarity_matrix, columns=doc.keys(), index=doc.keys())
    np.fill_diagonal(sim_df.values, 0) # Remove diagonal max values and set those to 0
    sim_df.idxmax()

    #Recommendation
    rec = sim_df.loc[username].idxmax()
        
    return rec