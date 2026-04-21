from multipleRegression import calculate_regression_weights, predict_win_pct
from webscaper import scrapeStatsF1T1Y, scrapeTotal
import numpy as np
print("Scraping data from 1980 to 2024...")
features, targets = scrapeTotal(1980, 2024)
X_train = np.vstack(features)
Y_train = np.vstack(targets)

# Save X and Y into one file
# np.savez('nba_data_1980_2025.npz', features=X_train, targets=Y_train)
# print("Data saved to nba_data_1980_2025.npz")

weights = calculate_regression_weights(X_train, Y_train)

print(scrapeStatsF1T1Y(2026, 1))

prediction = predict_win_pct(scrapeStatsF1T1Y(2026, 1), weights)

print(f"Predicted Win %: {prediction}")