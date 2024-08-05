# Customer-Churn-Prediction-Project

### Project Overview
 The goal of this project is to analyze how different factors, such as gender, partner status, dependents, tenure, account details, and services, influence customer churn. The objective is to develop a predictive model to identify customers at risk of churning and manage the data using SQL.

### Dataset Description
The dataset includes the following features:

- customerID: Unique identifier for each customer.
- gender: Gender of the customer (Male, Female).
- SeniorCitizen: Indicates if the customer is a senior citizen (0: No, 1: Yes).
- Partner: Indicates if the customer has a partner (Yes, No).
- Dependents: Indicates if the customer has dependents (Yes, No).
- tenure: Number of months the customer has stayed with the company.
- PhoneService: Indicates if the customer has phone service (Yes, No).
- MultipleLines: Indicates if the customer has multiple lines (Yes, No, No phone service).
- InternetService: Indicates the type of internet service (DSL, Fiber optic, No).
- OnlineSecurity: Indicates if the customer has online security service (Yes, No, No internet service).
- DeviceProtection: Indicates if the customer has device protection service (Yes, No, No internet service).
- TechSupport: Indicates if the customer has tech support service (Yes, No, No internet service).
- StreamingTV: Indicates if the customer has streaming TV service (Yes, No, No internet service).
- StreamingMovies: Indicates if the customer has streaming movies service (Yes, No, No internet service).
- Contract: Indicates the contract term (Month-to-month, One year, Two year).
- PaperlessBilling: Indicates if the customer uses paperless billing (Yes, No).
- PaymentMethod: Indicates the payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic)).
- MonthlyCharges: Monthly charges for the customer.
- TotalCharges: Total charges for the customer.
- Churn: Indicates if the customer churned (Yes, No).
  
### Project Steps
## Data Exploration: 
Understanding the dataset, checking for missing values, and performing exploratory data analysis (EDA) to identify patterns and correlations.
## Data Preprocessing: 
Handling missing values, encoding categorical variables, normalizing numerical variables, and splitting the dataset into training and testing sets.
## Feature Engineering: 
Creating new features or modifying existing ones to improve the performance of the predictive model.
## Model Development: 
Developing various machine learning models to predict customer churn, such as Logistic Regression, Random Forest, and Gradient Boosting.
## Model Evaluation:
Evaluating the performance of the models using metrics such as accuracy, precision, recall, F1-score, and ROC-AUC.
## Model Deployment: 
Deploying the best model for practical use, allowing the identification of customers at risk of churning.
## Data Management: 
Managing and querying the data using SQL for efficient handling and analysis.

### Tools and Technologies
#### Programming Languages: Python
#### Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
#### Database: SQL
#### Environment: Jupyter Notebook

## License
This project is licensed under the MIT License - see the LICENSE file for details.
