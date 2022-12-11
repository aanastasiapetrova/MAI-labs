import pandas as pd
from matplotlib import pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from yellowbrick.classifier import ConfusionMatrix


def visualization(model, X_train_v, X_test_v, y_train_v, y_test_v, y_pred_v, title):
    f, ax = plt.subplots(2, 1)
    risk = len(list(filter(lambda x: x == 1, y_pred_v)))
    not_risk = len(list(filter(lambda x: x == 0,  y_pred_v)))
    ax[0].bar(['RISK', 'NOT RISK'], [risk, not_risk])
    ax[0].set_title(f'Amount of patients in risk group and not by {title}')

    age_left_bound = 0
    age_right_bound = 10
    in_risk = 0
    while age_right_bound <= 100:
        for i in range(len(y_pred_v)):
            if X_test_v[:, 5][i] in range(age_left_bound, age_right_bound) and y_pred_v[i] == 1:
                in_risk += 1
        age_left_bound += 10
        age_right_bound += 10
        age_risk_group.append(in_risk)

    ax[1].plot(age_categories, age_risk_group)
    ax[1].set_title(f'Patients distribution in risk group by age categories by {title}')
    plt.show()

    cm = ConfusionMatrix(model)
    cm.fit(X_train_v, y_train_v)
    cm.score(X_test_v, y_test_v)
    cm.show()

    age_risk_group.clear()


def knneighbors(X_train_k, X_test_k, y_train_k, y_test_k):
    knn_model = KNeighborsClassifier(n_neighbors=11)
    knn_model.fit(X_train_k, y_train_k)
    y_pred_k = knn_model.predict(X_test_k)

    accuracy_scores[0] = accuracy_score(y_test_k, y_pred_k)
    print(classification_report(y_test_k, y_pred_k, zero_division=0))

    visualization(knn_model, X_train_k, X_test_k, y_train_k, y_test_k, y_pred_k, 'knneighbors')


def decision_tree(X_train_d, X_test_d, y_train_d, y_test_d):
    Tree_model = DecisionTreeClassifier(max_depth=12)
    Tree_model.fit(X_train_d, y_train_d)
    y_pred_d = Tree_model.predict(X_test_d)

    accuracy_scores[1] = accuracy_score(y_test_d, y_pred_d)
    print(classification_report(y_test_d, y_pred_d, zero_division=0))

    visualization(Tree_model, X_train_d, X_test_d, y_train_d, y_test_d, y_pred_d, 'decision_tree')


def native_bayes(X_train_n, X_test_n, y_train_n, y_test_n):
    naive_bayes_model = GaussianNB()
    naive_bayes_model.fit(X_train_n, y_train_n)
    y_pred_n = naive_bayes_model.predict(X_test_n)

    accuracy_scores[2] = accuracy_score(y_test_n, y_pred_n)
    print(classification_report(y_test_n, y_pred_n, zero_division=0))

    visualization(naive_bayes_model, X_train_n, X_test_n, y_train_n, y_test_n, y_pred_n, 'native_bayes')


def linear_discr(X_train_l, X_test_l, y_train_l, y_test_l):
    linear_discr_model = LinearDiscriminantAnalysis()
    linear_discr_model.fit(X_train_l, y_train_l)
    y_pred_l = linear_discr_model.predict(X_test_l)

    accuracy_scores[3] = accuracy_score(y_test_l, y_pred_l)
    print(classification_report(y_test_l, y_pred_l, zero_division=0))

    visualization(linear_discr_model, X_train_l, X_test_l, y_train_l, y_test_l, y_pred_l, 'linear_discr')


data = pd.read_csv('CovidData.csv')

