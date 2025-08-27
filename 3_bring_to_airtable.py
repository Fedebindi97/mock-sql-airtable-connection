import pandas as pd
from sqlalchemy import create_engine
import requests

# --- CONFIG ---
POSTGRES_URL = "postgresql://postgres:#8S8NUP3FZ*MztS@db.gvvzylsyumunjpxiqyui.supabase.co:5432/postgres"

AIRTABLE_BASE_ID = "appEoUxfn1g6zSX7t"  # Replace with your base ID
AIRTABLE_TABLE = "Beneficiaries"
AIRTABLE_TOKEN = "paton3VX1dXDlPQl3.28f17a8a52b26291d184d51e653fb9a5d856f57908e53aeb4e33de18d25aa5b0"   # Replace with your token

# --- GET FILTERED ROWS ---
engine = create_engine(POSTGRES_URL)
query = "SELECT * FROM beneficiaries WHERE status != 'Completed' LIMIT 1000;"
df = pd.read_sql(query, engine)

print(f"✅ Selected {len(df)} rows for Airtable")

# --- PUSH TO AIRTABLE ---
url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE}"
headers = {
    "Authorization": f"Bearer {AIRTABLE_TOKEN}",
    "Content-Type": "application/json"
}

for _, row in df.iterrows():
    record = {"fields": row.to_dict()}
    r = requests.post(url, json=record, headers=headers)
    if r.status_code not in (200, 201):
        print("⚠️ Error:", r.text)

print("✅ Data synced to Airtable")

