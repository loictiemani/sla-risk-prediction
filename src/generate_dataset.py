import pandas as pd
import numpy as np
import os

np.random.seed(42)
n = 5000

# Ensure output folder exists
os.makedirs("data/raw", exist_ok=True)

# ----------------------------
# Categorical domains
# ----------------------------
case_types = ["Work Permit", "Visa Renewal", "Relocation", "PR Application", "Tax", "Payroll"]
countries = ["US", "CA", "UK", "DE", "AU"]
stages = ["Intake", "Documentation", "Submission", "Government Review", "Decision", "Closure"]
priorities = ["Normal", "Urgent"]
complexities = ["Low", "Medium", "High"]

# ----------------------------
# Identifiers
# ----------------------------
case_id = np.arange(1, n + 1)

# "office_id" is more consistent with mobility operations than "officer_id"
office_id = np.random.randint(100, 120, size=n)

# ----------------------------
# Sample categorical fields
# ----------------------------
case_type = np.random.choice(case_types, n, p=[0.22, 0.18, 0.18, 0.10, 0.20, 0.12])
country = np.random.choice(countries, n, p=[0.30, 0.25, 0.18, 0.12, 0.15])
processing_stage = np.random.choice(stages, n, p=[0.15, 0.20, 0.15, 0.25, 0.15, 0.10])
priority = np.random.choice(priorities, n, p=[0.78, 0.22])
document_complexity = np.random.choice(complexities, n, p=[0.45, 0.40, 0.15])

# ----------------------------
# Operational numeric fields
# ----------------------------
# Represents active caseload handled by office/team
office_load = np.random.randint(20, 130, size=n)

# Missing documents at the point of intake / review
documents_missing = np.random.randint(0, 7, size=n)

# How long the client takes to return documents / respond (human factor)
client_response_delay_days = np.random.randint(0, 31, size=n)

# Reassignments between teams or handlers (workflow friction)
reassignment_count = np.random.poisson(lam=1.4, size=n)
reassignment_count = np.clip(reassignment_count, 0, 10)

# Days spent in current stage (proxy for bottleneck)
days_in_stage = np.random.randint(1, 46, size=n)

# ----------------------------
# SLA targets (in days)
# ----------------------------
# Base SLA depends on case type (more realistic than one shared list)
sla_base_by_case_type = {
    "Work Permit": 45,
    "Visa Renewal": 30,
    "Relocation": 35,
    "PR Application": 90,
    "Tax": 21,
    "Payroll": 14
}
sla_target_days = np.array([sla_base_by_case_type[ct] for ct in case_type])

# Adjust SLA target slightly by priority (urgent tends to have shorter target)
sla_target_days = sla_target_days - (priority == "Urgent") * 7
sla_target_days = np.clip(sla_target_days, 7, None)

# ----------------------------
# Simulate total processing time
# ----------------------------
# Complexity effect
complexity_weight = np.select(
    [document_complexity == "Low", document_complexity == "Medium", document_complexity == "High"],
    [0, 6, 14],
    default=6
)

# Stage effect (some stages naturally take longer)
stage_weight = np.select(
    [
        processing_stage == "Intake",
        processing_stage == "Documentation",
        processing_stage == "Submission",
        processing_stage == "Government Review",
        processing_stage == "Decision",
        processing_stage == "Closure",
    ],
    [2, 8, 6, 18, 10, 3],
    default=6
)

# Country effect (illustrative; keeps it realistic without claiming real-world timings)
country_weight = np.select(
    [country == "US", country == "CA", country == "UK", country == "DE", country == "AU"],
    [6, 5, 7, 8, 7],
    default=6
)

# Case type effect (baseline workload differences)
case_type_weight = np.select(
    [
        case_type == "Work Permit",
        case_type == "Visa Renewal",
        case_type == "Relocation",
        case_type == "PR Application",
        case_type == "Tax",
        case_type == "Payroll",
    ],
    [10, 7, 9, 20, 6, 4],
    default=8
)

# Office load scales time (more load = slower throughput)
office_load_weight = office_load / 12.0  # ~1.7 to ~10.8 days

# Missing docs and reassignments add friction
documents_weight = documents_missing * 2.2
reassignment_weight = reassignment_count * 3.8

# Total processing time (add noise to avoid perfectly deterministic labels)
noise = np.random.normal(loc=0, scale=5, size=n)

total_processing_days = (
    case_type_weight
    + stage_weight
    + country_weight
    + complexity_weight
    + office_load_weight
    + documents_weight
    + client_response_delay_days
    + reassignment_weight
    + days_in_stage * 0.35
    + noise
)

# Avoid negatives
total_processing_days = np.clip(total_processing_days, 1, None)

# SLA breach label
sla_breach = total_processing_days > sla_target_days

# ----------------------------
# Build DataFrame
# ----------------------------
df = pd.DataFrame({
    "case_id": case_id,
    "case_type": case_type,
    "country": country,
    "processing_stage": processing_stage,
    "office_id": office_id,
    "office_load": office_load,
    "priority": priority,
    "document_complexity": document_complexity,
    "documents_missing": documents_missing,
    "client_response_delay_days": client_response_delay_days,
    "reassignment_count": reassignment_count,
    "days_in_stage": days_in_stage,
    "sla_target_days": sla_target_days.astype(int),
    "total_processing_days": np.round(total_processing_days, 1),
    "sla_breach": sla_breach
})

# Save to CSV
out_path = "data/raw/sla_cases.csv"
df.to_csv(out_path, index=False)

print(f"Synthetic mobility SLA dataset generated with {n} rows")
print(f"Saved to: {out_path}")
print("SLA breach rate:", round(df["sla_breach"].mean() * 100, 2), "%")
