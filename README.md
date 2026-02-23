# Global Mobility SLA Risk Prediction
### Applied Machine Learning for Operational Decision Support

![Python](https://img.shields.io/badge/Python-3.10-blue)
![ML](https://img.shields.io/badge/ML-RandomForest-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## Project Overview

This project develops an **early-warning machine learning system** that predicts whether a case is likely to miss its Service Level Agreement (SLA) deadline in a global mobility workflow.

Rather than identifying delays after they occur, the system flags **high-risk active cases** so operational teams can intervene before a breach happens.

The project demonstrates an end-to-end applied AI pipeline:
- synthetic workflow data generation
- data cleaning and feature engineering
- predictive modeling
- model interpretability
- subgroup error analysis
- operational scoring

The objective is to illustrate how machine learning can support **proactive decision-making in service and compliance-driven organizations**.

---

## Problem

Operational reporting typically answers:

> “Which cases already missed their deadlines?”

However, organizations actually need:

> “Which ongoing cases are likely to miss their deadlines?”

This project reframes SLA monitoring as a **predictive classification problem**.

The model predicts:

**SLA Breach Risk = probability a case will exceed its allowed processing time**

This transforms performance monitoring from reactive reporting to proactive operational intelligence.

---

## Dataset

The dataset is fully **synthetic** and does not contain any proprietary or client information.

It simulates a realistic global mobility case lifecycle:

| Feature | Description |
|--------|------|
| case_type | Work permit, relocation, tax, payroll, etc. |
| country | Destination country |
| processing_stage | Workflow stage (intake → review → decision) |
| office_load | Current workload handled by the office/team |
| documents_missing | Missing documentation count |
| client_response_delay_days | Client response delay |
| reassignment_count | Number of workflow handoffs |
| days_in_stage | Time spent in current stage |
| sla_target_days | Expected completion time |
| sla_breach | Target variable |

**Dataset size:** ~5,000 synthetic cases

The synthetic dataset is intentionally designed so delays are influenced by operational factors such as workload, complexity, and client responsiveness.

---

## Pipeline

### 1. Data Engineering
- Synthetic workflow generation
- Cleaning and validation
- Handling missing values

### 2. Feature Engineering
Derived operational indicators:
- workload intensity
- documentation completeness
- stage delay ratios
- reassignment friction
- client responsiveness

### 3. Modeling
Models evaluated:
- Logistic Regression (baseline)
- Random Forest (final model)

Evaluation metrics:
- Precision
- Recall
- ROC-AUC
- Precision-Recall AUC

A recall-oriented threshold is used because the goal is **early detection of risky cases**.

---

## Results

The model successfully identifies patterns associated with delayed cases.

Key drivers of SLA risk:
- high office workload
- missing documentation
- repeated reassignment
- long time in workflow stage
- delayed client response

The model enables proactive monitoring rather than post-incident reporting.

---

## Interpretability

The project includes:
- feature importance analysis
- permutation importance
- case-level explanation examples

This allows operational teams to understand *why* a case is flagged, not just that it is flagged.

---

## Responsible AI Considerations

This system is designed as **decision support**, not automated decision-making.

- Human review is required before any action
- Thresholds can be tuned to operational priorities
- Subgroup performance (country, case type, stage) should be monitored
- Periodic retraining is recommended

The goal is to augment human workflow management, not replace it.

---

## Repository Structure
```
sla-risk-prediction/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   │   └── mobility_sla_cases.csv
│   ├── processed/
│   │   └── mobility_sla_cases_clean.csv
│   └── README.md
│
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_modeling.ipynb
│   ├── 04_interpretability.ipynb
│   ├── 05_error_analysis.ipynb
│   └── 06_demo_scoring.ipynb
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_processing.py
│   ├── features.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── models/
│   └── sla_rf_model.pkl
│
├── outputs/
│   └── predictions.csv
│
└── images/
    ├── roc_curve.png
    ├── feature_importance.png
    └── subgroup_recall.png

```

---

## How to Run

1) Generate dataset  
Run the synthetic data generator script.

2) Feature engineering  
Run `02_feature_engineering.ipynb`

3) Train model  
Run `03_modeling.ipynb`

4) Interpret model  
Run `04_interpretability.ipynb`

5) Score new cases  
Run `06_demo_scoring.ipynb`

---

## Why This Project Matters

Many operational organizations rely on dashboards that describe performance after delays occur.  
This project demonstrates how AI can shift operations from:

**reactive reporting → predictive intervention**

It illustrates applied machine learning in a real organizational context involving workflow management, compliance risk, and human-AI collaboration.

---

## Author

Loïc Tiemani  
Data & Analytics Professional | Applied AI Interest

