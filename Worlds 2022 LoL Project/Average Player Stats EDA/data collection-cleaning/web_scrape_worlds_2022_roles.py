# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 10:50:50 2022

@author: Olliver
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import numpy as np

#We will be scraping data for each role separately to further break down the data for analysis
roles = ['Top', 'Jungle', 'Mid', 'Bot', 'Support']

for role in roles:
    #Scrape data of players for each role separately
    url = 'https://lol.fandom.com/wiki/Special:RunQuery/TournamentStatistics?TS%5Bpreload%5D=TournamentByPlayerRole&TS%5Brole%5D='+ role +'&TS%5Btournament%5D=2022+Season+World+Championship%2FMain+Event&_run='
    
    PATH = "C:\geckodriver.exe"
    service = Service(PATH)
    driver = webdriver.Firefox(service=service)
    driver.get(url)
    driver.implicitly_wait(5)
    #Click element to accept cookies popup
    driver.find_element('css selector', ".NN0_TB_DIsNmMHgJWgT7U").click()
    #Champions Played column is sorted in descending order so at the end we can append null values the 2nd and 3rd most played for players who only played a single champion
    driver.implicitly_wait(5)
    driver.find_element('xpath', "//table/thead/tr[3]/th[20]").click()
    driver.find_element('xpath', "//table/thead/tr[3]/th[20]").click()
    
    #Scrape data from all columns in the table and define a list for each parameter using list comprehension
    teams = driver.find_elements("xpath", '//table/tbody/tr/td/a/img')
    teams = [x.get_attribute("alt").replace('logo std.png', '').replace('.NA', '') for x in teams]
    
    player_names = driver.find_elements("xpath", '//table/tbody/tr/td[2]/a')
    player_names = [x.text for x in player_names]
    
    num_games = driver.find_elements("xpath", '//table/tbody/tr/td[3]/a')
    num_games = [x.text for x in num_games]
    
    num_wins = driver.find_elements("xpath", '//table/tbody/tr/td[4]')
    #Use len of player_names and num_wins as index to remove incorrect data
    num_wins = [x.text for x in num_wins[:len(player_names)-len(num_wins)]]
    
    num_losses = driver.find_elements("xpath", '//table/tbody/tr/td[5]')
    num_losses = [x.text for x in num_losses]
    
    wr = driver.find_elements("xpath", '//table/tbody/tr/td[6]')
    wr = [x.text for x in wr]
    
    kills = driver.find_elements("xpath", '//table/tbody/tr/td[7]')
    kills = [x.text for x in kills]
    
    deaths = driver.find_elements("xpath", '//table/tbody/tr/td[8]')
    deaths = [x.text for x in deaths]
    
    assists = driver.find_elements("xpath", '//table/tbody/tr/td[9]')
    assists = [x.text for x in assists]
    
    kda = driver.find_elements("xpath", '//table/tbody/tr/td[10]')
    kda = [x.text for x in kda]
    
    cs = driver.find_elements("xpath", '//table/tbody/tr/td[11]')
    cs = [x.text for x in cs]
    
    cspm = driver.find_elements("xpath", '//table/tbody/tr/td[12]')
    cspm = [x.text for x in cspm]
    
    gold = driver.find_elements("xpath", '//table/tbody/tr/td[13]')
    gold = [x.text for x in gold]
    
    gold_pm = driver.find_elements("xpath", '//table/tbody/tr/td[14]')
    gold_pm = [x.text for x in gold_pm]
    
    dmg = driver.find_elements("xpath", '//table/tbody/tr/td[15]')
    dmg = [x.text for x in dmg]
    
    dmg_pm = driver.find_elements("xpath", '//table/tbody/tr/td[16]')
    dmg_pm = [x.text for x in dmg_pm]
    
    kill_par = driver.find_elements("xpath", '//table/tbody/tr/td[17]')
    kill_par = [x.text for x in kill_par]
    
    kill_share = driver.find_elements("xpath", '//table/tbody/tr/td[18]')
    kill_share = [x.text for x in kill_share]
    
    gold_s = driver.find_elements("xpath", '//table/tbody/tr/td[19]')
    gold_s = [x.text for x in gold_s]
    
    cp = driver.find_elements("xpath", '//table/tbody/tr/td[20]')
    cp = [x.text for x in cp]
    
    mp1 = driver.find_elements("xpath", '//table/tbody/tr/td[21]/a[1]/span')
    mp1 = [x.get_attribute("title") for x in mp1]
    
    mp2 = driver.find_elements("xpath", '//table/tbody/tr/td[21]/a[2]/span')
    mp2 = [x.get_attribute("title") for x in mp2]
    #Because we sorted table by champions played in descending order we can safely append null values for mp2 and mp3 for the correct players
    while len(mp2) != len(mp1):
        mp2.append(np.NaN)
    
    mp3 = driver.find_elements("xpath", '//table/tbody/tr/td[21]/a[3]/span')
    mp3 = [x.get_attribute("title") for x in mp3]
    while len(mp3) != len(mp1):
        mp3.append(np.NaN)
    
    columns = ['Team', 'Player Name', 'Games', 'Wins', 'Losses', 'Win Rate %', 'Kills', 'Deaths', 'Assists', 'KDA', 'Creep Score (CS)', 'CS per minute', 'Gold', 'Gold per minute', 'Damage', 'Damage per minute', 'Kill Participation %', 'Kill Share %', 'Gold Share %', 'Unique Champions', '1st Most Played', '2nd Most Played', '3rd Most Played']
    data = [teams, player_names, num_games, num_wins, num_losses, wr, kills, deaths, assists, kda, cs, cspm, gold, gold_pm, dmg, dmg_pm, kill_par, kill_share, gold_s, cp, mp1, mp2, mp3]
    
    #define dict to be used to create the dataframe
    data_dict = {k:v for (k,v) in zip(columns, data)}
    
    df= pd.DataFrame.from_dict(data_dict)
    #Save the dataframe as csv to then be cleaned
    df.to_csv('./data/'+role+'_df_unclean.csv', index=False)
    driver.quit()