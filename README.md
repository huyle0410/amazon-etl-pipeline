# Amazon Product Review ETL & Analytics Pipeline

A complete end-to-end data project that you can run to extract raw Amazon product reviews, clean and feature-engineer the data, load it into a database, and visualize insights with a Looker Studio dashboard.

---

## 📖 Table of Contents

1. [Project Overview](#project-overview)  
2. [Your Repo Structure](#your-repo-structure)  
3. [Getting Started](#getting-started)  
4. [ETL Pipeline](#etl-pipeline)  
5. [Notebooks](#notebooks)  
6. [Dashboard](#dashboard)  

---

## 🔍 Project Overview

I’ll work with a raw CSV of 1,465 Amazon product reviews to:

1. **Extract** the data  
2. **Transform**: clean prices, ratings, and engineer features such as `discount_amount`, `rating_score`, `category_lvl1`, `category_lvl2`, review lengths, etc.  
3. **Load** the processed data into SQLite  
4. **Analyze** in Jupyter notebooks  
5. **Visualize** with an interactive Looker Studio dashboard

This workflow demonstrates the full spectrum of a real-world Data Analyst or Data Engineer project.

---

## 📂 My Repo Structure

```text
.
├── README.md
├── airflow/                       
│   ├── dags/
│   └── logs/
├── dashboard/
│   └── Amazon_Review_&_Rating_Insights.pdf
├── data/
│   ├── raw/
│   └── processed/                 
├── database/
│   └── amazon_reviews.db        
├── notebooks/
│   ├── 01_amazon_eda_cleaning.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_product_insights.ipynb
├── requirements.txt              
├── run_pipeline.py             
└── scripts/
    ├── extract.py
    ├── transform.py
    └── load.py


## 🛠️ ETL Pipeline

### 1. Extract
I created `scripts/extract.py` to read `data/raw/amazon.csv` and write the cleaned file to `data/processed/amazon_clean.csv`.

### 2. Transform
In `scripts/transform.py`, I:

- Clean and parse prices, ratings, and counts  
- Engineer features such as `discount_amount`, `rating_score`, `category_lvl1`, `category_lvl2`, review title/content lengths, and word counts  
- Save the feature-engineered data to `data/processed/amazon_feature_engineered.csv`

### 3. Load
My `scripts/load.py` imports the engineered CSV into a SQLite database at `database/amazon_reviews.db`.

### 4. Run the Pipeline
To run the full pipeline, I simply execute: 

```bash
python3 run_pipeline.py



## 📓 Notebooks

- **01_amazon_eda_cleaning.ipynb**  
  I clean the raw data, handle missing values, and explore distributions of price, discount, and ratings.

- **02_feature_engineering.ipynb**  
  I create numeric, text, and categorical features (e.g. `discount_amount`, `rating_score`, `category_lvl2`), then save the engineered dataset.

- **03_product_insights.ipynb**  
  I analyze level-2 categories and my custom `rating_score`, producing bar charts that highlight top categories and product insights.

---

## 📊 Dashboard

**Amazon Review & Rating Insights**  
I exported my Looker Studio dashboard to PDF here:

[Download the Dashboard PDF](dashboard/Amazon_Review_&_Rating_Insights.pdf)

The PDF includes:

- Top 10 Level-2 Categories by Product Count  
- Average Rating Score by Category  
- Average Discount Ratio by Category  
- Top Products by Rating Score  

