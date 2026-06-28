# Athens Airbnb Market Intelligence & Price Prediction

## Project Overview

This is an end-to-end Business Intelligence and Machine Learning portfolio project focused on the Athens short-term rental market.

The project uses public Airbnb data for Athens and demonstrates the complete workflow from messy data cleaning to business dashboarding and predictive modeling.

## Business Problem

The objective is to understand the Athens Airbnb market and predict listing price / high-price potential using listing characteristics, location, host information, reviews, availability and amenities.

## Main Questions

- Which neighbourhoods have the highest listing concentration?
- Which factors influence nightly price?
- Can machine learning predict Airbnb listing prices in Athens?
- Which listings are likely to belong to the high-price segment?
- How can the results be communicated through Excel, Power BI and PowerPoint?

## Tools

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost / LightGBM
- Excel
- Power BI
- PowerPoint
- Git / GitHub

## Data Source

Primary source: Inside Airbnb Athens data.

Main files:
- `listings.csv.gz`
- `calendar.csv.gz`
- `reviews.csv.gz`
- `listings.csv`
- `reviews.csv`
- `neighbourhoods.csv`
- `neighbourhoods.geojson`

Download the files manually from Inside Airbnb and place them in:

```text
data/raw/
```

## Repository Structure

```text
athens-airbnb-bi-ml-project/
│
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_visualisation.ipynb
│   ├── 04_modeling_price_prediction.ipynb
│   └── 05_classification_revenue_potential.ipynb
│
├── src/
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── modeling.py
│   └── evaluation.py
│
├── models/
├── excel/
├── powerbi/
├── presentation/
├── reports/
└── images/
```

## Workflow

1. Data collection
2. Data understanding
3. Data cleaning
4. Feature engineering
5. Exploratory data analysis
6. Regression model for price prediction
7. Classification model for high-price listing prediction
8. Excel dashboard
9. Power BI dashboard
10. PowerPoint business presentation

## Target Variables

### Regression

```text
price
```

or preferably:

```text
log_price
```

### Classification

```text
high_price_listing = 1 if price is above the 75th percentile
high_price_listing = 0 otherwise
```

## Planned Models

### Regression

- Linear Regression
- Ridge Regression
- Lasso Regression
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost / LightGBM

### Classification

- Logistic Regression
- Random Forest Classifier
- Gradient Boosting Classifier
- XGBoost / LightGBM

## Model Evaluation

Regression metrics:

- MAE
- RMSE
- R²
- Cross-validation RMSE

Classification metrics:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion matrix

## Excel Deliverable

File to be created:

```text
excel/Athens_Airbnb_Excel_Analysis.xlsx
```

Suggested sheets:

- Raw Sample
- Cleaned Data
- Data Dictionary
- Pivot - Neighbourhood
- Pivot - Room Type
- Dashboard
- What-if Analysis
- Model Output

## Power BI Deliverable

File to be created:

```text
powerbi/Athens_Airbnb_Market_Intelligence.pbix
```

Suggested pages:

1. Executive Overview
2. Neighbourhood Analysis
3. Pricing Drivers
4. Availability & Revenue Potential
5. Machine Learning Insights

## PowerPoint Deliverable

File to be created:

```text
presentation/Athens_Airbnb_BI_Project_Presentation.pptx
```

Suggested slides:

1. Project Title
2. Business Problem
3. Data Sources
4. Data Cleaning Challenges
5. EDA Findings
6. Market Insights
7. Machine Learning Approach
8. Model Results
9. Power BI Dashboard
10. Business Recommendations
11. Limitations
12. Next Steps

## Author

Zisis Mandanas