# SLA Risk Prediction & Detection

## Project Overview
This project predicts SLA breaches in operational case management workflows. Inspired by real-world global mobility operations, it demonstrates end-to-end data engineering, feature engineering, and predictive modeling.

## Problem Statement
Identify cases at risk of missing SLA deadlines, enabling proactive workload balancing and decision support.

## Dataset
- Synthetic dataset simulating case workflows
- ~5,000 rows
- Features include case type, processing stage, officer load, document completeness, and duration

## Pipeline
1. Data Cleaning & Preprocessing
2. Feature Engineering
3. Model Training & Evaluation
4. Insights & Visualizations

## Modeling
- Logistic Regression, Random Forest, XGBoost
- Evaluation metrics: Accuracy, Precision, Recall, F1, ROC-AUC

## Key Findings
- Feature importance analysis
- Identification of high-risk patterns

## How to Run
1. Install dependencies: `pip install -r requirements.txt`  
2. Run notebooks in order: 01 → 02 → 03  
3. Outputs saved in `outputs/`

## Learnings & Next Steps
- Demonstrated end-to-end pipeline creation
- Prepared dataset for potential real-time SLA monitoring
- Extension: implement streaming SLA predictions using Kafka & Spark