# 🩺 Diabetes Risk Prediction System
An AI-powered healthcare web application built with Streamlit to predict diabetes risk using patient health indicators.
The system provides both a risk category and a probability-based risk score with an interactive visual interface.

## 🚀 Features
- 🧠 Machine Learning–based diabetes risk prediction
- 📊 Probability-driven risk assessment with visual risk bar
- 🎨 Modern healthcare-themed UI with animations
- ⚡ Real-time prediction using trained ML model
- 📱 Responsive and clean Streamlit layout

## 🧠 How It Works
- The application takes key patient health inputs such as glucose level, BMI, blood pressure, insulin, age, and medical history.
- A trained classification model processes this data and:
     #### Predicts diabetes risk (Low / Moderate / High)
     #### Outputs a probability score visualized through an interactive risk bar
The entire pipeline runs locally with no external API dependency.

## Tech Stack
- Python 3.x
- Streamlit
- NumPy
- Scikit-learn
- Joblib
- Custom CSS (Healthcare UI & animations)

## 📦 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/diabetes-risk-prediction.git
cd diabetes-risk-prediction
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
```

### 3️⃣ Activate the environment
#### Windows
```bash
venv\Scripts\activate
```
#### Mac/Linux
```bash
source venv/bin/activate
```

### 4️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Run the app
```bash
streamlit run app.py
```

## 📁 Project Structure
```bash
├── app.py                         # Streamlit frontend
├── best_diabetes_model.joblib     # Trained ML model
├── Diabetes Prediction.ipynb      # Model training notebook
├── requirements.txt               # Dependencies
└── README.md
```

## 📊 Dataset
- Available on Kaggle : https://www.kaggle.com/datasets/shahnawaj9/diabetes-database

## 🌐 Live Demo
https://diabetesriskanalyzer.streamlit.app/

## 📸 Screenshots
![img alt](https://github.com/nikhil-kumarrr/images/blob/main/Screenshot%202026-01-01%20153038.png?raw=true)
![img alt](https://github.com/nikhil-kumarrr/images/blob/main/Screenshot%202026-01-01%20153430.png?raw=true)
