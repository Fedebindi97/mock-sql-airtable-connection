import pandas as pd
from sqlalchemy import create_engine
import requests

# --- CONFIG ---
POSTGRES_URL = "YOUR_POSTGRES_URL"

AIRTABLE_BASE_ID = "YOUR_AIRTABLE_BASE_ID"  # Replace with your base ID
AIRTABLE_TABLE = "Beneficiaries"
AIRTABLE_TOKEN = "YOUR_AIRTABLE_TOKEN"   # Replace with your token

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

