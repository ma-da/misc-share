# misc-share
Misc. scripts for parsing scraped data, nlp, graph building, etc

# WTKdbsort.ipynb is my current working notebook for generating and analyzing network graphs of the WTK news database
It takes a few files exported from .SQLite tables, turns these into a big dataframe, cleans and preps the data for advanced indexing/analysis, and outputs a file to the specifications of kumu.com's graph rendering platform.

This notebook can be made into the basis of a generalized tool. 

# parseWTKnews.py is a python 3.6 script best run in a jupyter notebook
It takes html source where each summary is in the form of samplesource.html and parses it with bs4 into a pandas dataframe. All records must begin with `<hr>`. Note that approx. 30,000 non UTF-8 characters are present per 23.6m characters (as of last collection). These must be converted or scrubbed in preprocessing or the parser will not work. For best results, total record set should be batched into files of fewer than 800 records each.

Note that this parser is too closely coupled to be generalized for use on other webpages. 
