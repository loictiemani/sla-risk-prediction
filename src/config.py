import os
import sys

# ----------------------------
# Project root (works no matter where script is executed)
# ----------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Make src importable
SRC_PATH = os.path.join(PROJECT_ROOT, "src")
if SRC_PATH not in sys.path:
    sys.path.append(SRC_PATH)

# ----------------------------
# Data directories
# ----------------------------
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
RAW_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DIR = os.path.join(DATA_DIR, "processed")

# Create folders automatically if missing
os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

# ----------------------------
# File paths
# ----------------------------
RAW_PATH = os.path.join(RAW_DIR, "sla_cases.csv")
PROCESSED_PATH = os.path.join(PROCESSED_DIR, "sla_cases_clean.csv")

# (Optional — you’ll use this soon)
MODEL_DIR = os.path.join(PROJECT_ROOT, "models")
os.makedirs(MODEL_DIR, exist_ok=True)

MODEL_PATH = os.path.join(MODEL_DIR, "sla_rf_model.pkl")

