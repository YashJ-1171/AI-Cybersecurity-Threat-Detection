# 🛡️ AI-Powered Cybersecurity Threat Detection System

## 📌 Project Overview
Traditional rule-based security systems struggle to detect zero-day cyber threats. This project implements a Machine Learning-based Network Intrusion Detection System (NIDS) designed to analyze network traffic patterns and classify them as normal or malicious (e.g., DoS, Brute Force).

## 🎯 Problem Statement & Industry Relevance
In a modern Security Operations Center (SOC), analysts face "alert fatigue" from thousands of false positives. By applying AI/ML, this project demonstrates how to automate threat identification, improving precision and reducing response times—a critical requirement for fintech, cloud, and product-based IT infrastructures.

## ⚙️ Tech Stack
* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Random Forest Classifier)
* **Visualization:** Matplotlib, Seaborn

## 🧠 System Architecture
1. **Data Ingestion:** Simulated network flow logs (duration, bytes, protocols, login attempts).
2. **Preprocessing:** Label encoding and StandardScaler normalization.
3. **ML Engine:** Random Forest ensemble learning for binary classification (Normal vs. Attack).
4. **SOC Reporting:** Automated generation of Confusion Matrices and Feature Importance charts.

## 🚀 Installation & Usage
1. Clone the repository: `git clone https://github.com/yourusername/AI-Cybersecurity-Threat-Detection.git`
2. Navigate to directory: `cd AI-Cybersecurity-Threat-Detection`
3. Create virtual environment: `python -m venv venv`
4. Activate it and install dependencies: `pip install -r requirements.txt`
5. Run the pipeline: `python main.py`

## 📊 Results & Evaluation
* Achieved high accuracy and F1-score in distinguishing attack vectors.
* **Feature Importance:** Discovered that `failed_logins` and `src_bytes` are the strongest indicators of malicious activity.

## 📸 Project Screenshots

### 1. Model Evaluation: Confusion Matrix
![Confusion Matrix](images/confusion_matrix.png)
*This matrix shows the model's high precision in distinguishing between normal network traffic and malicious attacks.*

### 2. Threat Detection: Feature Importance
![Feature Importance](images/feature_importance.png)
*Analysis indicating which network behaviors (e.g., failed logins, massive data transfers) are the strongest indicators of a cyber attack.*

### 3. Execution Log & Classification Report
![CSV file](images/terminal_output.png)
*End-to-end pipeline execution showing 99%+ accuracy and detailed precision/recall scores for threat identification.*

## 4. Terminal Output
![Terminal Output](images/terminal_output)