from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix
import pandas as pd

iris = load_iris()
df = pd.DataFrame(data=iris.data,columns=iris.feature_names)
df['target'] = iris.target
print(df)
X = iris.data
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, y_prediction)
print("------")
print(accuracy)
print("------")
print(confusion_matrix(y_prediction,y_test))
print(classification_report(y_test, y_prediction, target_names=iris.target_names))
