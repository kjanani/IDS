# Janani Kalyanam
# January 11 2018

# finding some stats about the data

import os, sys
import pymongo
import glob
import json
import re

def stats():

    client = pymongo.MongoClient();
    db = client['IDS'];
    collection = db['collection_hashtag'];


    list_hashtags = list(map(lambda x: str.lower(x['text']), collection.distinct('entities.hashtags')));
    list_hashtags = list(set(list_hashtags)); # distinct, lower case
    print('#-distinct hashtags: ' + str(len(list_hashtags)));

    hashtag_count = dict.fromkeys(list_hashtags);
    
    ii = 0;
    for k in iter(hashtag_count.keys()):
        ii += 1;
        if(ii%1000 == 0):
            print(ii)
            fout = open('../output/hashtag_counts'+str(ii)+'.txt','w')
            fout.write(str(hashtag_count));
        hashtag_count[k] = collection.find({ 'entities.hashtags.text':  re.compile('^'+k+'$', re.IGNORECASE)}).count();

    fout.write(str(hashtag_count));
    

if __name__ == '__main__':
    stats();
