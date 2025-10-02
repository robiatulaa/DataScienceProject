# Property Data Transformation for Predictive Modeling

This project focuses on preparing suburb-level property data for predictive modeling.  
The goal is to apply a variety of data transformation techniques to ensure features are on similar scales, reduce skewness, and strengthen linear relationships with the target variable (median_house_price).

## Project Overview

- Dataset Features:
  - number_of_houses
  - number_of_units
  - population
  - aus_born_perc
  - median_income
  - median_house_price (target)

- Objective:  
  Transform raw features into formats suitable for linear regression models by addressing:
  - Skewed distributions  
  - Inconsistent feature scales  
  - Weak feature–target relationships  

## Techniques Applied

- Standardization (Z-score) – normalize feature means and variances  
- Min–Max Scaling – rescale variables into a [0,1] range  
- Log Transformation – reduce right-skewed distributions  
- Power Transformation (Box-Cox / Yeo-Johnson) – stabilize variance and improve normality  
- Correlation Analysis – assess improvements in linear relationships with the target variable  

## Outcomes

- Features with reduced skewness  
- Comparable feature scales for fairer model training  
- Stronger correlations between predictors and the target (median_house_price)  
- A dataset ready for predictive modeling with linear regression  

## Tech Stack

- Language: Python (Jupyter Notebook)  
- Libraries:  
  - pandas – data manipulation  
  - numpy – numerical computations  
  - scikit-learn – preprocessing and transformations  
  - matplotlib, seaborn – visualization  
   cd property-data-transformation

