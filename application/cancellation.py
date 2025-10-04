from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd

# def calculate_cancellation_score(cancellation_rate, file): # file data
#     cancellation_rates = np.array(file["cancellation_rate_pct"])

#     minimum_rate = np.min(cancellation_rates)
#     maximum_rate = np.max(cancellation_rates)
#     print(maximum_rate, minimum_rate)
#     labels = np.zeros(len(cancellation_rates))
#     for i in range(len(labels)):
#         labels[i] = mapToScore(cancellation_rates[i], maximum_rate, minimum_rate, 5, 1)

#     rate_level = np.average(cancellation_rates) / 5 # to determine the label of the rate between 1 and 5
    
#     print(len(cancellation_rates), len(labels))
#     X_train, X_test, y_train, y_test = train_test_split(cancellation_rates.reshape(-1,1), labels, test_size=0.3, random_state=42)
#     print(X_train.shape, y_train.shape)
#     linear_regression_model = LinearRegression()
#     linear_regression_model.fit(X_train, y_train)

#     test_predictions = linear_regression_model.predict(X_test)
    
#     mse = mean_squared_error(y_test, test_predictions)
#     print(f"Mean squared error: {mse:.4f}")
    
#     y_pred = linear_regression_model.predict(np.array(cancellation_rate).reshape(-1,1)) # X_test instead of cancellation_rate
#     cancellation_score = y_pred

#     if (cancellation_score < 1):
#         cancellation_score = 1
#     elif (cancellation_score > 5):
#         cancellation_score = 5

#     print(cancellation_score)

#     # main.plt.scatter(X_train, y_train, color="blue", label="Actual data")    # Original points
#     # main.plt.plot(X_train, test_predictions, color="red", label="Regression line")  # Regression line
#     # main.plt.xlabel("cancellation rates")
#     # main.plt.ylabel("label")
#     # main.plt.title("Linear Regression with scikit-learn")
#     # main.plt.legend()
#     # main.plt.show()
#     # cancellation_score
#     return 

def mapToScore(rate, max_rate, min_rate, upper_bound, lower_bound):
    score = -1

    if (max_rate == min_rate):
        score = (upper_bound + lower_bound) / 2
    else:
        score = (upper_bound + 1) - ((rate - min_rate) / (max_rate - min_rate) * (upper_bound - lower_bound) + lower_bound)
    
    return score

def getScore(cancellation_rate, datafile):
    cancellation_rates = np.array(datafile["cancellation_rate_pct"])
    minimum_rate = np.min(cancellation_rates)
    maximum_rate = np.max(cancellation_rates)

    # print(maximum_rate, minimum_rate)
    
    labels = np.zeros(len(cancellation_rates))
    for i in range(len(labels)):
        labels[i] = mapToScore(cancellation_rates[i], maximum_rate, minimum_rate, 5, 1)

    # print(maximum_rate, minimum_rate)

    X_train, X_test, y_train, y_test = train_test_split(cancellation_rates.reshape(-1,1), labels, test_size=0.3, random_state=42)
    # print(X_train.shape, y_train.shape)
    linear_regression_model = LinearRegression()
    linear_regression_model.fit(X_train, y_train)

    test_predictions = linear_regression_model.predict(X_test)
    
    mse = mean_squared_error(y_test, test_predictions)
    print(f"Mean squared error: {mse:.4f}")
    
    y_pred = linear_regression_model.predict(np.array(cancellation_rate).reshape(-1,1)) # X_test instead of cancellation_rate
    cancellation_score = y_pred

    if (cancellation_score < 1):
        cancellation_score = 1
    elif (cancellation_score > 5):
        cancellation_score = 5

    print("Predicted Cancellation Score:", cancellation_score)

    return cancellation_score

def calculate_cancellation_rate(city_id, datafile):
    cancellation_rates = np.array(datafile["cancellation_rate_pct"])
    city_ids = np.array(datafile["city_id"])
    
    # print(city_ids)

    X_train, X_test, y_train, y_test = train_test_split(city_ids.reshape(-1,1), cancellation_rates, test_size=0.3, random_state=42)
    # print(X_train.shape, y_train.shape)
    linear_regression_model = LinearRegression()
    linear_regression_model.fit(X_train, y_train)

    test_predictions = linear_regression_model.predict(X_test)
    
    mse = mean_squared_error(y_test, test_predictions)
    print(f"Mean squared error: {mse:.4f}")
    
    y_pred = linear_regression_model.predict(np.array(city_id).reshape(-1,1))
    print("Predicted Cancellation Rate:", y_pred)

    return y_pred

def calculate(city_id, datafile):
    prediction = calculate_cancellation_rate(city_id, datafile)
    getScore(prediction, datafile)
    return
    

file = pd.read_csv(r"..\resources\cancellation_rates.csv")
for i in range(6):
    calculate(i, file)
