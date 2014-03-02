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
import nltk
#==============================================================================
# import nltk, nltk.classify.util, nltk.metrics
# from nltk.classify import NaiveBayesClassifier
# from nlttk.metrics import BigramAssocMeasures
# from nltk.probability import FreqDist, ConditionalFreqDist
# import re, math
#==============================================================================

oscarmovies = {'\"12 years a slave\"':'\"oscars\"will\"win',
               '\"wolf of wall street\"':'\"oscars\"will\"win', 
               '\"nebraska\"':'\"oscars\"will\"win', 
               '\"captain phillips\"':'\"oscars\"will\"win', 
               '\"dallas buyers club\"':'\"oscars\"will\"win',
               '\"american hustle\"':'\"oscars\"will\"win',
               '\"gravity\"':'\"oscars\"will\"win',
               '\"#her\"':'\"oscars\"will\"win',
               '\"philomena\"':'\"oscars\"will\"win'}
               
om = oscarmovies


def oscarmoviestwittersearch():    
    L = []
    L2 = []
    t = Twitter()
    for key in om:
        for tweet in t.search(key + ' ' + om[key]):
            L.append(tweet.text)
            L2.append(sentiment(tweet.text))

    file = open('bestoscarmovietweets.txt','w')
    for i in L:
        file.write(str(i)+'\n')
    file.close()

    file = open('bestoscarmoviesentiments.txt','w')
    for i in L2:
        file.write(str(i)+'\n')
    file.close()

def openbestoscarmoviefiletweets():
    with open('bestoscarmovietweets.txt','r') as myfile:
        data = myfile.readlines()
    return data
    
def openbestoscarmoviefilesents():
    with open('bestoscarmoviesentiments.txt','r') as myfilesent:
        datasent = myfilesent.readlines()
    return datasent

def makingtweetslowercase(data):
    tweets = []
    for i in range(len(data)):
        tweets.append(data[i].lower())
    return tweets

def bestoscarmovieindex(lower_case_list):
    index = []
    for i in range(len(lower_case_list)):
        if '12 years a slave' in lower_case_list[i]:
            index.append(i)
    return index
    
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

if __name__ == "__main__":
    lower_case_list = makingtweetslowercase(openbestoscarmoviefiletweets())
    print bestoscarmovieindex(lower_case_list)