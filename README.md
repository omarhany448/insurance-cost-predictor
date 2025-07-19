🏥 Insurance Cost Predictor
A complete end-to-end machine learning project that predicts a person’s medical insurance cost based on key features like age, BMI, smoking status, number of children, and region.

🔍 Overview
This project aims to demonstrate the full ML pipeline — from data preprocessing and model training to deploying a live web app.
Users can input their personal data and instantly get a predicted insurance cost through a Gradio interface hosted on Hugging Face.

📊 Dataset
Source: Kaggle Insurance Dataset

1,300+ entries with the following features:

age, sex, bmi, children, smoker, region, charges

📈 ML Workflow
Data Cleaning & Preprocessing

Checked for null values

Encoded categorical variables

Feature scaling for numeric columns

Exploratory Data Analysis (EDA)

Visualizations to understand correlations

Insights: Smoking and BMI have the most impact on charges

Modeling

Used XGBoost Regressor for high accuracy

Achieved strong performance on the test set

Saving Model

Trained model exported using joblib as model.pkl

Web App Deployment

Built using Gradio

Hosted live on Hugging Face Spaces

🚀 Live Demo
👉 Try it Live on Hugging Face

🧠 Technologies Used
Python

Pandas, NumPy

Scikit-learn, XGBoost

Matplotlib, Seaborn

Gradio

Hugging Face Spaces

Git, GitHub

📁 Folder Structure
Copy
Edit
insurance_cost_predictor/
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
✍️ Author
Omar Hany
LinkedIn | GitHub
