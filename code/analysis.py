import pandas as pd  

file_path = "heart_disease.csv"

#  Define the correct column names for all 14 features
column_names = [
    "age",       # Age of the patient
    "sex",       # Sex (0 = Female, 1 = Male)
    "cp",        # Chest pain type (4 values)
    "trestbps",  # Resting blood pressure (in mm Hg)
    "chol",      # Serum cholesterol (mg/dl)
    "fbs",       # Fasting blood sugar > 120 mg/dl (1 = True, 0 = False)
    "restecg",   # Resting electrocardiographic results (0,1,2)
    "thalach",   # Maximum heart rate achieved
    "exang",     # Exercise-induced angina (1 = Yes, 0 = No)
    "oldpeak",   # ST depression induced by exercise relative to rest
    "slope",     # Slope of the peak exercise ST segment (0,1,2)
    "ca",        # Number of major vessels (0-3) colored by fluoroscopy
    "thal",      # Thalassemia type (3 = Normal, 6 = Fixed defect, 7 = Reversible defect)
    "target"     # Diagnosis of heart disease (0 = No, 1-4 = Yes)
]

#  Read the CSV file with correct delimiter
df = pd.read_csv(file_path, names=column_names, header=None, delimiter=",")

#  Convert all columns to numeric, forcing errors to NaN
df = df.apply(pd.to_numeric, errors='coerce')

#  Convert 'sex' column to categorical (Male/Female)
df["sex"] = df["sex"].replace({0: 'Female', 1: 'Male'}).astype("category")

#  Convert 'target' to binary classification (1 = disease, 0 = no disease)
df["target"] = df["target"].apply(lambda x: 1 if x > 0 else 0)

#  Fill missing values before converting to integer types
df["fbs"] = df["fbs"].fillna(df["fbs"].median()).astype(int)
df["thalach"] = df["thalach"].fillna(df["thalach"].median()).astype(int)
df["ca"] = df["ca"].fillna(df["ca"].median()).astype(int)
df["thal"] = df["thal"].fillna(df["thal"].median()).astype(int)
df = df[df["age"] <= 90]
#  Display final data types
print("Final Data Types:\n", df.dtypes)
df = df[df["age"] <= 90]
#  Display first few rows
print(df.head())


import matplotlib.pyplot as plt
import seaborn as sns

# Histogram of Age
plt.figure(figsize=(8, 5))
sns.histplot(df["age"], bins=20, kde=True)
plt.title("Age Distribution of Patients")
plt.xlabel("Age")
plt.ylabel("Count")
# plt.show()

# Histogram for Cholesterol
plt.figure(figsize=(8, 5))
sns.histplot(df["chol"], bins=20, kde=True)
plt.title("Cholesterol Level Distribution")
plt.xlabel("Cholesterol (mg/dl)")
plt.ylabel("Count")
#plt.show()

# Histogram for Maximum Heart Rate (Thalach)
plt.figure(figsize=(8, 5))
sns.histplot(df["thalach"], bins=20, kde=True)
plt.title("Maximum Heart Rate (Thalach) Distribution")
plt.xlabel("Thalach (bpm)")
plt.ylabel("Count")
plt.show()

# Check for missing values
missing_values = df.isnull().sum()
print("Missing Values per Column:\n", missing_values)

# Compute correlation matrix
correlation_matrix = df.corr()

# Plot heatmap of correlations
# plt.figure(figsize=(12, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
# plt.title("Correlation Heatmap of Features")
#plt.show()



# Plot Age Distribution by Heart Disease Presence
plt.figure(figsize=(8, 5))
ax = sns.histplot(data=df, x="age", hue="target", bins=20, kde=True, alpha=0.6)

# Manually set legend labels (0 = No Disease, 1 = Heart Disease)
handles, labels = ax.get_legend_handles_labels()
plt.legend(handles, ["No Disease", "Heart Disease"], title="Heart Disease")

plt.title("Corrected Age Distribution by Heart Disease Presence")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

print(df["age"].describe())  # Check min, max, mean values
print("Unique age values:", df["age"].unique())

