import joblib
import pandas as pd

from feature_test import extract_features


# Load the trained model
model = joblib.load("../model.pkl")


# Ask the user for a URL
url = input("Enter URL: ").strip()


# ---------------- URL VALIDATION ----------------

# Check if the user entered something
if not url:

    print("\nError: URL cannot be empty.")

    exit()


# Add https:// if the user did not enter http:// or https://
if not url.startswith(("http://", "https://")):

    url = "https://" + url


# Check that something exists after the protocol
rest = url.split("//", 1)[1]

if not rest or "." not in rest.split("/", 1)[0]:

    print("\nError: Please enter a valid domain.")

    exit()


# ---------------- FEATURE EXTRACTION ----------------

features = extract_features(url)


# Names of our 16 features
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
    "SuspiciousTerms",
    "DomainLength",
    "PathLength",
    "QueryLength",
    "SpecialCharCount",
    "SlashCount",
    "EqualsCount"
]


# Convert features into a DataFrame
features_df = pd.DataFrame(
    [features],
    columns=feature_names
)


# ---------------- PREDICTION ----------------

prediction = model.predict(features_df)[0]

probabilities = model.predict_proba(features_df)[0]

confidence = max(probabilities) * 100


# ---------------- DISPLAY RESULT ----------------

print("\n------------------------------")
print("     PHISHING URL DETECTOR")
print("------------------------------")

print("URL:", url)

if prediction == 0:
    print("Result: PHISHING")
else:
    print("Result: LEGITIMATE")

print(f"Confidence: {confidence:.2f}%")

print("------------------------------")