import pandas as pd
import os


# ------------------------------------------------
# Load raw dataset
# ------------------------------------------------
def load_raw_data(path: str) -> pd.DataFrame:
    """
    Load raw mobility SLA dataset.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Raw dataset not found at: {path}")

    df = pd.read_csv(path)
    print(f"Loaded raw dataset: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


# ------------------------------------------------
# Clean dataset
# ------------------------------------------------
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic cleaning and type enforcement.
    """

    # Drop duplicate cases
    df = df.drop_duplicates()

    # Convert boolean target safely
    if "sla_breach" in df.columns:
        df["sla_breach"] = df["sla_breach"].astype(int)

    # Fill numeric missing values
    numeric_cols = df.select_dtypes(include=["number"]).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)

    # Fill categorical missing values
    cat_cols = df.select_dtypes(include=["object"]).columns
    df[cat_cols] = df[cat_cols].fillna("Unknown")

    return df


# ------------------------------------------------
# Save processed dataset
# ------------------------------------------------
def save_processed_data(df: pd.DataFrame, path: str):
    """
    Save processed dataframe for modeling.
    Automatically creates the directory if needed.
    """

    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)

    df.to_csv(path, index=False)
    print(f"✅ Processed dataset saved to: {path}")
