import pandas as pd
from feature_test import extract_features

# Load processed dataset
df = pd.read_csv("../datasets/processed_features.csv")

# Extract features from Google
url = "https://google.com"
features = extract_features(url)

feature_names = [
    "URLLength",
    "DotCount",
    "HyphenCount",
    "DigitCount",
    "AtSymbol",
    "SubdomainCount",
    "IsIP",
    "IsHTTPS",
    "PathDepth",
    "SuspiciousTerms"
]

# Find dataset rows with exactly the same features
matches = df[
    (df[feature_names] == features).all(axis=1)
]

print("Google features:")
print(features)

print("\nMatching rows in dataset:", len(matches))

print("\nLabels of matching rows:")
print(matches["label"].value_counts())