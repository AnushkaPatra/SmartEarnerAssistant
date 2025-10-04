from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd

def mapToScore(rate, max_rate, min_rate, upper_bound, lower_bound):
    score = -1

    if (max_rate == min_rate):
        score = (upper_bound + lower_bound) / 2
    else:
        score = (upper_bound + 1) - ((rate - min_rate) / (max_rate - min_rate) * (upper_bound - lower_bound) + lower_bound)
    
    return score

def getScore(cancellation_rate, cancellation_rates):
    minimum_rate = np.min(cancellation_rates)
    maximum_rate = np.max(cancellation_rates)

    cancellation_score = mapToScore(cancellation_rate, maximum_rate, minimum_rate, 5, 1)[0]
    print("Predicted Cancellation Score:", cancellation_score)
    return cancellation_score

def calculate_cancellation_rate(city_id, cancellation_rates, city_ids):
    
    X_train, X_test, y_train, y_test = train_test_split(city_ids.reshape(-1,1), cancellation_rates, test_size=0.3, random_state=42)
    linear_regression_model = LinearRegression()
    linear_regression_model.fit(X_train, y_train)

    test_predictions = linear_regression_model.predict(X_test)
    
    mse = mean_squared_error(y_test, test_predictions)
    print(f"Mean squared error: {mse:.4f}")
    
    y_pred = linear_regression_model.predict(np.array(city_id).reshape(-1,1))
    print("Predicted Cancellation Rate:", y_pred)

    return y_pred

def calculate(city_id, datafile):
    cancellation_rates = np.array(datafile["cancellation_rate_pct"])
    city_ids = np.array(datafile["city_id"])

    prediction = calculate_cancellation_rate(city_id, cancellation_rates, city_ids)
    score = getScore(prediction, cancellation_rates)
    return score
    

file = pd.read_csv(r"..\resources\cancellation_rates.csv")
for i in range(6):
    calculate(i, file)
