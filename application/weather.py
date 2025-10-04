import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def decide_weather_scores(weather):
    """
    Maps weather conditions to numeric scores.
    
    Args:
        weather (str): Weather condition ('clear', 'rain', 'snow', or other)
    
    Returns:
        int: Score from 1-5, where 5 is best and 1 is worst
    """
    if weather == "clear":
        return 5   # best chance
    elif weather == "rain":
        return 3   # moderate chance
    elif weather == "snow":
        return 1   # lowest chance
    else:
        return 2   # unknown weather


def train_weather_model():
    """
    Trains a logistic regression model to predict weather based on city_id.
    
    Returns:
        tuple: (trained_model, accuracy_score)
    """
    print("Training weather prediction model...")
    
    # Load the dataset
    weather_data = pd.read_csv(r"..\resources\weather_daily.csv")
    print(f"Data loaded - Shape: {weather_data.shape}")
    
    # Encode weather to numeric codes
    weather_data["weather_code"] = weather_data["weather"].map({
        "clear": 0,
        "rain": 1,
        "snow": 2
    }).fillna(2)
    
    # Features (X) and target (y)
    X_weather = weather_data[["city_id"]]
    y_weather = weather_data["weather_code"]
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_weather, y_weather, test_size=0.3, random_state=42
    )
    
    # Train logistic regression model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Model trained successfully - Accuracy: {acc:.2f}")
    
    return model, acc


def predict_weather_score_for_city(city_id, model):
    """
    Predicts weather for a given city and returns the corresponding score.
    
    Args:
        city_id (int): The city identifier
        model: Trained logistic regression model
    
    Returns:
        tuple: (predicted_weather, weather_score)
    """
    # Weather code mapping
    weather_map = {0: "clear", 1: "rain", 2: "snow"}
    
    # Predict weather code for the city
    city_data = pd.DataFrame([[city_id]], columns=["city_id"])
    predicted_code = model.predict(city_data)[0]
    
    # Map code to weather label
    predicted_weather = weather_map[predicted_code]
    
    # Get the score for this weather
    weather_score = decide_weather_scores(predicted_weather)
    
    return predicted_weather, weather_score


# Main execution
if __name__ == "__main__":
    print("=" * 60)
    print("Weather Prediction and Scoring System")
    print("=" * 60)
    
    # Train the model
    model, accuracy = train_weather_model()
    
    print("\n" + "=" * 60)
    print("Testing predictions for different cities:")
    print("=" * 60)
    
    # Test predictions for various cities
    test_cities = [1, 2, 3, 4, 5]
    
    for city_id in test_cities:
        weather, score = predict_weather_score_for_city(city_id, model)
        print(f"City {city_id}: Predicted Weather = '{weather}', Score = {score}")
    
    print("\n" + "=" * 60)
    print("Example: Custom city prediction")
    print("=" * 60)
    
    # Example with a specific city
    custom_city = 10
    weather, score = predict_weather_score_for_city(custom_city, model)
    print(f"City {custom_city}: Weather = '{weather}', Score = {score}")