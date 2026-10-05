\# Real-Time E-Commerce Data Science Project



\## 📌 Project Overview



This project focuses on building an end-to-end \*\*E-Commerce Data Science solution\*\* covering data collection, data cleaning, exploratory data analysis, business intelligence, SQL analysis, feature engineering, and demand prediction.



The project combines \*\*real-world e-commerce product data\*\* with an \*\*online retail transaction dataset\*\* to understand product performance, inventory-related business problems, and demand patterns.



\---



\## 🎯 Business Problem



E-commerce businesses need to answer important questions such as:



\* Which products and categories perform well?

\* Which products have inventory risk?

\* How does price influence product demand and inventory?

\* Where are stock-related business risks concentrated?

\* Can historical sales data be used to predict product demand?

\* How can demand predictions support inventory-related decisions?



The objective is to convert raw e-commerce data into \*\*actionable business insights\*\* and develop a practical demand prediction workflow.



\---



\## 🎯 Project Objectives



\* Collect and validate e-commerce product data using an API.

\* Clean and validate raw datasets.

\* Perform Exploratory Data Analysis (EDA).

\* Identify important business patterns and risks.

\* Perform SQL-based business analysis.

\* Create business-focused features.

\* Build a demand prediction model using historical transaction data.

\* Compare actual demand with predicted demand.

\* Analyze prediction errors and high-demand spikes.

\* Translate model results into business and inventory insights.



\---



\## 🔄 Data Science Workflow



```text

Data Collection

&#x20;     ↓

Data Cleaning \& Validation

&#x20;     ↓

Exploratory Data Analysis

&#x20;     ↓

Business Analysis

&#x20;     ↓

Feature Engineering

&#x20;     ↓

SQL Analysis

&#x20;     ↓

Demand Dataset Preparation

&#x20;     ↓

Demand Prediction

&#x20;     ↓

Actual vs Predicted Analysis

&#x20;     ↓

Error Analysis

&#x20;     ↓

High-Demand Spike Investigation

&#x20;     ↓

Business Interpretation

&#x20;     ↓

Inventory Business Logic

```



\---



\## 📊 Data Sources



\### 1. E-Commerce Product API Dataset



The API dataset was used for:



\* Product-level analysis

\* Category analysis

\* Price and discount analysis

\* Stock analysis

\* Inventory value analysis

\* Brand validation

\* Stock-risk analysis

\* SQL business analysis



\### 2. Online Retail Transaction Dataset



The transaction dataset was used for demand prediction because it contains historical sales information.



Important fields include:



\* `InvoiceNo`

\* `StockCode`

\* `Description`

\* `Quantity`

\* `InvoiceDate`

\* `UnitPrice`

\* `CustomerID`

\* `Country`



Historical transaction data was transformed into a daily product-level demand dataset for prediction.



\---



\## 🧹 Data Cleaning \& Validation



The project included validation of:



\* Missing values

\* Duplicate records

\* Negative quantities

\* Cancellation transactions

\* Product-level sales records

\* Invalid transaction patterns

\* Stock and availability inconsistencies



The cleaned transaction dataset was then used for downstream demand analysis.



\---



\## 📈 Exploratory \& Business Analysis



The analysis covered:



\* Product price distribution

\* Discount distribution

\* Stock distribution

\* Category-level performance

\* Rating distribution

\* Price vs stock relationships

\* Stock-risk analysis

\* Inventory value analysis

\* Brand completeness

\* Availability status

\* Category-level business patterns



The focus was not only on statistical analysis but also on identifying \*\*business meaning behind the patterns\*\*.



\---



\## 🧮 Feature Engineering



Business-oriented features were created from the product data, including:



\* `discount\_amount`

\* `discounted\_price`

\* `inventory\_value`

\* `total\_inventory\_value`

\* `is\_low\_stock`

\* `is\_out\_of\_stock`

\* `stock\_level`



These features were designed to support business and inventory analysis.



\---



\## 🗄️ SQL Business Analysis



SQL was used to analyze the e-commerce product data.



Topics covered include:



\* SELECT

\* WHERE

\* AND / OR

\* IN

\* ORDER BY

\* LIMIT

\* GROUP BY

\* HAVING

\* Aggregate functions

\* Stock-risk analysis

\* Business segment analysis

\* Window functions

\* Category ranking

\* Inventory concentration

\* Stock-risk inventory exposure

\* MOQ analysis



The SQL analysis was used to move from raw data toward \*\*business decision support\*\*.



\---



\## 🤖 Demand Prediction



The API product dataset did not contain a reliable historical demand signal suitable for demand forecasting.



Therefore, the Online Retail transaction dataset was used for the machine learning demand prediction stage.



The transaction data was aggregated into \*\*daily product-level demand\*\* using:



\* Product identifier

\* Transaction date

\* Quantity sold



The resulting demand dataset contained historical sales patterns across thousands of product-days.



\---



\## 📊 Model Evaluation \& Error Analysis



The demand prediction workflow included:



\* Actual vs Predicted Demand analysis

\* Prediction error analysis

\* High-demand spike investigation

\* Business interpretation of prediction results



The objective was not only to evaluate model performance but also to understand \*\*where and why prediction errors occur\*\*.



\---



\## 📦 Inventory Business Logic



The final stage connects demand prediction with inventory decision-making.



The project intentionally does \*\*not invent current stock or lead-time values\*\* because these fields are not available in the demand dataset.



Instead, the prediction results are used as a foundation for future inventory decision logic when real operational fields such as:



\* Current Stock

\* Lead Time

\* Reorder Point

\* Safety Stock



become available.



\---



\## 🛠️ Technologies Used



\* Python

\* Pandas

\* NumPy

\* Matplotlib

\* Scikit-learn

\* Jupyter Notebook

\* SQL

\* SQLite

\* Git

\* GitHub



\---



\## 📁 Project Structure



```text

Real-Time-Ecommerce-Data-Science-Project/

│

├── notebooks/

│   ├── 01\_data\_collection.ipynb

│   └── Untitled.ipynb

│

├── Project\_Notes.txt

├── Project\_Roadmap.txt

├── Total-Business-Problem.docx

├── Screenshot 2026-09-15 080403.png

├── bisiness.txt

├── .gitignore

└── README.md

```



> Raw datasets and database files are excluded from GitHub using `.gitignore`.



\---



\## 🚀 Future Improvements



Potential production-level improvements include:



\* Adding real-time sales data

\* Adding current inventory data

\* Incorporating supplier lead time

\* Developing reorder-point calculations

\* Adding safety-stock optimization

\* Building an interactive dashboard

\* Deploying the prediction pipeline as an API

\* Automating model retraining

\* Monitoring model performance in production



\---



\## 👨‍💻 Project Focus



This project is designed to demonstrate an end-to-end \*\*Data Scientist thinking process\*\*:



\*\*Business Problem → Data → Validation → Analysis → Features → SQL → Prediction → Error Analysis → Business Decision\*\*



The emphasis is on connecting technical analysis with real-world business decisions rather than simply building a machine learning model.



