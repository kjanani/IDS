# Janani Kalyanam
# Scripts to run BTM

import os, sys

def run_btm_learning(inputfile, no_topics, vocab_file, alpha, beta, output_path):

    # Example:
    # ../BTM/src/btm est 150 3577 0.3 0.01 1000 10 data_processing_files/btm_input.txt output/BTM_OUTPUT/

    execute_string = '../BTM/src/btm est ' + str(no_topics) + ' ' + \
                str(len(open('data_processing_files/vocab.txt','r').readlines())) + ' ' + \
                str(float(50/K)) + ' ' + \
                str(beta) + ' ' + \
                str(1000) + ' ' + \
                str(10) + ' ' + \
                inputfile + ' ' + \
                output_path;


