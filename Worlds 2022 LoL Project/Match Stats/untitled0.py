# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 10:38:34 2022

@author: Olliver
"""

import pandas as pd

data_l = ['Days 1-2.csv', 'Days 3-4.csv', 'Days 5-6.csv', 'Days 7-8.csv', 'Tiebreakers.csv', 'Quarterfinals.csv', 'Semifinals and Finals.csv']
df_list = [pd.read_csv('./data/'+x) for x in data_l]

keys= [x.split('.')[0] for x in data_l]


roles=['Top', 'Jungle', 'Mid', 'Bottom', 'Support']
df = pd.concat(df_list, keys=keys, ignore_index=True)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

print(df)