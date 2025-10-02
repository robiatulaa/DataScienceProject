# Amazon Product Recommender System

This project builds a **recommender system** for Amazon products using collaborative filtering.  
Several models were tested, including **KNN**, **NMF**, and **SVD**, with SVD achieving the best performance.

## Overview

- **Dataset**: Amazon product ratings (user–item interactions)  
- **Goal**: Predict ratings for unseen products  
- **Methods**:  
  - K-Nearest Neighbors (KNN)  
  - Non-negative Matrix Factorization (NMF)  
  - Singular Value Decomposition (SVD)  
- **Evaluation**: RMSE and MAE  

## Results

- **SVD** provided the highest accuracy with RMSE **0.8759**  
- Hyperparameter tuning further improved performance  
- Final model achieved a **top 2 Kaggle leaderboard ranking**

## Tech Stack

- Python  
- pandas, numpy  
- scikit-learn  
- surprise  
- matplotlib, seaborn  

## How to Run

```bash
git clone https://github.com/yourusername/amazon-recommender-system.git
cd amazon-recommender-system
pip install -r requirements.txt
jupyter notebook code_34269193.ipynb
