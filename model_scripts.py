# Janani Kalyanam
# Scripts to run BTM

import os, sys
import pymongo
import json
import text_processing

def run_btm_learning(inputfile, no_topics, vocab_file, alpha, beta, total_number_of_iterations, save_step, output_path):

    # Example:
    # ../../BTM/src/btm est 150 3577 0.3 0.01 1000 10 data_processing_files/btm_input.txt output/BTM_OUTPUT/

    execute_string = '../../BTM/src/btm est ' + str(no_topics) + ' ' + \
                str(len(open(vocab_file,'r').readlines())) + ' ' + \
                str(alpha) + ' ' + \
                str(beta) + ' ' + \
                str(1000) + ' ' + \
                str(10) + ' ' + \
                inputfile + ' ' + \
                output_path;

    print(execute_string);
    os.system(execute_string);


def run_btm_inference(no_topics,inputfile,output_path):

    # Example
    # ../../BTM/src/btm inf sum_b 150 ../data_processing_files/btm_input.txt ../output/BTM_OUTPUT/models/first_run/

    execute_string = '../../BTM/src/btm inf sum_b ' + str(no_topics) + ' ' + \
            inputfile + ' ' + \
            output_path;

    print(execute_string);
    os.system(execute_string);


def getHashtags(topic_decomp_file,id_str_file,output_file):
    '''
    given a topic number and the topic decomposition file -- find the top hashtags (and some related tweets) in that topic.
    output_file = dictionary where keys are the topic numbers.  Values again a dictionary of 10 hashtags.. with keys being 5 most prominent tweets
    '''

    fout = open(output_file,'w');

    # Make connections to the database and collection
    client = pymongo.MongoClient();
    collection_hashtags = client['IDS']['collection_hashtag'];
    doc_by_topics = list(map(lambda x: list(map(lambda y: float(y), x.strip().split(' '))), open(topic_decomp_file,'r').readlines()));

    # list of dominant topic
    docs_sorted_topics = list(map(lambda z: z[0][0], list(map(lambda y: sorted(enumerate(y), key = lambda x: x[1], reverse = True), doc_by_topics))));
    
    # list of tweet ids
    id_str = list(map(lambda x: x.strip(), open(id_str_file, 'r').readlines()));
   

    for ii in range(len(id_str)):
        temp_result = collection_hashtags.find({'id_str':id_str[ii]}).next();
        hashtags_ = list(map(lambda x: str.lower(x['text']), temp_result['entities']['hashtags']));
        print(str(ii) + ' ' + str(id_str[ii]) + ' ' + str(docs_sorted_topics[ii]) + ' ' + '-'.join(hashtags_))
        fout.write(str(id_str[ii]) + ' ' + str(docs_sorted_topics[ii]) + ' ' + '-'.join(hashtags_) + '\n');
def get_relevant_hashtags(tweet):

    vocab_file = '/Users/jananikalyanam/Documents/insight_application/PROJECT/output/BTM_OUTPUT/models/first_run/vocab.txt';
    no_topics = 150;
    hashtags_list = list(map(lambda x: x.strip().split()[0], open('/Users/jananikalyanam/Documents/insight_application/PROJECT/data_processing_files/hashtag_counts_new.txt','r').readlines()))[:500];
    topic_hashtag_tweets = eval(open('/Users/jananikalyanam/Documents/insight_application/PROJECT/output/BTM_OUTPUT/models/first_run/topic_hashtags_tweets_k150.txt').read());
    [btm_number_input, btm_vocab_input] = text_processing.convert_to_btm_input_test(vocab_file,tweet);

    user_tweet_file = '/Users/jananikalyanam/Documents/insight_application/PROJECT/user_io/user_tweet.txt';
    output_path = '/Users/jananikalyanam/Documents/insight_application/PROJECT/user_io/'
    fout = open(user_tweet_file,'w');
    fout.write(btm_number_input);
    fout.close();

    run_btm_inference(no_topics,user_tweet_file,output_path);
    doc_by_topic = list(map(lambda x: list(map(lambda y: float(y), x.strip().split())), open(output_path+'k'+str(no_topics)+'.pz_d').readlines()));
    dominant_topic = list(map(lambda x: x[0], sorted(enumerate(doc_by_topic[0]), key = lambda x: x[1], reverse=True)))[0];

    smaller = list(set(hashtags_list).intersection(set(topic_hashtag_tweets[dominant_topic][1])));
    return smaller;


if __name__ == '__main__':

    ### Train and Infer from BTM
    #inputfile = '../data_processing_files/btm_input.txt';
    #no_topics = 150;
    #vocab_file = '../data_processing_files/vocab.txt';
    #alpha = float(50/no_topics);
    #beta = 0.01;
    #total_number_of_iterations = 1000;
    #save_step = 10;
    #output_path = '../output/BTM_OUTPUT/models/first_run/';
    #run_btm_learning(inputfile, no_topics, vocab_file, alpha, beta, total_number_of_iterations, save_step, output_path);
    #run_btm_inference(no_topics,inputfile,output_path);

    # Find the topic_hashtag_tweets
    # topic_decomp_file = '../output/BTM_OUTPUT/models/first_run/k150.pz_d'
    # output_file = '../output/BTM_OUTPUT/models/first_run/simple_output.txt'
    # id_str_file = '../output/BTM_OUTPUT/models/first_run/btm_input_id_str.txt'
    # getHashtags(topic_decomp_file,id_str_file,output_file);


    # Find relevant hashtags for test tweets
    tweet = 'i love golden globe awards i think they are awesome'
    get_relevant_hashtags(tweet);
