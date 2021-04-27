import pandas as pd
import numpy as np
import glob
import os
import xml.etree.ElementTree as ET
import xml.etree.ElementTree as ET




def extract_filename(file):
    base = os.path.basename(file)
    filename = os.path.splitext(base)[0]
    return filename

def get_tweets(xml_file):
    '''make a list of all tweets in an xml file.'''
    mytree = ET.parse(xml_file)
    myroot = mytree.getroot()
    tweets = []
    for x in myroot[0].findall('document'):
        tweet = x.text
        tweets.append(tweet)
    return tweets

def read_all_data(path_to_data):
    """Reads all data from XML and Text into Python"""
    path_to_text = path_to_data + 'truth.txt'
    labels = pd.read_csv(path_to_text, delimiter = "\:::",header = None)
    labels.rename(columns={0: 'id', 1: 'bot', 2: 'sex'}, inplace=True)
    path_to_xml = path_to_data + '/*.xml'
    xml = glob.glob(path_to_xml, recursive=False)
    ids = []
    for i in range(len(xml)):
        file = xml[i]
        file_id = extract_filename(file)
        ids.append(file_id)
    mytree = ET.parse(xml[0])
    myroot = mytree.getroot()
    all_tweets = []
    for i in range(len(ids)):
        tweets = get_tweets(xml[i])
        filename = ids[i]
        for i in range(len(tweets)):
            pair = [filename, tweets[i]]
            all_tweets.append(pair)
    tweet_df = pd.DataFrame(all_tweets)
    tweet_df = tweet_df.rename(columns = {0:"tweet_id", 1:'tweets'})
    tweet_df['bot'] = tweet_df['tweet_id'].map(labels.set_index('id')['bot'])
    return tweet_df







