from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

def find_k(X_train, X_test, y_train, y_test):

    print("\nFinding the best value for k with the highest accuracy...\n")
    # now we try to find a k value with the highest accuracy
    best_k = 1
    best_test_accuracy = 0.0

    for k in range (1,16,2):
            knn = KNeighborsClassifier(n_neighbors=k)
            knn.fit(X_train, y_train)

            # here we make predictions
            test_predictions = knn.predict(X_test)

            # now we check for accuracy
            test_accuracy = accuracy_score(y_test, test_predictions)

            if test_accuracy > best_test_accuracy:
                best_test_accuracy = test_accuracy
                best_k = k

    print(f"\nBest value for k found: k = {best_k}\n")
    return best_k


def run_model(X_train, X_test, y_train, y_test):

    optimal_k = find_k(X_train, X_test, y_train, y_test)

    # final model
    print("\nRunning model using the optimal value for k\n")
    knn = KNeighborsClassifier(n_neighbors=optimal_k)
    knn.fit(X_train, y_train)

    # model training is done

    test_predictions = knn.predict(X_test)
    accuracy = accuracy_score(y_test, test_predictions)

    print("\nFinal results: ")
    print(f"Best value for k = {optimal_k}")
    print(f"Accuracy = {accuracy*100:.2f}%\n")
    print(classification_report(y_test, test_predictions))

    # example (first seven samples from testing set)
    x_sample = X_test[:7]
    y_sample = list(y_test.head(7))
    predictions = list(knn.predict(x_sample))

    print("\nHere we can take a look if our model predicted correctly:\n")
    print(f"true labels:        {y_sample}")
    print(f"knn predictions:    {predictions}")





