"""
generate_sample_data.py
-----------------------
Run once to create sample_sales_data.csv for demo purposes.

    python generate_sample_data.py
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

# Config
N = 500
REGIONS = ["North", "South", "East", "West"]
PRODUCTS = ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard", "Mouse", "Headphones"]
CATEGORIES = {
    "Laptop": "Electronics", "Phone": "Electronics", "Tablet": "Electronics",
    "Monitor": "Peripherals", "Keyboard": "Peripherals",
    "Mouse": "Peripherals", "Headphones": "Audio"
}
SALES_REPS = [f"Rep_{i:02d}" for i in range(1, 11)]

# Generate dates
start_date = datetime(2024, 1, 1)
dates = [start_date + timedelta(days=random.randint(0, 364)) for _ in range(N)]

# Generate product data
products = random.choices(PRODUCTS, k=N)

# Generate price based on product
price_map = {
    "Laptop": (600, 1500), "Phone": (300, 1000), "Tablet": (200, 800),
    "Monitor": (150, 500), "Keyboard": (30, 150), "Mouse": (15, 80),
    "Headphones": (50, 300)
}

unit_prices = [
    round(random.uniform(*price_map[p]), 2) for p in products
]

quantities = [random.randint(1, 10) for _ in range(N)]
revenue = [round(p * q, 2) for p, q in zip(unit_prices, quantities)]

# Churn flag (for variety)
customer_ids = [f"CUST_{random.randint(1000, 9999)}" for _ in range(N)]

df = pd.DataFrame({
    "order_id": [f"ORD-{i:05d}" for i in range(1, N + 1)],
    "date": [d.strftime("%Y-%m-%d") for d in dates],
    "month": [d.strftime("%B") for d in dates],
    "quarter": [f"Q{(d.month - 1) // 3 + 1}" for d in dates],
    "customer_id": customer_ids,
    "sales_rep": random.choices(SALES_REPS, k=N),
    "region": random.choices(REGIONS, k=N),
    "product": products,
    "category": [CATEGORIES[p] for p in products],
    "unit_price": unit_prices,
    "quantity": quantities,
    "revenue": revenue,
    "discount_pct": [random.choice([0, 5, 10, 15, 20]) for _ in range(N)],
})

# Add a few missing values (realistic)
df.loc[df.sample(10).index, "discount_pct"] = None

df.to_csv("sample_sales_data.csv", index=False)
print(f"[✓] sample_sales_data.csv created — {N} rows")
print(df.head(3).to_string())
