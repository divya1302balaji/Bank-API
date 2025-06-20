import pandas as pd
from app.database import init_db, SessionLocal
from app.models import Bank, Branch

# Initialize the DB
init_db()
db = SessionLocal()

# Load the CSV
df = pd.read_csv("bank_branches.csv")

# Drop rows with missing essential values
df.dropna(subset=['bank_name', 'ifsc', 'branch'], inplace=True)

# Cache to avoid duplicate banks
bank_cache = {}

# Insert data
for _, row in df.iterrows():
    bank_name = row['bank_name']
    ifsc = row['ifsc']
    branch_name = row['branch']

    # Add bank only once
    if bank_name not in bank_cache:
        bank = Bank(name=bank_name)
        db.add(bank)
        db.flush()  # Assign ID
        bank_cache[bank_name] = bank
    else:
        bank = bank_cache[bank_name]

    # Add branch
    branch = Branch(ifsc=ifsc, branch=branch_name, bank=bank)
    db.add(branch)

# Commit changes
db.commit()
db.close()

print("✅ bank_branches.csv loaded into test.db successfully.")
