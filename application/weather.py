import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def decide_weather_scores(weather):
    if weather == "clear":
        return 5   # best chance
    elif weather == "rain":
        return 3   # moderate chance
    elif weather == "snow":
        return 1   # lowest chance
    else:
        return 2   

def read_weather_scores():
    weather_data = pd.read_csv(r"..\resources\weather_daily.csv")
    
    weather_scores = [decide_weather_scores(w) for w in weather_data["weather"]]
    weather_data["weather_idx"] = weather_scores

    print(weather_data[["date", "city_id", "weather", "weather_idx"]])
    return weather_data

def predict_weather_for_city_model():
    print("1 - Inside weather prediction function")

    # Load the dataset
    weather_data = pd.read_csv(r"..\resources\weather_daily.csv")
    print(f"2 - Data loaded - Shape: {weather_data.shape}")

    # Encode weather to numeric codes
    weather_data["weather_code"] = weather_data["weather"].map({
        "clear": 0,
        "rain": 1,
        "snow": 2
    }).fillna(2)

    print("3 - Weather encoded")

    # Features (X) and target (y)
    X_weather = weather_data[["city_id"]]   # only city_id for now
    y_weather = weather_data["weather_code"]

    print("4 - Features and target prepared")

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_weather, y_weather, test_size=0.3, random_state=42
    )
    print(f"5 - Train/test split done - Test size: {len(X_test)}")

    # Train logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    print("6 - Model trained")

    # Predictions
    y_pred = model.predict(X_test)
    print("7 - Predictions made")

    # Accuracy
    acc = accuracy_score(y_test, y_pred)
    print(f"8 - Model Accuracy: {acc:.2f}")

    # Map numeric codes back to labels
    weather_map = {0: "clear", 1: "rain", 2: "snow"}
    y_pred_labels = [weather_map[val] for val in y_pred]

    print("9 - Predictions (labels):", y_pred_labels[:10])

    return model, X_test, y_test, y_pred, y_pred_labels


print("10 - About to call weather function")
result = predict_weather_for_city_model()
print(result)
