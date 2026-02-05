import pandas as pd 

df = pd.read_csv("dataset.csv") # reads the from the file

print("Dataset loaded successfully")
print(df.head()) # prints the first 5 rows
print(df.shape) #  (number of rows, number of columns)


feature_cols = ["mean" , "STD" , "RMS" , "ratio"]

X = df[feature_cols] # input features 
y = df["label"] # target label

print("X shape: ", X.shape)
print("y shape: ", y.shape)

print("\nfirst 5 rows of X:")
print(X.head())

print("\nfirst 10 values of y:")
print(y.head(10))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size = 0.2, random_state= 42, stratify = y)

print("Train shapes:", X_train.shape, y_train.shape)
print("Test shapes:", X_test.shape, y_test.shape)

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(
n_estimators = 500, 
random_state= 42,
class_weight="balanced",
max_depth=None,
min_samples_leaf=2
)
rf.fit(X_train, y_train) 
y_pred = rf.predict(X_test)

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
print("accuracy:", accuracy_score(y_test, y_pred))
print("confusion martix:",confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))