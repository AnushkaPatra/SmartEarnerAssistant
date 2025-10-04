import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))

# Build path relative to the script location
csv_path = os.path.join(script_dir, "..", "resources", "cancellation_rates.csv")


cancellation_data = pd.read_csv(csv_path)

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

def calculate(city_id):
    cancellation_rates = np.array(cancellation_data["cancellation_rate_pct"])
    city_ids = np.array(cancellation_data["city_id"])

    prediction = calculate_cancellation_rate(city_id, cancellation_rates, city_ids)
    score = round(getScore(prediction, cancellation_rates), 2)

    return score
    
def score_for_userinput(city_id):
    return calculate(city_id)

# for i in range(6):
#     calculate(i, pd.read_csv(r"..\resources\cancellation_rates.csv"))
