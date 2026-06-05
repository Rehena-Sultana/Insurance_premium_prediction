from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input_pydantic import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict_output, model,model_version

app = FastAPI()

# for human readable
@app.get('/')
def home():
    return {"message" : "/insurance premium prediction API"}

# for machine readable
@app.get('/health')
def health_checkbox():
    return { "message" : "ok",
            'version' : model_version,
            "model_loaded" : model is not None}

@app.post('/predict', response_model=PredictionResponse)
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    try:
        prediction = predict_output(user_input)

        return JSONResponse(status_code=200, content={'response': prediction})
    
    except Exception as e:
        return JSONResponse (status_code=500, content= str(e))
#content={...} — the JSON data sent back to the user
#[0] — takes the first (and only) result from that array

# User sends JSON  →  Pydantic validates it  →  computed fields calculated ->DataFrame created  →  ML model predicts  →  JSON response returned




