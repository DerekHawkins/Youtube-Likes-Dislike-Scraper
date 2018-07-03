# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 10:31:56 2018

@author: Derek.Hawkins
"""

import pafy
import pandas as pd

path = 'C:/Users/Derek.Hawkins/Documents/Python Training/Youtube_URLs.xlsx'
data = pd.read_excel(path)

videos = data['Youtube Links']    
dataSheet = []

for i in videos:
    clips = pafy.new(i)
    titles = clips.title
    upvotes = clips.likes
    downvotes = clips.dislikes
    dataSheet.append((titles, upvotes, downvotes))


df = pd.DataFrame(dataSheet, columns = ['Video Titles', 'Likes', 'Dislikes'])
df["URLs"] = videos
print(df)

#df.to_csv('C:/Users/Derek.Hawkins/Documents/Python Training/Youtube_MetaData.csv')