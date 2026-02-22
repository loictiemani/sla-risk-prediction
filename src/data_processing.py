import pandas as pd

def load_raw_data(path="data/raw/sla_cases.csv"):
    """
    Load raw SLA dataset.
    """
    df = pd.read_csv(path)
    return df

def clean_data(df):
    """
    Basic cleaning: handle missing values, ensure types.
    """
    df = df.fillna(0)
    
    # Ensure boolean column
    if "breached" in df.columns:
        df["breached"] = df["breached"].astype(bool)
    return df

def save_processed_data(df, path="data/processed/df_cleaned.csv"):
    """
    Save cleaned dataframe for further processing.
    """
    df.to_csv(path, index=False)
    print(f"Cleaned data saved to {path}")