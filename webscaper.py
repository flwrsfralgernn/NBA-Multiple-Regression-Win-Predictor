from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np
import time



def scrapeTotal(yearBeg, yearEnd):

    all_features = [] 
    all_targets = []

    while yearBeg <= yearEnd:
        urlStats = f"https://www.basketball-reference.com/leagues/NBA_{yearBeg}.html"
        urlStandings = f"https://www.basketball-reference.com/leagues/NBA_{yearBeg}_standings.html"
        headers = {'User-Agent': 'Mozilla/5.0'}



        X = scrapeStatsByYear(urlStats, headers);
        time.sleep(3.1)
        Y = scrapeStandingsByYear(urlStandings, headers);
        time.sleep(3.1)
        all_features.append(X)
        all_targets.append(Y)

        yearBeg += 1
    return all_features, all_targets

def scrapeStatsByYear(url, headers):
    response = requests.get(url, headers=headers)

    if response.status_code == 429:
        print("Error: You are being rate limited. Wait ~1 hour.")
        return np.array([])

    tables = pd.read_html(response.text, attrs={'id': 'per_game-team'})
    df = tables[0]

    # 2. Clean and Sort
    df = df[df['Team'] != 'League Average']
    df = df.sort_values(by='Team')

    # 3. Drop unwanted columns (ID, Name, Games, Minutes)
    df = df.drop(columns=['Rk', 'Team', 'G', 'MP'])

    # 4. Convert to NumPy Array
    # This creates a matrix of shape (30, 21) roughly
    stats_matrix = df.to_numpy()

    return stats_matrix

def scrapeStatsF1T1Y(year):
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}.html"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)

    if response.status_code == 429:
        print("Error: You are being rate limited. Wait ~1 hour.")
        return np.array([])

    tables = pd.read_html(response.text, attrs={'id': 'per_game-team'})
    df = tables[0]

    # 1. Clean and Sort
    df = df[df['Team'] != 'League Average']
    df = df.sort_values(by='Team')

    # 2. Drop unwanted columns
    df = df.drop(columns=['Rk', 'Team', 'G', 'MP'])

    # 3. SELECT ONLY THE FIRST ENTRY
    # Using [[0]] keeps it as a DataFrame with one row, 
    # which maintains the 2D shape (1, 21) when converted to numpy.
    df = df.iloc[[0]] 

    # 4. Convert to NumPy Array
    stats_matrix = df.to_numpy()

    return np.vstack(stats_matrix)

def scrapeStandingsByYear(url, headers):
    response = requests.get(url, headers=headers)

    # Scrape standings and combine into one DataFrame for both conferences
    tables = pd.read_html(response.text)
    east = tables[0].rename(columns={tables[0].columns[0]: 'Team'})
    west = tables[1].rename(columns={tables[1].columns[0]: 'Team'})
    df = pd.concat([east, west])

    # Filter data and sort by team name
    df = df[~df['Team'].str.contains('Division')].sort_values(by='Team')

    # Calculate win percentage for each team
    df['W'] = df['W'].astype(int)
    df['L'] = df['L'].astype(int)
    df['Win_Pct'] = df['W'] / (df['W'] + df['L'])

    # Convert into numpy array
    win_pct_matrix = df['Win_Pct'].values.reshape(-1, 1)

    return win_pct_matrix