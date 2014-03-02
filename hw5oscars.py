# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:18:00 2014

@author: ychen1
"""

""" Goal of the project: To use python and pattern.web to parse through news articles
from google that state oscar predictions, in order to use sentiment analysis to extract data
and predict the oscars based off of all of the oscar predictions. If this doesn't work,
we will use twitter stream to use sentiment analysis on all of the twitters related to the
oscars, in order to predict what will be the best picture, best actress, best actor and best
director! 
"""

from pattern.web import *
from pattern.en import *
import matplotlib.pyplot as plt

oscarmovies = {'\"12 years a slave\"':'\"oscars\"will\"win',
               '\"wolf of wall street\"':'\"oscars\"will\"win', 
               '\"nebraska\"':'\"oscars\"will\"win', 
               '\"captain phillips\"':'\"oscars\"will\"win', 
               '\"dallas buyers club\"':'\"oscars\"will\"win',
               '\"american hustle\"':'\"oscars\"will\"win',
               '\"gravity\"':'\"oscars\"will\"win',
               '\"#her\"':'\"oscars\"will\"win',
               '\"philomena\"':'\"oscars\"will\"win'}
               
om = oscarmovies    #initializes a dictionary that we can use to search through Twitter for

def oscarmoviestwittersearch():
    """ This function, which we only run once, produces a set of tweets that we can work with in a plaintext
    file. The output of this function is a file containing all of our tweets, separated by /n """
    L = []
    L2 = []
    t = Twitter()
    for key in om:  #loops through all the keys in the dictionary, searching tweets for movie titles and words "Oscars", "will", and "win"
        for tweet in t.search(key + ' ' + om[key]):
            L.append(tweet.text)
            L2.append(sentiment(tweet.text))

    file = open('bestoscarmovietweets.txt','w') #opens a new file, writes all of our tweets to this file, and closes file
    for i in L:
        file.write(str(i)+'\n')
    file.close()

def openbestoscarmoviefiletweets():
    """ This function opens the plaintext file and outputs it as a varaible that can be called"""
    with open('bestoscarmovietweets.txt','r') as myfile:
        data = myfile.readlines()
    return data
    
def makingtweetslowercase(data):
    """This helps us search through all of the tweets by making all of the text in the tweets lowercase. The 
    function also creates a list of all our tweets which makes it easy for us to loop through them and search
    for the relevant information we need"""
    tweets = []
    for i in range(len(data)):
        tweets.append(data[i].lower())  #so we simultaneously make all of the tweets lowercase while appending them to a list
    return tweets

def finding_sentiment_analysis(index, lower_case_list):
    """ This function takes as input a list of all the indices for the tweets which mentioned the relevant movie
    and the full data-set of tweets. Then, using the indices it has found, it produces the indvidual sentiments
    of each relevant tweet. """
    sent_index = []
    for j in index: #loops through all the relevant tweets that pertain to each movie, find the sentiment analysis, and append it to a list
        sent_index.append((sentiment(lower_case_list[j])))
    return sent_index

def finding_tot_sentiment_for_movie(sent_index):
    """ This function takes as input the list of all of the sentiments, takes only the first sentiment value which
    indicates the postivity or negatviity of the tweet, and sums all of the sentiments """
    tot_sent = 0    #initializes starting value for total sentiment for each movie at 0
    for i in sent_index:
        tot_sent += i[0]
    return tot_sent
    
##############################################################################################################

if __name__ == "__main__":
    
    lower_case_list = makingtweetslowercase(openbestoscarmoviefiletweets()) #lower_case_list contains all of the tweets, in lowercase, in a list
    
    #we initialize a bunch of empty lists to store the indices of each tweet that contain any of these movie names
    index_12yearsaslave = []
    index_wolf = []
    index_nebraska = []
    index_captainphillips = []
    index_dallas = []
    index_ah = []
    index_gravity = []
    index_her = []
    index_philomena = []
        
    for i in range(len(lower_case_list)):
        if '12 years a slave' in lower_case_list[i]:
            index_12yearsaslave.append(i)
        if 'wolf of wall street' in lower_case_list[i]:
            index_wolf.append(i)
        if 'nebraska' in lower_case_list[i]:
            index_nebraska.append(i)
        if 'gravity' in lower_case_list[i]:
            index_gravity.append(i)
        if 'captain phillips' in lower_case_list[i]:
            index_captainphillips.append(i)
        if 'dallas buyers club' in lower_case_list[i]:
            index_dallas.append(i)
        if 'american hustle' in lower_case_list[i]:
            index_ah.append(i)
        if '#her' in lower_case_list[i]:
            index_her.append(i)
        if 'philomena' in lower_case_list[i]:
            index_philomena.append(i)
    
    #we chose to do this outside of a function so that we have access to all of these lists individually, without appending them all into one huge list
    
    sent_12yearsaslave = finding_sentiment_analysis(index_12yearsaslave, lower_case_list)
    sent_wolfofwallstreet = finding_sentiment_analysis(index_wolf, lower_case_list)
    sent_nebraska = finding_sentiment_analysis(index_nebraska, lower_case_list)
    sent_captainphillips = finding_sentiment_analysis(index_captainphillips, lower_case_list)
    sent_dallas = finding_sentiment_analysis(index_dallas, lower_case_list)
    sent_ah = finding_sentiment_analysis(index_ah, lower_case_list)
    sent_gravity = finding_sentiment_analysis(index_gravity, lower_case_list)
    sent_her = finding_sentiment_analysis(index_her, lower_case_list)
    sent_philomena = finding_sentiment_analysis(index_philomena, lower_case_list)

    a = finding_tot_sentiment_for_movie(sent_12yearsaslave)
    b = finding_tot_sentiment_for_movie(sent_wolfofwallstreet)
    c = finding_tot_sentiment_for_movie(sent_nebraska)
    d = finding_tot_sentiment_for_movie(sent_captainphillips)
    e = finding_tot_sentiment_for_movie(sent_dallas)
    f = finding_tot_sentiment_for_movie(sent_ah)
    g = finding_tot_sentiment_for_movie(sent_gravity)
    h = finding_tot_sentiment_for_movie(sent_her)
    k = finding_tot_sentiment_for_movie(sent_philomena)
    
    #using matplotlib to produce a pie chart of the probabilities of each movie to win Best Picture for the Oscars
    sumofsentiments = (a+b+c+d+e+f+g+h+k)/100
    sizes = [a/sumofsentiments,
             b/sumofsentiments,
             c/sumofsentiments,
             d/sumofsentiments,
             e/sumofsentiments,
             f/sumofsentiments,
             g/sumofsentiments,
             h/sumofsentiments,
             k/sumofsentiments]
    
    labels = ['12 Years a Slave','The Wolf of Wall Street','Nebraska','Gravity',
              'Captain Phillips','Dallas Buyers Club','American Hustle','Her','Philomena']
    colors = ['yellowgreen','gold','orange','red','lightskyblue','blue','lightcoral','purple','magenta']
    font = {'size':12}    
    plt.rc('font',**font)
    plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

################################

#bestactor = {'\"Leonardo\"Dicaprio\"':'\"oscars\"best actor\"will win',
#             '\"Matthew\"Mcconaughey\"':'\"oscars\"best actor\"will win',
#             '\"Christian\"Bale\"': '\"oscars\"best actor\"will win',
#             '\"Bruce\"Dern\"':'\"oscars\"best actor\"will win',
#             '\"Chiwetel\"Ejiofor\"':'\"oscars\"best actor\"will win'}
#
#ba = bestactor
#
#for key, val in ba.iteritems():
#    print key,val
#t = Twitter()
#for key in ba:
#    for tweet in t.search(key + ' ' + ba[key]):
#        print tweet.text
#        print ""
#        i = tweet.id
#        print sentiment(tweet.text)
#        print ""
#        
#################################
#
#bestactress = {'\"Amy Adams\"':'\"oscars\"best actress\"will win',
#               '\"Cate Blanchett\"':'\"oscars\"best actress\"will win',
#               '\"Sandra Bullock\"':'\"oscars\"best actress\"will win',
#               '\"Judi Dench\"':'\"oscars\"best actress\"will win',
#               '\"Meryl Streep\"':'\"oscars\"best actress\"will win'}
#              
#bas = bestactress
#
#for key,val in bas.iteritems():
#    print key,val
#t = Twitter()
#for key in bas:
#    for tweet in t.search(key+ ' ' + bas[key]):
#        print tweet.text
#        print ""
#        i = tweet.id
#        print sentiment(tweet.text)
#        
####################################
#
#bestdirector = {'\"David O\'Russell\"':'\"oscars\"best director\"will win',
#                '\"Alfonso Cuaron\"': '\"oscars\"best director\"will win',
#                '\"Alexander Payne\"':'\"oscars\"best director\"will win',
#                '\"Steve McQueen\"':'\"oscars\"best director\"will win',
#                '\"Martin Scorsese\"':'\"oscars\"best director\"will win'}
#                
#bd = bestdirector
#
#for key,val in bd.iteritems():
#    print key,val
#t = Twitter()
#for key in bd:
#    for tweet in t.search(key+ ' ' + bd[key]):
#        print tweet.text
#        print ""
#        i = tweet.id
#        print sentiment(tweet.text)

