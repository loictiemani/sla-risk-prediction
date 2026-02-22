import pandas as pd

def create_features(df):
    """
    Feature engineering for SLA prediction.
    """
    # Officer workload ratio
    df['officer_load_ratio'] = df['officer_load'] / df['sla_days']
    
    # Time to SLA
    df['time_ratio'] = df['duration_days'] / df['sla_days']
    
    # Document completeness
    max_docs = df['documents_missing'].max() if df['documents_missing'].max() > 0 else 1
    df['doc_complete'] = 1 - df['documents_missing'] / max_docs
    
    # One-hot encode categorical columns
    categorical_cols = ['case_type', 'country', 'processing_stage']
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    
    return df

def save_features(df, path="data/processed/features.csv"):
    """
    Save feature-engineered dataframe.
    """
    df.to_csv(path, index=False)
    print(f"Features saved to {path}")