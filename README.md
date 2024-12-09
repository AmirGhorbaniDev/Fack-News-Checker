### Fake News Detection System
A machine learning-based system that detects fake news using article titles. Built with Python, scikit-learn, and Streamlit.
---
## Overview
This project implements a fake news detection system using TF-IDF vectorization and Logistic Regression. The model is trained on over 40,000 news articles and deployed as a web application using Streamlit.
---
## Project Structure

Fack-News-Checker/
│
├── Dataset/
│   ├── evaluation.csv
│   ├── test (1).csv
│   └── train (2).csv
│
├── .venv/
├── app.py
├── fake_news_model.joblib
├── tfidf_vectorizer.joblib
├── Model.ipynb
└── requirements.txt
---
## Dataset Information

Total articles: ~45,000
Training set: 24,352 articles
Test set: 8,117 articles
Evaluation set: 8,117 articles
Features: article title, text content
Labels: Real (1) or Fake (0)

## Technologies Used

Python 3.x
scikit-learn
Streamlit
Pandas
Plotly
Joblib
---
## Installation & Setup

###Clone the repository

git clone https://github.com/yourusername/Fack-News-Checker.git
cd Fack-News-Checker

Create and activate virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

### Install required packages

pip install -r requirements.txt

---

## Usage

Run the Streamlit dashboard

Open the provided localhost URL in your browser
Enter a news title in the text area
Click "Predict" to get the classification result

### Model Details

Feature extraction: TF-IDF Vectorization
Algorithm: Logistic Regression
Input: News titles
Output: Binary classification (Fake/Real) with confidence score

### Features

Real-time prediction of news authenticity
Confidence score for predictions
Interactive visualization of results
User-friendly web interface
Responsive design

### File Descriptions

app.py: Streamlit dashboard implementation
fake_news_model.joblib: Trained model file
tfidf_vectorizer.joblib: Fitted TF-IDF vectorizer
Model.ipynb: Model development notebook
requirements.txt: Required Python packages
Dataset/: Contains training and evaluation data
---

## Requirements
streamlit
pandas
scikit-learn
plotly
joblib

---
## Future Improvements

Implement advanced NLP techniques
Add support for multiple languages
Include URL-based news verification
Enhance visualization capabilities
Add model performance metrics dashboard

## Contributing

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

## Acknowledgments

Dataset sources from Kaggle
Streamlit for the awesome framework
scikit-learn for machine learning tools

