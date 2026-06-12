import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def get_prepared_data(df):

    print("\nProcessing data...\n")
    # we separate the class column from the rest of the features
    X = df.drop(columns=['Class'])
    y = df['Class']

    # we split the data to be 80% training and 20% testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)

    # now we scale the data
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test