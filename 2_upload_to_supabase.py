import pandas as pd
from sqlalchemy import create_engine

# --- CONFIG ---
POSTGRES_URL = "YOUR_POSTGRES_URL"

# --- LOAD CSV ---
df = pd.read_csv("beneficiaries.csv")

# --- UPLOAD ---
engine = create_engine(POSTGRES_URL)

# Upload to Supabase (replace old table if exists)
df.to_sql("beneficiaries", engine, if_exists="replace", index=False)

print("✅ CSV uploaded to Supabase PostgreSQL")
