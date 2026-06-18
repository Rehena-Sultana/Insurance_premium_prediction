# Insurance Premium Category Predictor

A machine learning web application that predicts insurance premium categories based on user details. Built with **FastAPI** (backend) and **Streamlit** (frontend).

---

## Project Overview

This application takes user information such as age, weight, height, income, smoking status, city, and occupation, and predicts which insurance premium category they fall into using a trained Random Forest model.

---

##  Project Structure

```
INSURANCE_PREMIUM_PRED/
    ├── config/
    │     └── city_tier.py              # City tier classification
    ├── model/
    │     ├── predict.py                # Prediction logic
    │     └── randomforest_model.pkl    # Trained ML model
    ├── schema/
    │     ├── prediction_response.py    # Response schema
    │     └── user_input_pydantic.py    # Input validation schema
    ├── app.py                          # FastAPI backend
    ├── frontend.py                     # Streamlit frontend
    ├── requirements.txt                # Required packages
    └── README.md                       # Project documentation
```

---

## ⚙️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | REST API backend |
| Streamlit | Frontend web interface |
| Pydantic | Data validation |
| Scikit-learn | Machine learning model |
| Pandas | Data processing |
| Uvicorn | 

---

##  How to Run Locally

### Step 1 — Clone the repository
```bash
git clone https://github.com/Rehena-Sultana/Insurance_premium_prediction.git
cd Insurance_premium_pred
```

### Step 2 — Create a virtual environment
```bash
python -m venv myenv
myenv\Scripts\activate
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Run FastAPI backend
```bash
uvicorn app:app --reload
```
API will be available at: `http://127.0.0.1:8000`

### Step 5 — Run Streamlit frontend (in a new terminal)
```bash
streamlit run frontend.py
```
App will be available at: `http://localhost:8501`

---

##  API Endpoints

### POST `/predict`

Predicts the insurance premium category for a user.

**Request Body:**
```json
{
    "age": 30,
    "weight": 70.0,
    "height": 1.75,
    "income_lpa": 10.0,
    "smoker": false,
    "city": "Mumbai",
    "occupation": "private_job"
}
```

**Response:**
```json
{
    "predicted_category": "Low"
}
```

---

##  Input Fields

| Field | Type | Description |
|---|---|---|
| `age` | int | Age of the user (1-119) |
| `weight` | float | Weight in kg |
| `height` | float | Height in meters (0.5-2.5) |
| `income_lpa` | float | Annual income in LPA |
| `smoker` | bool | Smoking status (true/false) |
| `city` | string | City of residence |
| `occupation` | string | Type of occupation |

**Valid occupations:**
- `retired`
- `freelancer`
- `student`
- `government_job`
- `business_owner`
- `unemployed`
- `private_job`

---

## ML Model Features

The model uses these computed features for prediction:

| Feature | Description |
|---|---|
| `bmi` | Calculated from weight and height |
| `age_group` | young / adult / middle_aged / senior |
| `lifestyle_risk` | low / medium / high |
| `city_tier` | 1 / 2 / 3 based on city |
| `income_lpa` | Annual income |
| `occupation` | Type of occupation |

---

##  Live Demo

- **Frontend:** [Streamlit App](https://insurancepremiumprediction-ihvbuwe4vnzv4ajmf6v4dq.streamlit.app/)
- **Backend API:** [Render API](https://insurance-premium-prediction-uugj.onrender.com)
- **API Docs:** [Swagger UI](https://insurance-premium-prediction-uugj.onrender.com/docs#/default/predict_premium_predict_post)

---


