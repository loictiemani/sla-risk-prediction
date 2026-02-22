import pandas as pd
import numpy as np

np.random.seed(42)
n = 5000

# Basic fields
case_id = np.arange(1, n+1)
case_types = ["Tax", "Relocation", "Immigration", "Payroll"]
countries = ["US", "CA", "UK", "DE"]
stages = ["Intake", "Review", "Approval", "Closure"]
officer_ids = np.random.randint(100, 110, size=n)

# Randomly assign categorical fields
case_type = np.random.choice(case_types, n)
country = np.random.choice(countries, n)
processing_stage = np.random.choice(stages, n)

# Numeric fields
officer_load = np.random.randint(5, 26, size=n)
documents_missing = np.random.randint(0, 6, size=n)
duration_days = np.random.randint(1, 31, size=n)
sla_days = np.random.choice([7, 10, 14, 21], n)

# Generate SLA breach with realistic probability
# baseline probability
prob = (
    0.1 +
    0.02 * (officer_load - 5) +
    0.1 * documents_missing +
    0.03 * (duration_days / sla_days)
)
prob = np.clip(prob, 0, 1)
breached = np.random.binomial(1, prob)

# Build DataFrame
df = pd.DataFrame({
    "case_id": case_id,
    "case_type": case_type,
    "country": country,
    "processing_stage": processing_stage,
    "officer_id": officer_ids,
    "officer_load": officer_load,
    "documents_missing": documents_missing,
    "duration_days": duration_days,
    "sla_days": sla_days,
    "breached": breached.astype(bool)
})

# Save to CSV
df.to_csv("data/raw/sla_cases.csv", index=False)
print("Synthetic SLA dataset generated with", n, "rows")