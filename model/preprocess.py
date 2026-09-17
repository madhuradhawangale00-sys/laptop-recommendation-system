import pandas as pd

# Load dataset
df = pd.read_csv("dataset\data.csv")

print("Original shape:", df.shape)

# Remove unnecessary index columns
df = df.drop(columns=["Unnamed: 0.1", "Unnamed: 0"])

print("\nColumns after removing unnecessary columns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

# Convert RAM from string to integer
df["Ram"] = df["Ram"].str.extract(r"(\d+)").astype(int)

print("\nRAM values:")
print(df["Ram"].unique())

print("\nROM data type:")
print(df["ROM"].dtype)

print("\nROM values:")
print(df["ROM"].unique())


print("\n========== PROCESSORS ==========")
print(df["processor"].value_counts().head(20))

print("\n========== GPUs ==========")
print(df["GPU"].value_counts().head(20))