<h1 align="center">Welcome to Video Game Market Analysis 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/Epstei46/specialization-capstone-project#readme" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://github.com/Epstei46/specialization-capstone-project/graphs/commit-activity" target="_blank">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-no%3F-yellow.svg" />
  </a>
  <a href="https://github.com/Epstei46/specialization-capstone-project/blob/main/LICENSE.md" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green.svg" />
    <!-- <img alt="License:MIT" src="https://img.shields.io/github/license/Epstei46/specialization-capstone-project" /> -->
  </a>
</p>

# Video Game Market Analysis

This is a project I started to get a better understanding of the amount of games and/or total sales, per recent system, for each genre. After exploring and cleaning this data, I will do some analysis and make use of Python modules to create bar charts which I will display in this repo.

## About the Data

The data set used in this project was created early January 2022 and downloaded as a .csv file from [data.world](https://data.world/sumitrock/video/), which scraped the data from [VGChartz](https://www.vgchartz.com/gamedb/). I have created a [Data Dictionary](#data-dictionary) below, providing info on each column in the data set. And if you would like to know more about [VGChartz Data Collection Methodology](https://www.vgchartz.com/methodology.php), they have a short post about it.
> Main point from their methodology page is that they stopped tracking sales data in 2018 but still have the legacy data available for those who are interested in browsing it. There is only 3 games from 2017 and 1 game from 2020 in the data set, so I will be focusing on data from 2016 and earlier.

If you would like to learn more about how the data was scraped or try it yourself, you may be able to gain some insight by viewing [this GitHub repository](https://github.com/ashaheedq/vgchartzScrape). However, data scraping was outside of the scope of this project, so the data set from data.world was used for this analysis.
> The creator of this GitHub repo is unrelated to the creator of the dataset on data.world, but there are 61 forks linked to this GitHub repo. It is possible that the data set came from one of those forks.

VGChartz also has additional data on [total platform sales](https://www.vgchartz.com/analysis/platform_totals/). This was not included in the data set but is worth taking note of.

## Data Dictionary

The data dictionary included in the data set only showed data types; the descriptions I added after exploring the dataset and source website (VGChartz).

| Column | Data Type | Description |
|--------|:---------:|-------------|
| name | string | name of the game |
| platform | string | platform  the game was released on (i.e. PS4, XOne, etc.) |
| year_of_release | integer | year the game was released |
| genre | string | genre of the game |
| publisher | string | publisher of the game |
| na_sales | decimal | sales in North America (in millions) |
| eu_sales | decimal | sales in Europe (in millions) |
| jp_sales | decimal | sales in Japan (in millions) |
| other_sales | decimal | sales in the rest of the world (in millions) |
| global_sales | decimal | sales throughout the world (in millions) |
| critic_score | integer | average critic score, out of 100 |
| critic_count | integer | total number of critics who provided a score |
| user_score | string[^1] | average user score from VGChartz, out of 10 |
| user_count | integer | total number of users who provided a score |
| developer | string | developer of the game |
| rating | string | rating of the game (i.e. E, E10+, T, M, etc.) |

[^1]: user_score values are decimals, 'tbd', or empty. If 'tbd' is converted to empty/NaN, then the data type could be decimal. If multiplied by 10, then the data type could be integer and comparable to critic_score.

## MVP

* As a user, I should be able to select a genre and see which system had the largest number of games.
* As a user, I should be able to select a genre and see which system had the highest sales.

<!-- ## Additional Features -->

<!-- * Along with the title of show/movie, added an input field to the form for an optional comment.
* Changed pixel width/height to view width/height to look better on mobile.
* Made the title of this project a header that stays at the top of the browser while scrolling.
* Created a sidebar image for some extra flair. -->

<!-- ## Challenge
I wanted to be able to go from local testing to Heroku deployment without needing to modify the code every time I went from one to the other. My original solution I came up with after doing some research was to set the baseURL object in the client folder equal to window.location.origin instead of having the URL in my code. I later changed that to use window.location.origin to see if it includes Heroku, and depending on the truthiness of that function, use the production or development URL. -->

<!-- ### 🏠 [Homepage](https://github.com/Epstei46/foundations-capstone-project#readme) -->
<!-- ### ✨ [Demo](https://drive.google.com/file/d/1iO7s3PV4oqWdbjrgjKnLjg7WsC1JBi03/view) -->

<!-- ![Deployed Screenshot](watch-list-ss.png?raw=true "Deployed Screenshot") -->

<!-- ## Install & Setup

```sh
npm install
```
* In the root folder, create a .env file, type in SERVER_PORT=4242 to match with client/main.js line 6 -->

<!-- ## Usage

```sh
npm run start
``` -->

## Author

👤 **Steven Epstein**

* Portfolio Page: https://Epstei46.github.io (under construction)
* Github: [@Epstei46](https://github.com/Epstei46)
<!-- * LinkedIn: [@TBA](https://linkedin.com/in/TBA) -->

<!-- ## Show your support -->

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2022 [Steven Epstein](https://github.com/Epstei46).<br />
This project is [MIT](https://github.com/Epstei46/specialization-capstone-project/blob/main/LICENSE.md) licensed.