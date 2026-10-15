from pathlib import Path
import pandas as pd

csv_path = Path.home() / "Desktop" / "PHISHING-URL-PROJECT" / "datasets" / "PhiUSIIL_Phishing_URL_Dataset.csv"
df = pd.read_csv(csv_path)

print(df.shape)
print(df.columns)
print(df.head())
print(df["label"].value_counts())