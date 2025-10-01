# From Westeros To Twitter
This repository contains he project demonstrates practical data science workflows across shell scripting, web scraping, text and social media analysis, and machine learning modeling.
**Created by Robiatul Adawiyah Al-Qosh**.  

## Tasks Overview

### Task A – Web Scraping
Collected and processed online data with R (`rvest`):
- **A1**: Scraped ICC Men’s T20I Team Rankings (Wikipedia).  
  Cleaned citations, converted columns, summarized average ranking duration per country.
- **A2**: Scraped Westeros houses dataset (*A Song of Ice and Fire*).  
  Cleaned region names, split multiple regions, and visualized counts per region (largest: Reach, smallest: Dorne).

### Task B – Social Media Analysis (Tokyo Olympics Tweets)
Analyzed tweets from **Olympics_tweets.csv**:
1. **User Analysis**
   - Accounts created per year.
   - Average followers after 2010.
   - Top 10 user locations (London, USA, UK, Melbourne, etc.).
2. **Tweet Analysis**
   - Number of tweets per day (July 2021).
   - Tweet length categories (most common: 121–160 chars).
   - Mentions analysis: 25,982 tweets contained mentions; ~10,739 had 3+ mentions.
   - Word frequency analysis before/after stopword removal (keywords: *olympics, tokyo, gold, medal, team*).

### Task C – Dialogue Usefulness Prediction
Built predictive models for dialogue usefulness:
- **C1**: Engineered features (utterance count, dialogue duration, sentiment score).  
- **C2**: Regression tree model (`rpart`) with RMSE ≈ 1.21.  
- **C3**: Feature selection improved RMSE to 0.89. Compared with Random Forest (RMSE ≈ 1.09).  
- **C4**: Tested models on example dialogues, including soccer transfer negotiations.

---

## Requirements

- **R (≥ 4.0.0)**  
- **RStudio** (recommended)  
- R packages:
  - `tidyverse`
  - `rvest`
  - `tidytext`
  - `rpart`
  - `randomForest`

- **Shell tools**: `awk`, `grep`, `sort`, `uniq`, `head`, `tail`, `wc`, `cut`

---

## How to Run

1. Open the `.Rmd` file (if provided) or review the `.pdf` report.  
2. Install required packages in R:
   ```r
   install.packages(c("tidyverse", "rvest", "tidytext", "rpart", "randomForest"))

