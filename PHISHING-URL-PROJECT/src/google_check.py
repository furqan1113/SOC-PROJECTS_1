import pandas as pd
import joblib

from feature_test import extract_features


# Load the original dataset
df = pd.read_csv("../datasets/PhiUSIIL_Phishing_URL_Dataset.csv")


# Load our trained model
model = joblib.load("../model.pkl")


# Get 10 legitimate URLs
legitimate_urls = df[df["label"] == 1]["URL"].head(10)


print("Testing legitimate URLs:\n")


for url in legitimate_urls:

    # Extract the same 16 features used during training
    features = extract_features(url)

    # Make prediction
    prediction = model.predict([features])[0]

    # Actual label
    actual = 1

    # Convert prediction to text
    if prediction == 1:
        result = "LEGITIMATE"
    else:
        result = "PHISHING"

    print("URL:", url)
    print("Actual: LEGITIMATE")
    print("Predicted:", result)

    if prediction == actual:
        print("Status: CORRECT")
    else:
        print("Status: WRONG")

    print("-" * 60)