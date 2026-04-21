import numpy as np


numOfFeatures: 21


## Calculation weights using the normal equation for multiple linear regression
## X is the feature matrix (m x n) where m is the number of samples and n is the number of features
## y is the target vector (m x 1), in this case, is win count
def calculate_regression_weights(X, y):
    print(f"Calculating regression weights for X shape: {X.shape} and y shape: {y.shape}")
    # Add column to X for intercept term (bias)
    ones = np.ones((X.shape[0], 1))
    X_b = np.append(ones, X, axis=1)
    
    # Calculate the Normal Equation: w = inv(XT * X) * XT * y
    # np.linalg.pinv (pseudo-inverse) for better numerical stability 
    xt_x = X_b.T.dot(X_b)
    xt_x_inv = np.linalg.pinv(xt_x)
    weights = xt_x_inv.dot(X_b.T).dot(y)
    
    return weights


def predict_win_pct(X, weights):
    """
    X: A numpy array of team stats (m x 21)
    weights: The weight vector returned by calculate_regression_weights (22 x 1)
    """
    # 1. Add the column of ones for the intercept term 
    # This must match the shape adjustment you did during training
    ones = np.ones((X.shape[0], 1))
    X_b = np.append(ones, X, axis=1)
    
    # 2. Perform matrix multiplication (Dot Product)
    predictions = X_b.dot(weights)
    
    return predictions