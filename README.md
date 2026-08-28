Social Network Ads Purchase Prediction

Project Overview

This project uses Machine Learning to predict whether a person will
purchase a product after seeing a social network advertisement.

The prediction is based on: - Age - Estimated Salary

The target variable is:- 
Purchased = 0 → Did not purchase
Purchased = 1 → Purchased

Machine Learning Models

The following classification algorithms were tested:

Logistic Regression

K-Nearest Neighbors (KNN)

Decision Tree Classifier

Random Forest Classifier

Model Results

Model                 Parameters              Accuracy

Logistic Regression   Default                 91.25%
K-Nearest Neighbors   n_neighbors=10          83.75%
Decision Tree         random_state=10         91.25%
Random Forest         random_state=20         93.75%

Best Model

Random Forest Classifier achieved the highest accuracy of 93.75%
on the test dataset.

Project Workflow

Dataset
   ↓
Data Understanding
   ↓
Data Visualization / EDA
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Prediction
   ↓
Model Evaluation
   ↓
Model Comparison
   ↓
Best Model Selection

Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

Jupyter Notebook

Dataset

The project uses the Social_Network_Ads.csv dataset.

Main features: - Age - Estimated Salary

Target: - Purchased

Conclusion

Four classification models were compared. Random Forest performed best
with 93.75% accuracy, followed by Logistic Regression and Decision
Tree with 91.25%, while KNN achieved 83.75%.

Future Improvements

Add feature scaling and compare results where appropriate

Perform hyperparameter tuning

Build a Streamlit web application

Deploy the application online
