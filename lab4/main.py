import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from collections import Counter


def euclidean(first_point, second_point):
    return np.sqrt(np.sum((first_point - second_point) ** 2))


def knneighbors(k, x_train, x_test, y):
    y_pred = []

    for i in range(len(x_test)):
        distances = []
        for j in range(len(x_train)):
            dist = euclidean(np.array(x_train)[j, :], np.array(x_test)[i])
            distances.append(dist)

        distances = np.array(distances)

        k_distances = np.argsort(distances)[:k]

        values = y[k_distances]
        y_pred.append(Counter(values).most_common(1)[0][0])

    return y_pred


def knneighbors_scikit(k, X, y):
    # split dataset
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # scale dataset
    scaler = StandardScaler()
    scaler.fit(x_train)

    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)

    # define the model: init K-NN
    classifier = KNeighborsClassifier(n_neighbors=k)

    # fit model
    classifier.fit(x_train, y_train)

    # predict the test set results
    y_pred = classifier.predict(x_test)

    return x_train, x_test, y_test, y_test, y_pred


def data_classification(dataset):
    X = dataset.iloc[:, 1:3]
    y = dataset.iloc[:, 3]

    x_train = dataset.iloc[:(int)(0.7 * len(dataset)), 1:3]
    x_test = dataset.iloc[(int)(0.7 * len(dataset)):, 1:3]
    y_test = dataset.iloc[(int)(0.7 * len(dataset)):, 3]

    X_train, X_test, Y_test, Y_test, Y_pred = knneighbors_scikit(7, X, y)
    y_pred = knneighbors(7, x_train, x_test, y)

    # check base classification characteristics
    print('Statistics knneighbors method using scikit')
    print(classification_report(Y_test, Y_pred))

    print('Statistics knneighbors method using selfmade method')
    print(classification_report(y_test, y_pred))

    return x_test, X_test, y_pred, Y_pred


def visualization(x_test, X_test, points_color, points_color_scikit):
    f, ax = plt.subplots(2, 1, figsize=(8, 8))

    ax[0].scatter(x_test['Sweetness'][:], x_test['Crunch'][:], c=points_color)
    ax[0].set_title('Statistics knneighbors method using selfmade method')

    ax[1].scatter(X_test[:, 0], X_test[:, 1], c=points_color_scikit)
    ax[1].set_title('Statistics knneighbors method using scikit')

    plt.show()


# read dataset
dataset = pd.read_csv('data.csv')
x_test, X_test, y_pred, Y_pred = data_classification(dataset)

# define color for each category
points_color = [label.replace("Fruit", "orange", 1)
                .replace("Vegetable", "green", 1)
                .replace("Protein", "brown", 1) for label in y_pred]

points_color_scikit = [label.replace("Fruit", "orange", 1)
                       .replace("Vegetable", "green", 1)
                       .replace("Protein", "brown", 1) for label in Y_pred]

# build plots to visualize results of methods usage
visualization(x_test, X_test, points_color, points_color_scikit)

extended_dataset = pd.read_csv('extended_data.csv')
x_test, X_test, y_pred, Y_pred = data_classification(extended_dataset)

points_color = [label.replace("Fruit", "orange", 1)
                     .replace("Vegetable", "green", 1)
                     .replace("Protein", "brown", 1)
                     .replace("Berry", "red", 1) for label in y_pred]

points_color_scikit = [label.replace("Fruit", "orange", 1)
                            .replace("Vegetable", "green", 1)
                            .replace("Protein", "brown", 1)
                            .replace("Berry", "red", 1) for label in Y_pred]

visualization(x_test, X_test, points_color, points_color_scikit)