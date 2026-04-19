import numpy as np
from webscaper import scrapeStatsF1T1Y
from multipleRegression import predict_win_pct

# Wrap the values in np.array and add commas between the inner lists
weights = np.array([
    [-3.29424339e+00],
    [ 5.94228479e-05],
    [ 9.34236565e-02],
    [ 5.89106454e+00],
    [-6.26395472e-02],
    [-1.39516677e-01],
    [ 9.73923008e-03],
    [-1.24585247e-01],
    [-9.56772746e-02],
    [ 1.22134828e+00],
    [-4.18512223e-02],
    [-3.91609969e-03],
    [ 2.73431200e-01],
    [ 2.78954634e-01],
    [ 2.69917118e-01],
    [-2.33071989e-01],
    [ 4.63538704e-03],
    [ 5.39094106e-02],
    [ 1.78834420e-02],
    [-4.64277262e-02],
    [-1.62026719e-03],
    [ 4.80896924e-02]
])

# Now run the prediction
prediction = predict_win_pct(scrapeStatsF1T1Y(1982), weights)
print(f"Predicted Win %: {prediction}")