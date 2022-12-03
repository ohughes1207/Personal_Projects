# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import numpy as np
import time



url = 'https://lol.fandom.com/wiki/2022_Season_World_Championship/Main_Event/Scoreboards'

PATH = "C:\geckodriver.exe"
service = Service(PATH)
driver = webdriver.Firefox(service=service)
driver.get(url)
driver.implicitly_wait(10)
#Click element to accept cookies popup
driver.find_element('css selector', ".NN0_TB_DIsNmMHgJWgT7U").click()


daysTabs = driver.find_elements('xpath', '//div/div[2]/div[4]/div/div')
tabsArray = np.arange(1, len(daysTabs)+1)
i=1
for x in tabsArray:
    tabs=driver.find_element('xpath', '//div/div[2]/div[4]/div[' + str(x) +']/div')
    tab_name=tabs.text
    tabs.click()
    time.sleep(10)
    scoreboards_found = driver.find_elements('xpath', '/html/body/div[4]/div[3]/div[3]/main/div[3]/div[1]/div/div[2]/div/table/tbody')
    driver.implicitly_wait(20)
    showall = driver.find_element('css selector', 'div.expand-contract-button:nth-child(9) > span:nth-child(1)')
    showall.click()
    driver.implicitly_wait(20)
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable(('css selector', 'div.expand-contract-button:nth-child(9) > span:nth-child(1)'))).click()
    matchData = []
    for s in scoreboards_found:
        columns = ['Game Number', 'Match Length (minutes)', 'Side', 'Team', 'Top', 'Top Champion', 'Jungle', 'Jungle Champion', 'Mid', 'Mid Champion', 'Bottom', 'Bottom Champion', 'Support', 'Support Champion', 'Total Team Kills', 'Total Team Gold (k)', 'Towers', 'Inhibitors', 'Barons', 'Dragons', 'Heralds', 'Victory']
        BlueTeam= s.find_element('xpath', './tr[1]/th[1]/span/span[2]/a').text
        RedTeam= s.find_element('xpath', './tr[1]/th[3]/span/span[1]/a').text
        sides = s.find_elements('xpath', './tr[5]/td')
        teamStats = [s.find_element('xpath', './tr[3]/th[1]'), s.find_element('xpath', './tr[3]/th[3]')]
        gameLength = np.round((float(s.find_element('xpath', './tr[3]/th[2]').text.split(':')[0]) + np.divide(float(s.find_element('xpath', './tr[3]/th[2]').text.split(':')[1]), 60)), 2)
        objStats = s.find_elements('xpath', './tr[7]/td')
        teams = [BlueTeam, RedTeam]
        for side, team, obj, tstats in zip(sides, teams, objStats, teamStats):
            teamSide = side.get_attribute('class').split('-')[1].capitalize()
            topPlayer = side.find_element('xpath', './div[1]/div[4]/div[1]/a').text
            #print(topPlayer)
            topChamp = side.find_element('xpath', './div[1]/div/span').get_attribute('title')
            jgPlayer = side.find_element('xpath', './div[2]/div[4]/div[1]/a').text
            #print(jgPlayer)
            jgChamp = side.find_element('xpath', './div[2]/div/span').get_attribute('title')
            midPlayer = side.find_element('xpath', './div[3]/div[4]/div[1]/a').text
            midChamp = side.find_element('xpath', './div[3]/div/span').get_attribute('title')
            botPlayer = side.find_element('xpath', './div[4]/div[4]/div[1]/a').text
            botChamp = side.find_element('xpath', './div[4]/div/span').get_attribute('title')
            suppPlayer = side.find_element('xpath', './div[5]/div[4]/div[1]/a').text
            suppChamp = side.find_element('xpath', './div[5]/div/span').get_attribute('title')

            towerStats = obj.find_element('xpath', './div/div[2]/div[1]').text
            inhibitorStats = obj.find_element('xpath', './div/div[2]/div[2]').text
            baronStats = obj.find_element('xpath', './div/div[2]/div[3]').text
            dragonStats = obj.find_element('xpath', './div/div[2]/div[4]').text
            heraldStats = obj.find_element('xpath', './div/div[2]/div[5]').text

            Victory = 1 if tstats.find_element('xpath', './div/div[1]').text=='Victory' else 0
            TeamGold = tstats.find_element('xpath', './div/div[2]').text.replace('k', '')
            TeamKills = tstats.find_element('xpath', './div/div[3]').text


            sideData = [str(i), gameLength, teamSide, team, topPlayer, topChamp, jgPlayer, jgChamp, midPlayer, midChamp, botPlayer, botChamp, suppPlayer, suppChamp, TeamKills, TeamGold, towerStats, inhibitorStats, baronStats, dragonStats, heraldStats, Victory]
            data_dict = {k:v for (k,v) in zip(columns, sideData)}
            matchData.append(data_dict)

        data_dict = {k:v for (k,v) in zip(columns, matchData)}
        df=pd.DataFrame.from_records(matchData)
        df.to_csv('../data/'+ str(tab_name) + '.csv', index=False)
        i+=1
        
driver.quit()