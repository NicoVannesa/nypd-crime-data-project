import pandas as pd

#NYC Open Data API URL
url = "https://data.cityofnewyork.us/resource/qgea-i56i.csv?$limit=5000"

#Read dataset
df = pd.read_csv(url)

#Save raw data locally
df.to_csv("data/raw/nypd_complaint_raw.csv", index=False)

print("Data successfully sourced and saved."
