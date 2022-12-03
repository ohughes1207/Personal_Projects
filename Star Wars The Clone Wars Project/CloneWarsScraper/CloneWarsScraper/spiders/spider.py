# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 10:38:47 2022

@author: Olliver
"""

import scrapy



class CloneWarsSpider(scrapy.Spider):
    name = 'clonewars'   
    start_urls = ['https://en.wikipedia.org/wiki/List_of_Star_Wars:_The_Clone_Wars_episodes']
        
    def parse(self, response):
        for season in response.css('table.wikitable.plainrowheaders.wikiepisodetable')[1:]:
            for episode_n, episode_s in zip(season.css('tbody tr.vevent'), season.css('tbody tr.expand-child')):
                yield {
                    'Episode Name': episode_n.css('td.summary ::text').getall(),
                    'Episode Synopsis': episode_s.css('td.description ::text').getall(),
                }                
                
