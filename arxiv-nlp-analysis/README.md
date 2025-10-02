# Text Classification and Topic Modelling on arXiv Articles

This project applies both **supervised** and **unsupervised** Natural Language Processing (NLP) techniques on research articles sourced from **arXiv.org** (2016–2024).  
It demonstrates end-to-end workflows for text classification and topic modelling.

## Project Overview

### Part 1 – Text Classification
- **Objective**: Classify articles as *Computational Linguistics (CL)* or *non-CL*.  
- **Methods**:
  - Logistic Regression with TF-IDF features
  - Recurrent Neural Network (RNN) with PyTorch  
- **Experiments**:
  - Dataset size: 1000 samples vs. full dataset  
  - Text length: titles vs. abstracts  
- **Findings**:
  - Logistic Regression outperformed RNN in accuracy, precision, recall, and F1-score  
  - Larger datasets significantly improved performance  
  - Abstracts yielded better results than titles due to richer context  

### Part 2 – Topic Modelling
- **Objective**: Discover latent themes from article abstracts.  
- **Method**: Latent Dirichlet Allocation (LDA)  
- **Experiments**:
  - Dataset size: 1000 vs. 20,000 articles  
  - Representation: Unigrams vs. Bigrams  
- **Findings**:
  - Larger datasets and bigram representation produced more coherent and interpretable topics  
  - Smaller datasets led to overlapping topics, while larger datasets captured more distinct themes  

## Techniques and Tools

- **Text Preprocessing**: Tokenization, lemmatization, duplicate removal  
- **Classification**:
  - Logistic Regression (scikit-learn)
  - RNN (PyTorch, Torchtext)  
- **Topic Modelling**: LDA (gensim, pyLDAvis)  
- **Visualization**: Precision–Recall curves, topic clusters  

## Outcomes

- Implemented supervised and unsupervised NLP pipelines  
- Demonstrated the effect of dataset size and representation on model performance  
- Produced coherent and meaningful topic models from large-scale text data  

## Tech Stack

- Python 3.10 
- Libraries:
  - `pandas`, `numpy`  
  - `scikit-learn`  
  - `nltk`, `spacy`  
  - `torch`, `torchtext`  
  - `gensim`, `pyLDAvis`  
  - `matplotlib`, `seaborn`  

## How to Run

Clone the repository, install the dependencies, and run the notebook:

```bash
git clone https://github.com/yourusername/arxiv-nlp-analysis.git
cd arxiv-nlp-analysis
pip install -r requirements.txt
jupyter notebook code_34269193.ipynb
