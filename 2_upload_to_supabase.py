import pandas as pd
from sqlalchemy import create_engine

# --- CONFIG ---
POSTGRES_URL = "postgresql://postgres:#8S8NUP3FZ*MztS@db.gvvzylsyumunjpxiqyui.supabase.co:5432/postgres"

# --- LOAD CSV ---
df = pd.read_csv("beneficiaries.csv")

# --- UPLOAD ---
engine = create_engine(POSTGRES_URL)

# Upload to Supabase (replace old table if exists)
df.to_sql("beneficiaries", engine, if_exists="replace", index=False)

print("✅ CSV uploaded to Supabase PostgreSQL")
