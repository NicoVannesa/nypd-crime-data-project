import pandas as pd

# Load transformed dataset
df = pd.read_csv("data/transformed/nypd_complaint_transformed.csv")

# Simulate loading data into warehouse dimension tables

dim_date = df[[
    "complaint_date",
    "year",
    "quarter",
    "month",
    "day"
]].drop_duplicates()

dim_location = df[[
    "boro_nm",
    "addr_pct_cd",
    "latitude",
    "longitude"
]].drop_duplicates()

dim_crime = df[[
    "ofns_desc",
    "law_cat_cd",
    "is_felony"
]].drop_duplicates()

dim_premises = df[[
    "prem_typ_desc"
]].drop_duplicates()

dim_suspect = df[[
    "susp_age_group",
    "susp_race",
    "susp_sex"
]].drop_duplicates()

# Save dimension tables

dim_date.to_csv("data/transformed/dim_date.csv", index=False)
dim_location.to_csv("data/transformed/dim_location.csv", index=False)
dim_crime.to_csv("data/transformed/dim_crime.csv", index=False)
dim_premises.to_csv("data/transformed/dim_premises.csv", index=False)
dim_suspect.to_csv("data/transformed/dim_suspect.csv", index=False)

print("Dimension tables successfully created.")import pandas as pd

# Load transformed dataset
df = pd.read_csv("data/transformed/nypd_complaint_transformed.csv")

# Simulate loading data into warehouse dimension tables

dim_date = df[[
    "complaint_date",
    "year",
    "quarter",
    "month",
    "day"
]].drop_duplicates()

dim_location = df[[
    "boro_nm",
    "addr_pct_cd",
    "latitude",
    "longitude"
]].drop_duplicates()

dim_crime = df[[
    "ofns_desc",
    "law_cat_cd",
    "is_felony"
]].drop_duplicates()

dim_premises = df[[
    "prem_typ_desc"
]].drop_duplicates()

dim_suspect = df[[
    "susp_age_group",
    "susp_race",
    "susp_sex"
]].drop_duplicates()

# Save dimension tables

dim_date.to_csv("data/transformed/dim_date.csv", index=False)
dim_location.to_csv("data/transformed/dim_location.csv", index=False)
dim_crime.to_csv("data/transformed/dim_crime.csv", index=False)
dim_premises.to_csv("data/transformed/dim_premises.csv", index=False)
dim_suspect.to_csv("data/transformed/dim_suspect.csv", index=False)

print("Dimension tables successfully created.")
