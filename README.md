# SLA Breach Prediction – Operational Intelligence Project

![Python](https://img.shields.io/badge/Python-3.10-blue)
![ML](https://img.shields.io/badge/ML-RandomForest%2CXGBoost-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## **Project Overview**

This project predicts **Service Level Agreement (SLA) breaches** in a global mobility services environment. It demonstrates an end-to-end **data engineering, feature engineering, and machine learning pipeline** using synthetic SLA case data.

The goal is to help case management teams and attorneys monitor **SLA performance, case lifecycle progression, and compliance deadlines**, and to enable **data-driven process optimization**.

---

## **Motivation**

In operational and legal environments, SLA breaches can have **financial and compliance consequences**. Predicting which cases are at risk allows teams to:

- Prioritize high-risk cases
- Allocate resources efficiently
- Reduce delays and improve service quality

---

## **Dataset**

The dataset is **synthetic** and designed to simulate realistic SLA operations:

| Feature | Description |
|---------|-------------|
| `case_id` | Unique identifier for each case |
| `case_type` | Type of case (e.g., Tax, Relocation, Immigration) |
| `country` | Client location |
| `processing_stage` | Current stage in case workflow |
| `officer_id` | Assigned officer |
| `officer_load` | Number of active cases for officer |
| `documents_missing` | Number of missing documents |
| `duration_days` | Days since case creation |
| `sla_days` | SLA threshold in days |
| `breached` | Target variable: True if SLA exceeded |

**Synthetic Dataset Size:** 5,000+ rows

---

## **Project Structure**

```text
SLA-Prediction/
│
├── data/
│   ├── raw/                 # Raw CSV dataset
│   └── processed/           # Cleaned & feature-engineered datasets
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_modeling.ipynb
│
├── src/
│   ├── data_processing.py
│   ├── feature_engineering.py
│   └── modeling.py
│
├── outputs/
│   └── models/              # Saved trained ML models
│
├── README.md
└── requirements.txt