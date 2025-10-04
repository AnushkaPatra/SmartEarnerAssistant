import main

# import pandas as pd
# import gradio as gr
# import numpy as np
# from transformers import pipeline #Install these libraries again on host computer
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error

# # Join rides_trips with earners (drivers)
# rides_with_earners = rides_trips.merge(
#     earners, left_on="driver_id", right_on="earner_id", how="inner"
# )

# # Join courier_trips with earners (couriers)
# couriers_with_earners = courier_trips.merge(
#     earners, left_on="courier_id", right_on="earner_id", how="inner"
# )



x_courier = main.courier_trips_data[['city_id', 'start_time', 'distance_km', 'duration_mins', 'basket_value_eur']]   # predictors
y_courier = main.courier_trips_data['net_earnings']   


X_train_courier, X_test_courier, Y_train_courier, Y_test_courier = main.train_test_split(
    x_courier, y_courier, test_size=0.3, random_state=42
)


def predict_net_earnings_courier():
    pass
    
def predict_net_earnings_rides():

    # Extract continuous features from start_time
    main.rides_trips_data["start_time"] = main.pd.to_datetime(main.rides_trips_data["start_time"])
    main.rides_trips_data["start_hour_cont"] = main.rides_trips_data["start_time"].dt.hour + main.rides_trips_data["start_time"].dt.minute / 60
    main.rides_trips_data["day_of_week"] = main.rides_trips_data["start_time"].dt.dayofweek  

    # Features and target
    X_rides = main.rides_trips_data[["city_id", "start_hour_cont", "day_of_week", "distance_km", "duration_mins", "surge_multiplier"]]
    y_rides = main.rides_trips_data["net_earnings"]

    # Train-test split
    X_train, X_test, y_train, y_test = main.train_test_split(
        X_rides, y_rides, test_size=0.2, random_state=42
    )

    # Train linear regression model
    model = main.LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)
    
    return model, X_test, y_test, y_pred