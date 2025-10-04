import pandas as pd
import gradio as gr
import numpy as np
from transformers import pipeline #Install these libraries again on host computer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import random
from sklearn.metrics import mean_squared_error


def calculate_city_score():
    csv = pd.read_csv("cancellation_rates.csv")
    csv["actual_rates"] = csv["job_count"] * csv["cancellation_rate_pct"]
    # csv["hexagon_to_int"] = csv["hexagon_id9"].apply(lambda x: int(x, 16))
    # locations = csv["hexagon_to_int"]
    # rates = csv["actual_rates"]

    average = np.average[csv["cancellation_rate_pct"]]

    cities = csv["city_id"]
    mean_ratings = csv.groupby("city_id")["cancellation_rate_pct"].mean()
    

    X_train, Y_train, X_test, Y_test = train_test_split(locations, rates, test_size=0.3, random_state=random.random())
    linear_regression_model = LinearRegression()
    linear_regression_model.fit(X_train, Y_train)

    predictions = linear_regression_model.predict(X_test)
    
    mse = mean_squared_error(Y_test, predictions)
    print(f"Mean squared error: {mse:.4f}")

    # average = np.average(cancellation_rates)
    # level = average / 5
    
    # if (destination_cancellation_rate <= level):
    #     return 5
    # elif (destination_cancellation_rate <= level * 2):
    #     return 4
    # elif (destination_cancellation_rate <= level * 3):
    #     return 3
    # elif (destination_cancellation_rate <= level * 4):
    #     return 2
    # else:
    return 