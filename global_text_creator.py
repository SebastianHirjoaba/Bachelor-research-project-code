# -*- coding: utf-8 -*-
"""
Created on Mon May 29 15:32:02 2023

@author: Sebastian Hirjoaba
"""

import nltk
import os 
import glob

for filename in glob.glob("Transcripts/*"):
    with open(filename, "r", encoding = 'utf-8') as infile:
        raw_text = infile.read()
    name = filename.replace("_interview.txt", "")
    rows = ["Line\tName\tSentence\tEmotion\n"]
    sentences = []
    counter = 1     

    text = nltk.sent_tokenize(raw_text)

    for sent in text:
        y = sent.replace("\n", "")
        if not y.startswith("Interviewer"):
            sentences.append(y)
            
    for x in sentences:
        row = str(counter) + "\t" + name + "\t" + x + "\t" + " " + "\n"
        rows.append(row)
        counter += 1 

    fulltext_tsv="".join(rows)        

    save_filename = os.path.normpath("texts.tsv")
    with open(save_filename, 'w', encoding = 'utf-8') as outfile:
        outfile.write(fulltext_tsv)
        