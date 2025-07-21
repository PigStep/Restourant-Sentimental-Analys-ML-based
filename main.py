from model import TextClassifier
from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
classifier = TextClassifier('restaurant_review_pipelineLR.joblib')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Only for developing. Specific domains for production
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    text = data["text"]
    print(classifier.predict(data["text"]),f" {text}")
    try:
        prediction = classifier.predict(text)
        print("positive" if prediction == 1 else "negative")
        return {
            "prediction": "positive" if prediction == 1 else "negative",
        }
    except Exception as e:
        return {"error": str(e)}