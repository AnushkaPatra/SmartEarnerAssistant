import main

def calculate_time_of_day_score():  # Nehir

    X = ['city_id', 'hour', 'surge_multiplier']
    y = ['score']

    train_df, test_df = main.train_test_split(main.time_of_day_score_data, test_size = 0.3, random_state = 42)

    X_train = train_df[X]
    X_test = test_df[X]
    
    y_train = train_df[y]

    linear_model = main.LinearRegression()
    linear_model.fit(X_train, y_train)

    y_pred = linear_model.predict(X_test)
    time_of_day_score = main.np.clip(main.np.round(y_pred), 1, 5)

    return time_of_day_score