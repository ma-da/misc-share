# misc-share
Misc. scripts for parsing scraped data, nlp, graph building, etc

# vectorSearch.html
One pager using Pyscript to search the WantToKnow.info news database using TF-IDF vector cosine similarity.

# preprocess.ipynb
Updated code for turning the WantToKnow.info articles database into a useful dataset and identifying related article groupings using cosine similarity.

# ULTRA.ipynb

An ipython python notebook used to sort 17,612 document images using K-means clustering

# MAPpreprocess.ipynb 
...is for preprocessing the WTK articles database into a dataset

# MAPnlp.ipynb
... contains snippets for NLP using SpaCy, deduplication using fuzzywuzzy, and ngram generation

# MAPmaker.ipynb
...is used to make the economic system corruption news map demonstrated in https://www.youtube.com/watch?v=lW9tvgH5r_w

# WTKdbsort.ipynb is a starting-point notebook for generating and analyzing network graphs of the WTK news database
It takes a few files exported from .SQLite tables, turns these into a big dataframe, cleans and preps the data for advanced indexing/analysis, and outputs a file to the specifications of kumu.com's graph rendering platform.

This notebook can be made into the basis of a generalized tool. 

# parseWTKnews.py is a python 3.6 script best run in a jupyter notebook
It takes html source where each summary is in the form of samplesource.html and parses it with bs4 into a pandas dataframe. All records must begin with `<hr>`. Note that approx. 30,000 non UTF-8 characters are present per 23.6m characters (as of last collection). These must be converted or scrubbed in preprocessing or the parser will not work. For best results, total record set should be batched into files of fewer than 800 records each.

Note that this parser is too closely coupled to be generalized for use on other webpages. 
