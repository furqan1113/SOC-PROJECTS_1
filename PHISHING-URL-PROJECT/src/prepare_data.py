import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score



# Load our processed dataset
df = pd.read_csv("../datasets/processed_features.csv")

# X = the 10 features used by the model
X = df.drop("label", axis=1)

# y = the correct answer (0 = phishing, 1 = legitimate)
y = df["label"]

print("X shape:", X.shape)
print("y shape:", y.shape)


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("Training features:", X_train.shape)
print("Testing features:", X_test.shape)
print("Training labels:", y_train.shape)
print("Testing labels:", y_test.shape)



model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Model training completed")


# Test the model on data it has not seen before
y_pred = model.predict(X_test)

print("Testing completed")




print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:")
print(cm)


import joblib

# Save the trained model
joblib.dump(model, "../model.pkl")

print("Model saved")

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

print("\nComparing models...")

# Logistic Regression
logistic_model = LogisticRegression(max_iter=1000)
logistic_model.fit(X_train, y_train)

logistic_prediction = logistic_model.predict(X_test)

print("Logistic Regression Accuracy:",
      accuracy_score(y_test, logistic_prediction))


# Decision Tree
tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)

tree_prediction = tree_model.predict(X_test)

print("Decision Tree Accuracy:",
      accuracy_score(y_test, tree_prediction))


# Random Forest
print("Random Forest Accuracy:",
      accuracy_score(y_test, y_pred))

