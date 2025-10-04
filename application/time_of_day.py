import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

# Load only 50 rows from CSV
csv_path = os.path.join(os.path.dirname(__file__), "..", "resources", "time_of_day_score_data.csv")
time_of_day_score_data = pd.read_csv(csv_path).sample(50, random_state=42)


def calculate_time_of_day_score():
    X = ['city_id', 'hour', 'surge_multiplier']
    y = ['score']

    train_df, test_df = train_test_split(time_of_day_score_data, test_size=0.3, random_state=42)

    X_train = train_df[X]
    X_test = test_df[X]
    y_train = train_df[y]

    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)

    y_pred = linear_model.predict(X_test)
    time_of_day_score = np.clip(np.round(y_pred), 1, 5)

    return time_of_day_score

print(csv_path)
print(os.path.exists(csv_path))

