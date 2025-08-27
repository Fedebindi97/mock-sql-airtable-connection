import pandas as pd
from faker import Faker
import random

fake = Faker()
rows = []

statuses = ["To Assign", "In Progress", "Completed"]
help_types = ["Food", "Medicine", "Shelter", "Psychological Support"]

for i in range(1, 201):
    rows.append({
        "id": i,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "age": random.randint(5, 90),
        "city": fake.city(),
        "help_type": random.choice(help_types),
        "status": random.choice(statuses)
    })

df = pd.DataFrame(rows)
df.to_csv("beneficiaries.csv", index=False)