import pandas as pd
from pathlib import Path

raw_path = "data/raw/McDonalds_Financial_Statements.csv"
processed_path = Path("data/processed")
processed_path.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(raw_path)

assert "Year" in df.columns, "Year column missing"

df = df.sort_values("Year").reset_index(drop=True)

assert df.isna().sum().sum() == 0, "Missing values detected"

df.columns = df.columns.str.lower().str.replace(" ","_")

assert df["year"].is_monotonic_increasing, "Years are still not ordered"

df.to_csv(processed_path / "mcdonalds_financials_clean.csv", index=False)

print("Data validated and saved to processed")