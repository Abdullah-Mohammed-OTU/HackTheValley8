import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt



def main(): 
    #Read CSV File
    data = pd.read_csv('toronto_average_temperatures_final.csv')

    #Getting the x and y values
    X = data['Year'].values.reshape(-1, 1)
    y = data['Average_Temperature'].values  

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    return model

main()