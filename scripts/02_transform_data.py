import pandas as pd

# Load raw data
df = pd.read_csv("data/raw/nypd_complaint_raw.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Convert complaint date to datetime format
df["cmplnt_fr_dt"] = pd.to_datetime(df["cmplnt_fr_dt"], errors="coerce")

# Remove rows where complaint date is missing/invalid
df = df.dropna(subset=["cmplnt_fr_dt"])

# Create new date columns
df["complaint_date"] = df["cmplnt_fr_dt"].dt.strftime("%Y-%m-%d")
df["year"] = df["cmplnt_fr_dt"].dt.year
df["month"] = df["cmplnt_fr_dt"].dt.month
df["day"] = df["cmplnt_fr_dt"].dt.day
df["quarter"] = df["cmplnt_fr_dt"].dt.quarter

# Remove rows missing important fields
important_columns = ["boro_nm", "ofns_desc", "law_cat_cd"]
df = df.dropna(subset=important_columns)

# Create new column for crime severity
df["is_felony"] = df["law_cat_cd"].apply(lambda x: 1 if x == "FELONY" else 0)

# Save transformed data
df.to_csv("data/transformed/nypd_complaint_transformed.csv", index=False)

print("Data transformed and saved successfully.")
