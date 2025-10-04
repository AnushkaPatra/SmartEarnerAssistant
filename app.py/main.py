import pandas as pd
import gradio as gr
import numpy as np

from transformers import pipeline #Install these libraries again on host computer
from sklearn.linear_model import Linear
user_input = input()
generator = pipeline("text-generation", model = "gpt-neo-125M")
output = generator(user_input, max_length = 50)

earners_data = pd.read_csv("earners.csv")
cancellation_rates_data = pd.read_csv("cancellation_rates.csv")
courier_trips_data = pd.read_csv("courier_trips.csv")
jobs_like_data = pd.read_csv("jobs_like.csv")
rides_trips_data = pd.read_csv("rides_trips.csv")
surge_by_hour_data = pd.read_csv("surge_by_hour.csv")

#convert to numpy 
rides_trips_array = rides_trips_data.to_numpy()
earners_data_array = earners_data.to_numpy()
cancellation_rates_data_array = cancellation_rates_data.to_numpy()
courier_trips_data_array = courier_trips_data.to_numpy()
jobs_like_data_array = jobs_like_data.to_numpy()
surge_by_hour_data_array = surge_by_hour_data.to_numpy()

#tanisha and anushka 
def calculate_potential_net_earnings_score():
    
    return

def calculate_demand_likelihood_score():
    return

def calculate_weather_score():
    weather = data['weather']
    
    if weather == "clear":
        weather_idx = 0
    elif weather == "rain":
        weather_idx = 1
    else:
        weather_idx = 2  





def calculate_time_of_day_score():  # Nehir
    # surge_by_hour_multiplier = data['surge_multiplier'] # TODO: Change "data" to the appropriate variable name

    X = ['']
    y = ['']

    train_df, test_df = surge_by_hour_data_split(dataframe, test_size = 0.3, random state = 1)

    X_test = train_df[X]
    X_test = test_df[X]
    
    y_train = train_df[y]
    y_test = test_df[y]

    linear_regression_model = 

    y_pred = linear_regression_model.predict(X_test)


    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)

    time_of_day_score = y_pred, y_test

    return time_of_day_score
    


    

def calculate_city_score(destination_cancellation_rate, cancellation_rates):
    csv = pd.read_csv("cancellation_rates.csv")
    data = csv.drop(columns=["hexagon_id9"])
    csv["actual_rates"] = ccsv[""]
    average = np.average(cancellation_rates)
    level = average / 5
    
    if (destination_cancellation_rate <= level):
        return 5
    elif (destination_cancellation_rate <= level * 2):
        return 4
    elif (destination_cancellation_rate <= level * 3):
        return 3
    elif (destination_cancellation_rate <= level * 4):
        return 2
    else:
        return 

def calculate_location_score(): #Eda (Working on it)
    x_predictions = data['msg.predictions.predicted_eph']
    y_city = data['msg.city_id']

    
    
    return

def calculate_customer_rating_score(): 
    return

def calculate_driver_wellbeing_score():
    return



def calculate_overall_recommendation_score(): 
    recommendation_scores = [
        # TODO: Insert specific functions here
    ]

    return sum(recommendation_scores) / len(recommendation_scores)