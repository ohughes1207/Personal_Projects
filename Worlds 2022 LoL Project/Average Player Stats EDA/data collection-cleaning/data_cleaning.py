# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 11:10:01 2022

@author: Olliver
"""

import pandas as pd

roles=['Top', 'Jungle', 'Mid', 'Bot', 'Support']

#Data will be cleaned for each csv file individually through the use of a for loop
for role in roles:
    
    df=pd.read_csv('./data/'+role+'_df_unclean.csv')
    
    #Removes the "%" and "k" from the series that contain them and converts them to float
    df['Win Rate %'] = df['Win Rate %'].apply(lambda x: float(x[:-1]))
    df['Kill Participation %'] = df['Kill Participation %'].apply(lambda x: float(x[:-1]))
    df['Damage'] = df['Damage'].apply(lambda x: float(x[:-1]) * 1000)
    df['Kill Share %'] = df['Kill Share %'].apply(lambda x: float(x[:-1]))
    df['Gold Share %'] = df['Gold Share %'].apply(lambda x: float(x[:-1]))
    
    #Save the cleaned data as a csv file in the /data directory
    df.to_csv('./data/'+role+'_df.csv', index=False)