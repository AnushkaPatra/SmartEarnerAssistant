import main

def calculate_location_score():
    x_city = main.heatmap_data['msg.city_id']
    y_predictions = main.heatmap_data['msg.predictions.predicted_eph']
    
    x_train, x_test, y_train, y_test = main.train_test_split(
    x_city, y_predictions, test_size=0.33, random_state=42)

    model = main.LinearRegression()
    model.fit(x_train,y_train)
    slope = model.coef_[0]

    predicted_heatmap = model.predict(x_test)

    return y_test, slope, predicted_heatmap