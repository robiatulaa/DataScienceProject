# Google Maps Reviews – Data Wrangling & Text Mining

This project demonstrates how to transform raw, semi-structured reviews from Google Maps into structured insights using **Python**.  
It covers the full pipeline of **data wrangling, cleaning, and text mining**, producing structured datasets and sparse representations ready for downstream machine learning tasks.

---

## Project Overview

- **Task 1 – Data Wrangling**  
  - Parsed raw review data from mixed sources (text files + Excel metadata).  
  - Extracted attributes such as user IDs, timestamps, ratings, review text, responses, and picture details.  
  - Standardized dates, cleaned text (lowercasing, emoji removal, handling missing values).  
  - Produced structured outputs:
    - **`task1_008.csv`** → Aggregated summary per location.  
    - **`task1_008.json`** → Detailed review dataset.

- **Task 2 – Text Mining**  
  - Filtered businesses with sufficient review volume (≥ 70).  
  - Preprocessed English text (tokenization, stopword removal, stemming).  
  - Built vocabulary of unigrams and top 200 bigrams using PMI.  
  - Generated sparse count-vector representations for ML.  
  - Produced outputs:
    - **`008_vocab.txt`** → Vocabulary with frequencies.  
    - **`008_countvec.txt`** → Sparse matrix (reviews × terms).  

---

## Tech Stack

- **Language:** Python 3.10  
- **Libraries:** `pandas`, `nltk`, `langid`, `json`, `re`  
- **Skills Demonstrated:**  
  - Data wrangling & preprocessing  
  - Text mining & feature engineering  
  - Working with semi-structured data (CSV, JSON, text files)  
  - Sparse matrix construction for ML pipelines  
