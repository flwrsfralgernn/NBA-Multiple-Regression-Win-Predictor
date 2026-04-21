Goals for this project:

Create a webscraping script to pull data from Basketball Reference and clean this data. Once cleaned, create custom ranking data for each team in their respective year, measured up against other teams, and append to each year/team's data. Combine into one singular csv file.

After all data cleaned, create a multiple regression formula, using matrix formula. Return which 3 features had largest weights, essentially which 3 stats are conducive to winning.


Write up:

After feeding the team data from 1979-1980 season till 2024-2025 season, the RMSE was off by about 7 games. Our total number of data points was around 1200-1300, and for 21 features. A table is attached below, sorted by accuracy. Obviously, the accuracy isn't great and I'd mainly attribute it to a couple issues:

1. My stats didn't include defense rating and used primitive stats like steals and blocks, which are poor measures of real team defense
2. I didn't end up following through with ranking each team for the stats and instead just fed in raw numbers. This has a large effect on our predictions, because modern team playstyle and team playstyles pre-analytic revolution were very different, since the average team took minimal threes. 
3. I'm not knowledgeable enough about machine learning, but the algo was not very complex and I think that with a more sophisticated algorithm, we may have achieved better results. 

Overall though, I think this was a pretty cool learning experience

NBA PREDICTION ANALYSIS (2026)
Sorted by Accuracy: Most Accurate to Least Accurate



Team                       Actual %  Pred %    Diff (Games Off)
---------------------------------------------------------------
Toronto Raptors            0.561     0.562     0.09
Cleveland Cavaliers        0.634     0.631     0.27
Golden State Warriors      0.451     0.446     0.40
Philadelphia 76ers         0.549     0.541     0.64
Minnesota Timberwolves     0.598     0.610     1.02
Los Angeles Lakers         0.646     0.627     1.59
Oklahoma City Thunder      0.780     0.808     2.33
Charlotte Hornets          0.537     0.508     2.35
Detroit Pistons            0.732     0.767     2.85
San Antonio Spurs          0.756     0.712     3.59
Boston Celtics             0.683     0.638     3.70
Milwaukee Bucks            0.390     0.437     3.87
Atlanta Hawks              0.561     0.612     4.15
Memphis Grizzlies          0.305     0.357     4.25
New York Knicks            0.646     0.700     4.44
Indiana Pacers             0.232     0.295     5.13
Miami Heat                 0.524     0.588     5.27
Dallas Mavericks           0.317     0.398     6.64
Chicago Bulls              0.378     0.462     6.89
Washington Wizards         0.207     0.292     6.93
Houston Rockets            0.634     0.720     7.05
Sacramento Kings           0.268     0.363     7.79
Orlando Magic              0.549     0.452     7.93
Phoenix Suns               0.549     0.448     8.27
Los Angeles Clippers       0.512     0.626     9.37
Denver Nuggets             0.659     0.778     9.77
Utah Jazz                  0.268     0.398     10.64
Brooklyn Nets              0.244     0.096     12.15
New Orleans Pelicans       0.317     0.489     14.11
Portland Trail Blazers     0.512     0.309     16.66
---------------------------------------------------------------
OVERALL PERFORMANCE STATS:
Average Error (MAE): 5.67 Games
Average Percent Error (MAPE): 17.91%
---------------------------------------------------------------
