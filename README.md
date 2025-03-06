# Heart Disease Prediction – Data Analysis & Machine Learning
## Understanding Heart Disease Through Data 
This project explores the Heart Disease dataset from the UCI Machine Learning Repository to analyze risk factors associated with heart disease. The goal is to use data analysis and machine learning techniques to predict whether a patient has heart disease based on their medical attributes.

---

##  Project Overview
Cardiovascular diseases are one of the leading causes of death worldwide. Early detection and prevention are key to reducing mortality rates. This project aims to analyze patient data and build a predictive model for heart disease diagnosis.

### **Key Objectives:**
- Perform **exploratory data analysis (EDA)** to uncover trends in heart disease risk factors.
- Apply **data preprocessing** to clean and prepare the dataset.
- Use **machine learning models** to predict the presence of heart disease.
- Visualize insights using **Python, Power BI**.

---

##  Dataset Information
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/45/heart+disease)  
- **Instances:** 303 patients  
- **Features:** 14 clinical and diagnostic attributes  
- **Target Variable:**  
  - `0` = No heart disease  
  - `1-4` = Presence of heart disease (grouped into `1` for prediction)

### 🏥 Feature Description
| Feature     | Description |
|------------|-------------|
| `age`      | Age of the patient |
| `sex`      | Sex (0 = Female, 1 = Male) |
| `cp`       | Chest pain type (1 = Typical angina, 2 = Atypical angina, 3 = Non-anginal pain, 4 = Asymptomatic) |
| `trestbps` | Resting blood pressure (mm Hg) |
| `chol`     | Serum cholesterol (mg/dl) |
| `fbs`      | Fasting blood sugar > 120 mg/dl (1 = True, 0 = False) |
| `restecg`  | Resting electrocardiographic results (0 = Normal, 1 = ST-T wave abnormality, 2 = Left ventricular hypertrophy) |
| `thalach`  | Maximum heart rate achieved |
| `exang`    | Exercise-induced angina (1 = Yes, 0 = No) |
| `oldpeak`  | ST depression induced by exercise |
| `slope`    | Slope of the peak exercise ST segment (0 = Upsloping, 1 = Flat, 2 = Downsloping) |
| `ca`       | Number of major vessels (0-3) colored by fluoroscopy |
| `thal`     | Thalassemia type (3 = Normal, 6 = Fixed defect, 7 = Reversible defect) |
| `target`   | Presence of heart disease (0 = No, 1 = Yes) |

---

## 📂 Project Structure
```bash
/heart-disease-analysis
    ├── data/               # Dataset files
    ├── notebooks/          # Jupyter Notebooks for analysis
    ├── models/             # Machine Learning models
    ├── dashboards/         # Power BI/Tableau visualizations
    ├── sql_queries/        # SQL queries for data analysis
    ├── README.md           # Project documentation
