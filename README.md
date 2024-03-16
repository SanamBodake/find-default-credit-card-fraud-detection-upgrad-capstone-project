# FindDefault (Prediction of Credit Card fraud) - Capstone Project

## Problem Statement:
 A credit card is one of the most used financial products to make online purchases and payments. Though the Credit cards can be a convenient way to manage your finances, they can also be risky. Credit card fraud is the unauthorized use of someone else's credit card or credit card information to make purchases or withdraw cash. It is important that credit card companies are able to recognize fraudulent credit card transactions so that customers are not charged for items that they did not purchase.

## About Credit Card Fraud Detection:
- **What is credit card fraud detection?**

  Credit card fraud detection is the collective term for the policies, tools, methodologies, and practices that credit card companies and financial institutions take to combat identity fraud and stop fraudulent transactions.  

  In recent years, as the amount of data has exploded and the number of payment card transactions has skyrocketed, credit fraud detection has become largely digitized and automated. Most modern solutions leverage artificial intelligence (AI) and machine learning (ML) to manage data analysis, predictive modeling, decision-making, fraud alerts and remediation activity that occur when individual instances of credit card fraud are detected.  

- **Anomaly detection**

  Anomaly detection is the process of analyzing massive amounts of data points from both internal and external sources to produce a framework of “normal” activity for each individual user and establish regular patterns in their activity.

  Data used to create the user profile includes:

  - Purchase history and other historical data
  - Location
  - Device ID
  - IP address
  - Payment amount
  - Transaction information

  When a transaction falls outside the scope of normal activity, the anomaly detection tool will then alert the card issuer and, in some cases, the user. Depending on the transaction details and risk score assigned to the action, these fraud detection systems may flag the purchase for review or put a hold on the transaction until the user verifies their activity.

- **What can be an anomaly?**
  - A sudden increase in spending
  - Purchase of a large ticket item
  - A series of rapid transactions
  - Multiple transactions with the same merchant
  - Transactions that originate in an unusual location or foreign country
  - Transactions that occur at unusual times

  If the anomaly detection tool leverages ML, the models can also be self-learning, meaning that they will constantly gather and analyze new data to update the existing model and provide a more precise scope of acceptable activity for the user.

 
## Project Introduction: 
The dataset contains transactions made by credit cards in September 2013 by European cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions. 

In this Project, we have to build a classification model to predict whether a transaction is fraudulent or not. We will use various predictive models to see how accurate they are in detecting whether a transaction is a normal payment or a fraud. Let's start!

## Project Outline:
- **Exploratory Data Analysis:** Analysing and understanding the data to identify patterns, relationships, and trends in the data by using Descriptive Statistics and Visualizations.
- **Data Cleaning:** Checking for the data quality, handling the missing values and outliers in the data.
- **Dealing with Imbalanced data:** This data set is highly imbalanced. The data should be balanced using the appropriate Resampling Techniques (NearMiss Undersampling, SMOTETomek) before moving onto model building.
- **Feature Engineering:** Transforming the existing features for better performance of the ML Models. 
- **Model Training:** Splitting the data into train & test sets and use the train set to estimate the best model parameters.
- **Model Validation:** Evaluating the performance of the models on data that was not used during the training process. The goal is to estimate the model's ability to generalize to new, unseen data and to identify any issues with the model, such as overfitting.
- **Model Selection:** Choosing the most appropriate model that can be used for this project.
- **Model Deployment:** Model deployment is the process of making a trained machine learning model available for use in a production environment.

## Project Assets Overview:
- [data](https://github.com/SanamBodake/find-default-credit-card-fraud-detection-upgrad-capstone-project/tree/main/data):

  This folder contains the dataset(s) used in the project. Includes raw.csv file along with a README file explaining the dataset's attributes. The 'preprocessed_data.csv' and 'resampled_os.csv' data files have been excluded from the repository by adding them to the .gitignore file due to their large file sizes.
