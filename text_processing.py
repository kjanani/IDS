# Janani Kalyanam
# Jan 11 2018

import os, sys
import pymongo
import tweet_utils

def getvocab():

    fout = open('../output/vocab_full.txt','w');
    vocab = dict();
    ii = 0;
    for document in collection.find():
        ii += 1;
        print(ii)
        for x in tweet_utils.get_text_normalized(document):
            if x in vocab.keys():
                vocab[x] += 1;
            else:
                vocab[x] = 1;
    fout.write(str(vocab))

def convert_to_btm_input(vocab_file,output_file):
    client = pymongo.MongoClient();
    db = client['IDS'];
    collection = db.collection_hashtag;


    vocab = list(map(lambda x: x.strip().split(' ')[1], open(vocab_file,'r').readlines()));

    fid = open(output_file,'w');
    fid2 = open('../data_processing_files/btm_input_id_str.txt','w');
    ii = 0;
    for document in collection.find():
        ii += 1;
        print(ii)
        words = tweet_utils.get_text_normalized(document);
        print(words)
        jj = 0;
        myStr = '';
        for word in words:
            if(word in vocab):
                jj += 1;
                myStr = myStr + str(vocab.index(word)) + ' ';
        if(jj < 2):
            continue;
        fid.write(myStr+'\n');
        fid2.write(document['id_str']+'\n');                         
    fid.close();
    fid2.close()
    client.close()

if __name__ == '__main__':

    #getvocab();
    #convert_to_btm_input('../data_processing_files/vocab.txt','../data_processing_files/btm_input.txt');
