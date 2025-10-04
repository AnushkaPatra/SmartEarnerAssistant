import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
# Add this line right here, after imports
np.set_printoptions(threshold=np.inf)


# Get the directory where THIS script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build path relative to the script location
csv_path = os.path.join(script_dir, "..", "resources", "courier_trips.csv")


rides_trips_data = pd.read_csv(csv_path)


def predict_net_earnings_courier():
    
    # Sample the data
    rides_sample = rides_trips_data.copy()

    # Extract continuous features from start_time
    rides_sample["start_time"] = pd.to_datetime(rides_sample["start_time"])
    rides_sample["start_hour_cont"] = rides_sample["start_time"].dt.hour + rides_sample["start_time"].dt.minute / 60
    rides_sample["day_of_week"] = rides_sample["start_time"].dt.dayofweek  

    # Features and target
    X_rides = rides_sample[["city_id", "distance_km", "duration_mins", "start_hour_cont", "day_of_week"]]
    y_rides = rides_sample["net_earnings"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_rides, y_rides, test_size=0.2, random_state=42
    )
    

    # Train linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)
    
    #print(f"13 - Predictions made - First 5: {y_pred}")
    
    # Convert continuous predictions to 1-5 scale
    # Using quantiles to split the predictions into 5 buckets
    bins = np.quantile(y_pred, [0, 0.2, 0.4, 0.6, 0.8, 1])
    y_pred_scaled = np.digitize(y_pred, bins, right=True)
    
    # Ensure values are within 1-5
    y_pred_scaled = np.clip(y_pred_scaled, 1, 5)
    print(y_pred_scaled)
    return model, X_test, y_test, y_pred, y_pred_scaled


predict_net_earnings_courier()

# import os
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split

# print("IMPORTED PANDAS")

# # Get the directory where THIS script is located
# script_dir = os.path.dirname(os.path.abspath(__file__))

# # Build path relative to the script location
# csv_path = os.path.join(script_dir, "..", "resources", "rides_trips.csv")

# rides_trips_data = pd.read_csv(csv_path)

# print("CSV LOADED")

# def predict_net_earnings_rides():
#     # Sample the data
#     rides_sample = rides_trips_data

#     # Extract continuous features from start_time
#     rides_sample["start_time"] = pd.to_datetime(rides_sample["start_time"])
#     rides_sample["start_hour_cont"] = rides_sample["start_time"].dt.hour + rides_sample["start_time"].dt.minute / 60
#     rides_sample["day_of_week"] = rides_sample["start_time"].dt.dayofweek  

#     # Features and target
#     X_rides = rides_sample[["city_id", "distance_km", "duration_mins", "surge_multiplier"]]
#     y_rides = rides_sample["net_earnings"]

#     # Train-test split
#     X_train, X_test, y_train, y_test = train_test_split(
#         X_rides, y_rides, test_size=0.2, random_state=42
#     )

#     # Train linear regression model
#     model = LinearRegression()
#     model.fit(X_train, y_train)

#     # Predictions
#     y_pred = model.predict(X_test)

#     print("Predictions:", y_pred)
    
#     return model, X_test, y_test, y_pred




