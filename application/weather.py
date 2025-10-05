import os 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#train
def train_weather_model():

    # Get the directory where THIS script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Build path relative to the script location
    csv_path = os.path.join(script_dir, "..", "resources", "weather_daily.csv")

    weather_data = pd.read_csv(csv_path)
    

    # Encode weather to numeric codes
    weather_data["weather_code"] = weather_data["weather"].map({
        "clear": 0,
        "rain": 1,
        "snow": 2
    }).fillna(2)

    # Features and target
    X = weather_data[["city_id"]]  # keep as DataFrame
    y = weather_data["weather_code"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Train logistic regression
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Optional: check accuracy
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Weather model trained. Accuracy: {acc:.2f}")

    return model

def decide_weather_score(weather_label):
    if weather_label == "clear":
        return 5
    elif weather_label == "rain":
        return 3
    elif weather_label == "snow":
        return 1
    else:
        return 2

def get_city_weather_score(model, city_id):
    # Create DataFrame with same column name used for training
    city_df = pd.DataFrame({"city_id": [city_id]})

    # Predict numeric code
    weather_code = model.predict(city_df)[0]

    # Map code back to label
    weather_map = {0: "clear", 1: "rain", 2: "snow"}
    weather_label = weather_map.get(weather_code, "unknown")

    # Convert to score
    score = decide_weather_score(weather_label)
    return score

#example
if __name__ == "__main__":
    # Train the model once
    model = train_weather_model()

    # Get score for city_id = 1
    score = get_city_weather_score(model, 1)
    print(f"City 1 weather score: {score}")

    # You can call it multiple times for different cities
    score2 = get_city_weather_score(model, 4)
    print(f"City 2 weather score: {score2}")
