import data_setup
import data_visualization
import data_processing
import model

def main():

    # install libraries and download dataset
    df = data_setup.setup_and_load()

    # visualize data
    data_visualization.visualize_data(df)

    # process the data and split into training/testing
    X_train, X_test, y_train, y_test = data_processing.get_prepared_data(df)

    # run the model
    model.run_model(X_train, X_test, y_train, y_test)

if __name__ == "__main__":
    main()