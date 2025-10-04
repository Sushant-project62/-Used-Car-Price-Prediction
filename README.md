# 🚗 Used Car Price Prediction

A machine learning web application that predicts the selling price of a used car based on its features like company, model, year, kilometers driven, and fuel type.

## 📌 Project Overview

This project applies **data preprocessing, machine learning, and deployment using Flask** to create a web app where users can input car details and get an estimated price instantly.

## ⚙️ Tools & Technologies

* Python (Pandas, NumPy, Scikit-learn, Pickle)
* Flask (for deployment)
* HTML, CSS, Bootstrap (frontend)
* Jupyter Notebook (model training & analysis)

## 📂 Dataset Features

| Column       | Description                           |
| ------------ | ------------------------------------- |
| `Name`       | Car model name                        |
| `Company`    | Brand of the car                      |
| `Year`       | Manufacturing year                    |
| `Price`      | Price of the car (target variable)    |
| `Kms_driven` | Kilometers driven by the car          |
| `Fuel_type`  | Type of fuel used (Petrol/Diesel/CNG) |

## 🧠 Machine Learning Workflow

1. Data Cleaning & Preprocessing
2. Feature Engineering
3. Model Training (Regression)
4. Model Saving using Pickle
5. Flask-based Web Application

## 💻 How to Run the Project

1. Clone the repository

   ```bash
   git clone https://github.com/<your-username>/used-car-price-prediction.git
   cd used-car-price-prediction
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Run Flask app

   ```bash
   python application.py
   ```

4. Open in browser

   ```
   http://127.0.0.1:5000/
   ```

## 🌐 Web Application Features

* Select company, model, year, fuel type
* Enter kilometers driven
* Predict the resale value of the car

![UI Screenshot](screenshot.png)

## 📊 Sample Prediction

Input: Maruti Suzuki Swift, 2019, 100 kms, Petrol
Output: ₹4,50,000 (approx.)

## 📜 Conclusion

This project demonstrates how **machine learning can be applied to real-world pricing problems**. It highlights skills in **data analysis, model deployment, and full-stack integration**.

---

👨‍💻 **Author:** Sushant Kishan Rathod
📧 Contact: [sushanrathod6288@gmail.com]
🔗 GitHub: [https://github.com/Sushant-project62]
