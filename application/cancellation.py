import main

def calculate_cancellation_score(cancellation_rate, file): # file data
    file = main.pd.read_csv("file")

    rates = file["cancellation_rate_pct"]

    rate_level = main.np.average[rates] / 5 # to determine the label of the rate between 1 and 5
    
    labels = main.np.where(rates <= rate_level, 5, rates)
    labels = main.np.where(rates <= rate_level*2, 4, rates)
    labels = main.np.where(rates <= rate_level*3, 3, rates)
    labels = main.np.where(rates <= rate_level*4, 2, rates)
    labels = main.np.where(rates > rate_level*4, 1, rates)

    X_train, y_train, X_test, y_test = main.train_test_split(rates, labels, test_size=0.3, random_state=42)
    linear_regression_model = main.LinearRegression()
    linear_regression_model.fit(X_train, y_train)

    test_predictions = linear_regression_model.predict(X_test)
    
    mse = main.mean_squared_error(y_test, test_predictions)
    print(f"Mean squared error: {mse:.4f}")
    
    y_pred = linear_regression_model.predict(cancellation_rate) # X_test instead of cancellation_rate
    cancellation_score = y_pred

    print(cancellation_score)

    # main.plt.scatter(X_train, y_train, color="blue", label="Actual data")    # Original points
    # main.plt.plot(X_train, test_predictions, color="red", label="Regression line")  # Regression line
    # main.plt.xlabel("cancellation rates")
    # main.plt.ylabel("label")
    # main.plt.title("Linear Regression with scikit-learn")
    # main.plt.legend()
    # main.plt.show()

    return cancellation_score