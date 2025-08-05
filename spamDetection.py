import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.feature_extraction.text import CountVectorizer

url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"

df = pd.read_csv(url, sep='\t',header=None,names=['label',"message"])

print(df)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["message"])
Y = df["labelnum"] = df.label.map({"spam":1,"ham":0})
# = df.label.map({"ham":0,"spam":1})

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


model = RandomForestClassifier()
model.fit(X_train, y_train)

y_prediction = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_prediction))
print("Classification Report:\n", classification_report(y_test, y_prediction))
print("----------")
new_messages = ["You won a $1000 Walmart gift card. Click here to claim it!","Hey, are we still meeting for lunch today?"]

hadi = vectorizer.transform(new_messages)
wahada = model.predict(hadi)
print(wahada)

for had,label in zip(new_messages,wahada):
    print(f" Message : '{had}' ---> {'spam' if label == 1 else 'ham'}")