# Financial Fraud Detection Project

This project is aimed at developing a machine learning model to identify fraudulent financial transactions accurately and efficiently. The dataset utilized is derived from the PaySim1 dataset, which contains information about various types of transactions. The primary objective is to build a reliable model that can detect fraudulent activities while minimizing false positive rates.

## Project Overview

### 1. Data Exploration and Feature Engineering
   - The project began with an in-depth analysis of the dataset to identify key features that could contribute to fraud detection. Critical attributes such as transaction amount, transaction type, and account balance changes were examined.
   - To enhance the dataset, additional features were engineered. These include balance ratios, transaction differences, and ratios comparing transaction amounts to account balances, all designed to improve the model's sensitivity to fraudulent behavior.

### 2. Model Development and Optimization
   - The dataset was divided into training and testing sets to ensure that the model’s performance could be rigorously evaluated.
   - Various machine learning models were explored, with a particular focus on the Naive Bayes classifier. Hyperparameter tuning was performed using `GridSearchCV` to optimize the model’s configuration, ensuring robust performance.
   - The final model was selected based on its accuracy, precision, recall, and ROC AUC score. The model was further fine-tuned to achieve the best balance between identifying fraudulent transactions and minimizing false positives.

### 3. Implementation in Jupyter Notebook
   - The Jupyter Notebook was structured to present a clear and concise workflow:
     - **Configuration Settings**: Defined for model training and evaluation, ensuring reproducibility.
     - **Modular Code Design**: Functions were developed for data preprocessing, model training, and evaluation to maintain clarity and scalability.
     - **Evaluation Metrics**: Key metrics such as ROC AUC score, confusion matrices, and classification reports were logged to monitor performance.
     - **Visualizations**: Graphical representations, including plots and confusion matrices, were integrated to provide visual insights into model performance.

### 4. Deployment via Streamlit Application
   - A professional, interactive Streamlit application was developed to allow real-time fraud detection based on user-uploaded data.
   - **Application Features**:
     - Users can upload transaction datasets in CSV format, and the app processes and visualizes the data.
     - The application displays key insights such as transaction type distributions and transaction values over time, offering an interactive user experience.
     - The trained model predicts fraudulent transactions in the uploaded dataset, presenting flagged entries in a well-organized table format.
     - Advanced visualizations using Plotly provide detailed analysis of flagged transactions, enhancing the interpretability of results.
   - The application was styled with custom CSS and designed with a clean and intuitive interface, demonstrating a professional approach to deploying machine learning models.

## Conclusion

We successfully build and deploying a machine learning solution for financial fraud detection. The model and application are designed to provide financial institutions with a reliable tool for monitoring transactions, ensuring the security and integrity of financial systems.