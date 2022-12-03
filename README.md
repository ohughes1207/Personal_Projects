# Personal Projects

- [My Academic Projects](https://github.com/ohughes1207/Academic_Projects)

<details><summary><strong>Projects I am currently working on</strong></summary> 
<br>

1. [Worlds 2022 LoL Project](https://github.com/ohughes1207/Personal_Projects/tree/main/Worlds%202022%20LoL%20Project)
2. [Star Wars The Clone Wars Project](https://github.com/ohughes1207/Personal_Projects/tree/main/Star%20Wars%20The%20Clone%20Wars%20Project)

</details>
  
## Introduction

Currently both of my personal projects are a work in progress and so, as the projects develop the README.md of this repository will be expanded upon.

## Worlds 2022 LoL Project

The esports scene has grown rapidly over the recent years with some games being more popular than others. League of Legends (LoL) is a multiplayer online battle arena (MOBA) game where 2 teams of 5 players select a character (referred to as champions in-game) to play as and work together to destroy a struture within the opposing teams base called the Nexus. The LoL esports scene is one of the largest, being in the top 5 biggest and most popular esports scenes. It's largest tournament is the World Championship where teams from all regions compete to win, the World Championship typically takes place in October each year. Being a fan of the game and it's esports scene I wanted to determine what where the deciding factors in the recent World Championship that took place this year and recently concluded as of writing, this World Championship took place from 29/09/2022 to 5/11/2022.

Currently the data has been collected using web scraping techniques with Selenium and the web scraped data has been cleaned using a Python script. Two datasets have been created, one dataset contains the average stats of each player and the other contains the stats scraped from the endgame scoreboards of all 80 matches that took place in the tournament. The average player stats were scraped from [here](https://lol.fandom.com/wiki/2022_Season_World_Championship/Main_Event/Player_Statistics) and the match stats were scraped from [here](https://lol.fandom.com/wiki/2022_Season_World_Championship/Main_Event/Scoreboards)

<h4 align=center> Match stats dataset </h4>

![](https://raw.githubusercontent.com/ohughes1207/Personal_Projects/main/Worlds%202022%20LoL%20Project/Match%20Stats/figs/dataset.PNG)

<h4 align=center> Average player stats dataset </h4>

![](https://raw.githubusercontent.com/ohughes1207/Personal_Projects/main/Worlds%202022%20LoL%20Project/Average%20Player%20Stats%20EDA/figs/dataset.PNG)

## Star Wars The Clone Wars Project

Star Wars The Clone Wars is an animated series that takes place in the Star Wars universe and tells the events that occured between Episode II and Episode III. Being a huge fan of the Star Wars franchise, I wanted to build an episode synopsis generator to see if through machine learning, episode synopsis could be generated and if it could would they be coherent and make sense. Because of my knowledge of the Star Wars universe and it's lore, I can determine if these generated episode synopsis would make sense.

Currently the data has been collected by building a Scrapy spider to scrape the episode titles and synopsis, a Python script was written to clean the data. Challenges were faced when some of the episode synopsis contains text with hyperlinks, the Scrapy spider scrapes the hyperlink text seperately when it meets them and adds them to a list and the data cleaning script removes unwanted characters and builds the episode synopsis through string manipulation. This data was scraped from [here](https://en.wikipedia.org/wiki/List_of_Star_Wars:_The_Clone_Wars_episodes).

<h4 align=center> Star Wars The Clone Wars dataset </h4>

![](https://raw.githubusercontent.com/ohughes1207/Personal_Projects/main/Star%20Wars%20The%20Clone%20Wars%20Project/figs/dataset.PNG)
