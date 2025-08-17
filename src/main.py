from model import TextClassifier
from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
classifier = TextClassifier("..\model\model.joblib")

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
        result= {
            "prediction": "positive" if prediction["prediction"] == 1 else "negative",
            "confidence": prediction["confidence"]
        }
        print(result)
        return result
    except Exception as e:
        return {"error": str(e)}