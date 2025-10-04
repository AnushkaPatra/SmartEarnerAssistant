import main 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# # Join rides_trips with earners (drivers)
# rides_with_earners = rides_trips.merge(
#     earners, left_on="driver_id", right_on="earner_id", how="inner"
# )

# # Join courier_trips with earners (couriers)
# couriers_with_earners = courier_trips.merge(
#     earners, left_on="courier_id", right_on="earner_id", how="inner"
# )

x_courier = courier_trips_data[['city_id', 'start_time', 'distance_km', 'duration_mins', 'basket_value_eur']]   # predictors
y_courier = courier_trips_data['net_earnings']   


X_train_courier, X_test_courier, Y_train_courier, Y_test_courier = train_test_split(
    x_courier, y_courier, test_size=0.3, random_state=42
)

def predict_net_earnings_courier():
    
def predict_net_earnings_rides():
    rides_trips_data["start_time"] = pd.to_datetime(rides_trips_data["start_time"])
    
    # Extract continuous features from start_time
    rides_trips_data["start_hour_cont"] = rides_trips_data["start_time"].dt.hour + rides_trips_data["start_time"].dt.minute / 60
    rides_trips_data["day_of_week"] = rides_trips_data["start_time"].dt.dayofweek  

    # Features and target
    X_rides = rides_trips_data[["city_id", "start_hour_cont", "day_of_week", "distance_km", "duration_mins", "surge_multiplier"]]
    y_rides = rides_trips_data["net_earnings"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_rides, y_rides, test_size=0.2, random_state=42
    )

    # Train linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Metrics
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print("Rides Model Performance:")
    print(f"  RMSE: {rmse:.2f}")
    print(f"  R² Score: {r2:.2f}")

return model, X_test, y_test, y_pred