# 97, 99 - данные отсутствуют, 1 - true, 2 - false
data = data.loc[(data['CLASIFFICATION_FINAL'] < 4)]
data = data.loc[(data['SEX'] == 1) | (data['SEX'] == 2)]
data = data.loc[(data['USMER'] == 1) | (data['USMER'] == 2)]
data = data.loc[(data['PATIENT_TYPE'] == 1) | (data['PATIENT_TYPE'] == 2)]
data = data.loc[(data['PNEUMONIA'] == 1) | (data['PNEUMONIA'] == 2)]
data = data.loc[(data['DIABETES'] == 1) | (data['DIABETES'] == 2)]
data = data.loc[(data['COPD'] == 1) | (data['COPD'] == 2)]
data = data.loc[(data['ASTHMA'] == 1) | (data['ASTHMA'] == 2)]
data = data.loc[(data['INMSUPR'] == 1) | (data['INMSUPR'] == 2)]
data = data.loc[(data['HIPERTENSION'] == 1) | (data['HIPERTENSION'] == 2)]
data = data.loc[(data['OTHER_DISEASE'] == 1) | (data['OTHER_DISEASE'] == 2)]
data = data.loc[(data['CARDIOVASCULAR'] == 1) | (data['CARDIOVASCULAR'] == 2)]
data = data.loc[(data['OBESITY'] == 1) | (data['OBESITY'] == 2)]
data = data.loc[(data['RENAL_CHRONIC'] == 1) | (data['RENAL_CHRONIC'] == 2)]
data = data.loc[(data['TOBACCO'] == 1) | (data['TOBACCO'] == 2)]
data = data.loc[(data['ICU'] == 1) | (data['ICU'] == 2)]

# модифицируем данные, заменяем 2 на 0
data['SEX'] = data['SEX'].apply(lambda x: x if x == 1 else 0)
data['USMER'] = data['USMER'].apply(lambda x: x if x == 1 else 0)
data['PATIENT_TYPE'] = data['PATIENT_TYPE'].apply(lambda x: x if x == 1 else 0)
data['PNEUMONIA'] = data['PNEUMONIA'].apply(lambda x: x if x == 1 else 0)
data['DIABETES'] = data['DIABETES'].apply(lambda x: x if x == 1 else 0)
data['COPD'] = data['COPD'].apply(lambda x: x if x == 1 else 0)
data['ASTHMA'] = data['ASTHMA'].apply(lambda x: x if x == 1 else 0)
data['INMSUPR'] = data['INMSUPR'].apply(lambda x: x if x == 1 else 0)
data['HIPERTENSION'] = data['HIPERTENSION'].apply(lambda x: x if x == 1 else 0)
data['OTHER_DISEASE'] = data['OTHER_DISEASE'].apply(lambda x: x if x == 1 else 0)
data['CARDIOVASCULAR'] = data['CARDIOVASCULAR'].apply(lambda x: x if x == 1 else 0)
data['OBESITY'] = data['OBESITY'].apply(lambda x: x if x == 1 else 0)
data['RENAL_CHRONIC'] = data['RENAL_CHRONIC'].apply(lambda x: x if x == 1 else 0)
data['TOBACCO'] = data['TOBACCO'].apply(lambda x: x if x == 1 else 0)
data['DATE_DIED'] = data['DATE_DIED'].apply(lambda x: 0 if x == "9999-99-99" else 0)
data['PREGNANT'] = data['PREGNANT'].apply(lambda x: x if x == 1 else 0)
data['INTUBED'] = data['INTUBED'].apply(lambda x: x if x == 1 else 0)
data['ICU'] = data['ICU'].apply(lambda x: x if x == 1 else 0)

fig = plt.figure(figsize=(10,10))
ax = fig.gca()
data.hist(ax=ax)
plt.show()

# формирование столбца GROUP_RISK, базируясь на 4 признаках
data['RISK_GROUP'] = data['DATE_DIED'] + data['INTUBED'] + data['ICU'] + data['PNEUMONIA']
data['RISK_GROUP'] = data['RISK_GROUP'].apply(lambda x: 1 if x > 0 else 0)

# удаление лишних столбцов
data.drop(columns=['CLASIFFICATION_FINAL', 'MEDICAL_UNIT', 'PATIENT_TYPE', 'PREGNANT'],
          inplace=True)

# формрование набора данных
X = data.drop(columns='RISK_GROUP').values
y = data['RISK_GROUP'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
accuracy_scores = [0, 0, 0, 0]
age_risk_group = []
age_categories = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59',
                  '60-69', '70-79', '80-89', '90-99']

print('Knneighbours statistics:')
knneighbors(X_train, X_test, y_train, y_test)
print('DecisionTree statistics:')
decision_tree(X_train, X_test, y_train, y_test)
print('NativeBayes statistics:')
native_bayes(X_train, X_test, y_train, y_test)
print('LinearDiscriminantAnalysis statistics:')
linear_discr(X_train, X_test, y_train, y_test)

plt.bar(['knn', 'dtc', 'nb', 'lda'], accuracy_scores)
plt.title('Accuracy scores for all classification algorithms')
plt.show()



