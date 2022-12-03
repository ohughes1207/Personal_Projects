# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 05:08:42 2022

@author: Olliver
"""

import json
import pandas as pd

file = open('CloneWarsScraper/episodes.json')


data=json.load(file)


episode_n = [x['Episode Name'] for x in data]
episode_s = [x['Episode Synopsis'] for x in data]
slist = []
#Remove the notes from the episodes that have them
for s in episode_s:
    try:
        i=s.index('Note')
        s=s[:i-1]
        slist.append(s)
    except:
        slist.append(s)
    

clean_s =[]
for ls in slist:
    ls= [x.replace('\n', '') for x in ls if x != '\n']
    ls= ''.join(ls)
    clean_s.append(ls)

#print(episode_n)

clean_n = []

for ln in episode_n:
    ln= [x.replace('"', '')  for x in ln if x != '"']
    if len(ln)==1:
        clean_n.append(ln[0])
    else:
        print('Error occured somewhere')
    

cw_dict = {
    'name': clean_n,
    'synopsis': clean_s
    }

print(cw_dict['name'])

df=pd.DataFrame(cw_dict)
#df.to_csv('data/clonewars_cleaned.csv', index=False)