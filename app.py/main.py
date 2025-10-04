import pandas as pd
import gradio as gr
import numpy as np
from transformers import pipeline #Install these libraries again on host computer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

user_input = input()
generator = pipeline("text-generation", model = "gpt-neo-125M")
output = generator(user_input, max_length = 50)

earners_data = pd.read_csv("earners.csv")
cancellation_rates_data = pd.read_csv("cancellation_rates.csv")
courier_trips_data = pd.read_csv("courier_trips.csv")
jobs_like_data = pd.read_csv("jobs_like.csv")
rides_trips_data = pd.read_csv("rides_trips.csv")
surge_by_hour_data = pd.read_csv("surge_by_hour.csv")
heat_data = pd.read_csv("heat_data.csv")
weather_data = pd.read_csv("weather_daily.csv")

#convert to numpy 
rides_trips_array = rides_trips_data.to_numpy()
earners_data_array = earners_data.to_numpy()
cancellation_rates_data_array = cancellation_rates_data.to_numpy()
courier_trips_data_array = courier_trips_data.to_numpy()
jobs_like_data_array = jobs_like_data.to_numpy()
surge_by_hour_data_array = surge_by_hour_data.to_numpy()
heat_data_array = heat_data.to_numpy()

def calculate_customer_rating_score(): 
    return

def calculate_overall_recommendation_score(): 
    recommendation_scores = [
        # TODO: Insert specific functions here
    ]

    return sum(recommendation_scores) / len(recommendation_scores)