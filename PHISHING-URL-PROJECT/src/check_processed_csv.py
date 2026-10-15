import pandas as pd

# Load our processed dataset
df = pd.read_csv("../datasets/processed_features.csv")

# Check the size of the dataset
print("Shape:", df.shape)

# Check the label distribution
print("\nLabels:")
print(df["label"].value_counts())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())