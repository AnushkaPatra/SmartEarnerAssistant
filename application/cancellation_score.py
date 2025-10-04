import main
import random
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt



def cancellation_score(cancellation_rate, file): # file data
    # file = pd.read_csv("cancellation_data")

    rates = file["cancellation_rate_pct"]

    rate_level = main.np.average[rates] / 5 # to determine the label of the rate between 1 and 5

    labels = main.np.where(rates <= rate_level, 5, rates)
    labels = main.np.where(rates <= rate_level*2, 4, rates)
    labels = main.np.where(rates <= rate_level*3, 3, rates)
    labels = main.np.where(rates <= rate_level*4, 2, rates)
    labels = main.np.where(rates > rate_level*4, 1, rates)

    X_train, Y_train, X_test, Y_test = main.train_test_split(rates, labels, test_size=0.3, random_state=random.random())
    linear_regression_model = main.LinearRegression()
    linear_regression_model.fit(X_train, Y_train)

    test_predictions = linear_regression_model.predict(X_test)
    
    mse = mean_squared_error(Y_test, test_predictions)
    print(f"Mean squared error: {mse:.4f}")
    
    prediction = linear_regression_model.predict(cancellation_rate)

    plt.scatter(X_train, Y_train, color="blue", label="Actual data")    # Original points
    plt.plot(X_train, test_predictions, color="red", label="Regression line")  # Regression line
    plt.xlabel("cancellation rates")
    plt.ylabel("label")
    plt.title("Linear Regression with scikit-learn")
    plt.legend()
    plt.show()
    return