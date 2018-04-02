# misc-share
Misc. scripts for parsing scraped data, nlp, graph building, etc

# parseWTKnews.py is a python 3.6 script best run in a jupyter notebook
It takes html source where each summary is in the form of samplesource.html and parses it with bs4 into a pandas dataframe. All records must begin with `<hr>`. Note that approx. 30,000 non UTF-8 characters are present per 23.6m characters (as of last collection). These must be converted or scrubbed in preprocessing or the parser will not work. For best results, total record set should be batched into files of fewer than 800 records each.

Note that this parser is too closely coupled to be generalized for use on other webpages. 
