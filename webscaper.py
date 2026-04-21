from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np
import time
from io import StringIO  # Added this import

def scrapeTotal(yearBeg, yearEnd):
    all_features = [] 
    all_targets = []

    while yearBeg <= yearEnd:
        print(f"Scraping data for year: {yearBeg}")
        urlStats = f"https://www.basketball-reference.com/leagues/NBA_{yearBeg}.html"
        urlStandings = f"https://www.basketball-reference.com/leagues/NBA_{yearBeg}_standings.html"
        headers = {'User-Agent': 'Mozilla/5.0'}

        X = scrapeStatsByYear(urlStats, headers)
        time.sleep(3.1)
        Y = scrapeStandingsByYear(urlStandings, headers)
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

    # Wrapped response.text in StringIO()
    tables = pd.read_html(StringIO(response.text), attrs={'id': 'per_game-team'})
    df = tables[0]

    df = df[df['Team'] != 'League Average']
    df = df.sort_values(by='Team')
    df = df.drop(columns=['Rk', 'Team', 'G', 'MP'])
    stats_matrix = df.to_numpy()

    return stats_matrix

def scrapeStatsF1T1Y(year, team_idx):
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}.html"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)

    if response.status_code == 429:
        print("Error: You are being rate limited. Wait ~1 hour.")
        return np.array([])

    # Wrapped response.text in StringIO()
    tables = pd.read_html(StringIO(response.text), attrs={'id': 'per_game-team'})
    df = tables[0]

    # 1. Clean and Sort
    df = df[df['Team'] != 'League Average']
    df = df.sort_values(by='Team').reset_index(drop=True)

    # 2. Safety check for the index
    if team_idx < 0 or team_idx >= len(df):
        print(f"Error: Index {team_idx} is out of range. Please use 0 to {len(df)-1}.")
        return np.array([])

    # 3. Extract the Team Name for printing
    team_name = df.iloc[team_idx]['Team']
    print(f"Fetching stats for: {team_name} ({year})")
    time.sleep(3.1)
    print(scrapeWinPctF1T1Y(year, team_idx))  # Print the win percentage for this team and year

    # 4. Filter to the specific team and drop non-stat columns
    # We select the row first, then drop, so the name is still available for the print above
    df_selected = df.iloc[[team_idx]].copy()
    df_selected = df_selected.drop(columns=['Rk', 'Team', 'G', 'MP'])
    
    stats_matrix = df_selected.to_numpy()

    return np.vstack(stats_matrix)

def scrapeWinPctF1T1Y(year, team_idx):
    # 1. Setup URL and Headers
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}_standings.html"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)

    if response.status_code == 429:
        print("Error: You are being rate limited. Wait ~1 hour.")
        return np.array([])

    # 2. Extract Tables (0 is East, 1 is West)
    tables = pd.read_html(StringIO(response.text))
    east = tables[0].rename(columns={tables[0].columns[0]: 'Team'})
    west = tables[1].rename(columns={tables[1].columns[0]: 'Team'})
    
    # Combine and Clean
    df = pd.concat([east, west])
    
    # Filter out "Division" headers and clean team names (remove playoff asterisks)
    df = df[~df['Team'].str.contains('Division')].copy()
    df['Team'] = df['Team'].str.replace('*', '', regex=False)
    
    # 3. Sort by Team to align with index 0-29
    df = df.sort_values(by='Team').reset_index(drop=True)

    # 4. Safety check for the index
    if team_idx < 0 or team_idx >= len(df):
        print(f"Error: Index {team_idx} is out of range. Use 0-{len(df)-1}.")
        return np.array([])

    # 5. Calculation Logic (from your provided method)
    df['W'] = df['W'].astype(int)
    df['L'] = df['L'].astype(int)
    df['Win_Pct'] = df['W'] / (df['W'] + df['L'])

    # 6. Extract and Print
    team_name = df.iloc[team_idx]['Team']
    win_pct_val = df.iloc[team_idx]['Win_Pct']
    
    print(f"Team: {team_name} | Win Percentage: {win_pct_val:.3f}")

    # 7. Return as a matrix (1x1 or array) to match scrapeStatsF1T1Y style
    # Returning a 2D array [ [win_pct] ]
    return np.array([[win_pct_val]])

def scrapeStandingsByYear(url, headers):
    response = requests.get(url, headers=headers)

    # Wrapped response.text in StringIO()
    tables = pd.read_html(StringIO(response.text))
    east = tables[0].rename(columns={tables[0].columns[0]: 'Team'})
    west = tables[1].rename(columns={tables[1].columns[0]: 'Team'})
    df = pd.concat([east, west])

    df = df[~df['Team'].str.contains('Division')].sort_values(by='Team')

    df['W'] = df['W'].astype(int)
    df['L'] = df['L'].astype(int)
    df['Win_Pct'] = df['W'] / (df['W'] + df['L'])

    win_pct_matrix = df['Win_Pct'].values.reshape(-1, 1)

    return win_pct_matrix