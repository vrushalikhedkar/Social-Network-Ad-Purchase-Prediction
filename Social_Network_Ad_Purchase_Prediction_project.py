import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


dataset = pd.read_csv("Social_Network_Ads.csv")


dataset


dataset.shape


plt.scatter(dataset['Age'],dataset['EstimatedSalary'],c=dataset['Purchased'],cmap='rainbow')
plt.xlabel('Age')
plt.ylabel('Est.salary')
plt.show()


X = dataset[["Age", "EstimatedSalary"]]
y = dataset["Purchased"]


X


y


from sklearn.model_selection import train_test_split


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)


X_train.shape


X_test.shape


from sklearn.linear_model import LogisticRegression


model = LogisticRegression()


model.fit(X_train, y_train)


y_pred = model.predict(X_test)


y_pred


from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)


print (confusion_matrix(y_test,y_pred))


print(classification_report(y_test,y_pred))


model.predict([[35,70000]])


model.predict([[46,41000]])


from sklearn.neighbors import KNeighborsClassifier


knn = KNeighborsClassifier(n_neighbors=20)


knn.fit(X_train, y_train)


y_pred_knn = knn.predict(X_test)


accuracy_score(y_test, y_pred_knn)


from sklearn.tree import DecisionTreeClassifier


model_dt = DecisionTreeClassifier(random_state=20)


model_dt.fit(X_train, y_train)


y_pred_model_dt = dt.predict(X_test)


accuracy_score(y_test, y_pred_dt)


from sklearn.ensemble import RandomForestClassifier


model_rf = RandomForestClassifier(random_state=20)


model_rf.fit(X_train, y_train)


y_pred_model_rf = model_rf.predict(X_test)


accuracy_score(y_test, y_pred_model_rf)


print(confusion_matrix(y_test, y_pred_model_rf))


print(classification_report(y_test, y_pred_model_rf))


model_rf.predict([[46, 41000]])
