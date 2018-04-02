#better functional script to parse wtk archive source into panda's dataframe.
import os
import re
import bs4
from bs4 import BeautifulSoup as soup
import pandas as pd

#hard-coded filepath can be replaced with directory iteration. Preprocessed HTML source begins with first "<hr>" tag in body

HtmlFile = open('C:\\datasources\\wtk1to793.html', 'r', encoding='utf-8')
source_code = HtmlFile.read()
#HtmlFile.close()

Rsoup = soup(source_code,'lxml')

Raw_stories = Rsoup.find_all(['div', {"style": "font-size:14pt"}, 'div', {"style": "font-size:12pt"}, 'p'])

#use loop below to confirm file has been preprocessed correctly and get count of articles in file
'''    
Story = []

for i in range(0, len(Raw_stories), 6):
    Story.append(Raw_stories[i : i+6])
'''
#initialize some lists

Headlines = []
Datesources = []
News_source_links = []
Quotes = []
Summaries = []
Note_text = []
Adtl_ref_links = []
Note_ref_links = []

#create other lists from beautifulsoup oblects

titles_list = Raw_stories[0::6]
date_sources = Raw_stories[1::6]
story_links = Raw_stories[2::6]
raw_sums = Raw_stories[4::6]
notes = Raw_stories[5::6]

#simple loops make columns

for i in titles_list:
    headline = i.text
    Headlines.append(headline)

for i in date_sources:
    datesource = i.text
    Datesources.append(datesource)

for i in story_links:
    story_link = i.a
    News_source_links.append(story_link)

#these loops extract important stuff from summmaries and summary notes	
	
for i in raw_sums:
    try:
        quote = i.strong.text
    except (AttributeError):
        quote = i.text.split('. ')[0]
    summary = i.text
    ref_links = []
    xlinks = i.a
    ref_links.append(xlinks)
    Quotes.append(quote)
    Summaries.append(summary)
    Adtl_ref_links.append(ref_links)

for i in notes:
    note = i.text
    note_links = []
    nlinks = i.a
    note_links.append(nlinks)
    Note_text.append(note)
    Note_ref_links.append(note_links)

#make initial dataframe from populated columns	
    
df = pd.DataFrame({'Headline': Headlines,
                  'Datesource': Datesources,
                  'News_source_link': News_source_links,
                  'Quote': Quotes,
                  'News_summary': Summaries,
                  'Note': Note_text,
                  'Summary_ref_links': Adtl_ref_links,
                  'Note_ref_links': Note_ref_links})

#check to make sure it looks right				  
df.head(5)

#split delimited values in DataFrame 'Datesource' column into new 'Date' and 'News_source' columns
df['Date'], df['News_source'] = df['Datesource'].str.split(' ', 1).str

#drops now-unused datesource column
df.drop('Datesource', axis=1, inplace=True)

#checks that all columns are present. Object dtypes easily changed as needed.
df.dtypes

