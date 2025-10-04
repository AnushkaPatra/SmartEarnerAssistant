import main

def calculate_cancellation_score(cancellation_rate, file): # file data
    cancellation_rates = main.np.array(file["cancellation_rate_pct"])
    # print(file.columns)

    minimum_rate = main.np.min(cancellation_rates)
    maximum_rate = main.np.max(cancellation_rates)
    print(maximum_rate, minimum_rate)
    labels = main.np.zeros(len(cancellation_rates))
    for i in range(len(labels)):
        labels[i] = mapToScore(cancellation_rates[i], maximum_rate, minimum_rate, 5, 1)

    rate_level = main.np.average(cancellation_rates) / 5 # to determine the label of the rate between 1 and 5
    
    print(len(cancellation_rates), len(labels))
    X_train, X_test, y_train, y_test = main.train_test_split(cancellation_rates.reshape(-1,1), labels, test_size=0.3, random_state=42)
    print(X_train.shape, y_train.shape)
    linear_regression_model = main.LinearRegression()
    linear_regression_model.fit(X_train, y_train)

    test_predictions = linear_regression_model.predict(X_test)
    
    mse = main.mean_squared_error(y_test, test_predictions)
    print(f"Mean squared error: {mse:.4f}")
    
    y_pred = linear_regression_model.predict(main.np.array(cancellation_rate).reshape(-1,1)) # X_test instead of cancellation_rate
    cancellation_score = y_pred

    if (cancellation_score < 1):
        cancellation_score = 1
    elif (cancellation_score > 5):
        cancellation_score = 5


    print(cancellation_score)

    # main.plt.scatter(X_train, y_train, color="blue", label="Actual data")    # Original points
    # main.plt.plot(X_train, test_predictions, color="red", label="Regression line")  # Regression line
    # main.plt.xlabel("cancellation rates")
    # main.plt.ylabel("label")
    # main.plt.title("Linear Regression with scikit-learn")
    # main.plt.legend()
    # main.plt.show()
    # cancellation_score
    return 

def mapToScore(rate, max_rate, min_rate, upper_bound, lower_bound):
    score = -1

    if (max_rate == min_rate):
        score = (upper_bound + lower_bound) / 2
    else:
        score = (upper_bound + 1) - ((rate - min_rate) / (max_rate - min_rate) * (upper_bound - lower_bound) + lower_bound)
    
    return score


file = main.pd.read_csv(r"..\resources\cancellation_rates.csv")
calculate_cancellation_score(1, file)
