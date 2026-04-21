Goals for this project:

Create a webscraping script to pull data from Basketball Reference and clean this data. Once cleaned, create custom ranking data for each team in their respective year, measured up against other teams, and append to each year/team's data. Combine into one singular csv file.

After all data cleaned, create a multiple regression formula, using matrix formula. Return which 3 features had largest weights, essentially which 3 stats are conducive to winning.


Write up:

After feeding the team data from 1979-1980 season till 2024-2025 season, the RMSE was off by about 7 games. Our total number of data points was around 1200-1300, and for 21 features. A table is in the github repo of my results, sorted by accuracy. Obviously, the accuracy isn't great and I'd mainly attribute it to a couple issues:

1. My stats didn't include defense rating and used primitive stats like steals and blocks, which are poor measures of real team defense
2. I didn't end up following through with ranking each team for the stats and instead just fed in raw numbers. This has a large effect on our predictions, because modern team playstyle and team playstyles pre-analytic revolution were very different, since the average team took minimal threes. 
3. I'm not knowledgeable enough about machine learning, but the algo was not very complex and I think that with a more sophisticated algorithm, we may have achieved better results. 

Overall though, I think this was a pretty cool learning experience.
