
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.neighbors import NearestNeighbors

# Load dataset
df = pd.read_csv("data.csv")
df.columns = df.columns.str.strip()
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

# Clean numeric columns
for col in ["price", "spec_rating", "Ram", "ROM", "display_size"]:
    df[col] = pd.to_numeric(
        df[col].astype(str).str.extract(r"(\d+\.?\d*)")[0],
        errors="coerce"
    )

df = df.dropna(subset=["price", "Ram", "ROM"])
df["brand"] = df["brand"].fillna("Unknown")
df["processor"] = df["processor"].fillna("Unknown")

print("\n===== LAPTOP RECOMMENDATION SYSTEM =====")

budget = float(input("Enter your maximum budget (₹): "))
ram = float(input("Enter required RAM (GB): "))
storage = float(input("Enter required storage (GB): "))
brand = input("Preferred brand (or Any): ").strip().lower()
processor = input("Preferred processor (or Any): ").strip().lower()

# Filter laptops according to requirements
candidates = df[
    (df["price"] <= budget) &
    (df["Ram"] >= ram) &
    (df["ROM"] >= storage)
].copy()

if brand != "any":
    candidates = candidates[
        candidates["brand"].str.lower().str.contains(brand, na=False)
    ]

if processor != "any":
    candidates = candidates[
        candidates["processor"].str.lower().str.contains(processor, na=False)
    ]

if candidates.empty:
    print("\nNo laptops match your requirements.")
else:
    # Features used by KNN
    numeric = ["price", "Ram", "ROM", "spec_rating"]
    categorical = ["brand", "processor", "OS", "GPU"]

    numeric = [c for c in numeric if c in candidates.columns]
    categorical = [c for c in categorical if c in candidates.columns]

    for col in numeric:
        candidates[col] = candidates[col].fillna(candidates[col].median())
    for col in categorical:
        candidates[col] = candidates[col].fillna("Unknown")

    features = numeric + categorical

    preprocess = ColumnTransformer([
        ("num", StandardScaler(), numeric),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical)
    ])

    X = preprocess.fit_transform(candidates[features])

    # KNN model
    model = NearestNeighbors(
        n_neighbors=min(5, len(candidates)),
        metric="euclidean"
    )
    model.fit(X)

    # Use an eligible laptop as a query reference
    query = candidates.iloc[[0]][features]
    distances, indices = model.kneighbors(preprocess.transform(query))

    print("\n===== RECOMMENDED LAPTOPS =====")
    results = candidates.iloc[indices[0]].copy()
    results["KNN Distance"] = distances[0]

    display_cols = [
        c for c in [
            "brand", "name", "price", "Ram", "ROM",
            "processor", "OS", "spec_rating"
        ] if c in results.columns
    ]

    print(results[display_cols].to_string(index=False))
