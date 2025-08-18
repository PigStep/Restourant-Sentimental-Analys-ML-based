from TextClassifier import TextClassifier
from fastapi import FastAPI
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
classifier = TextClassifier("../model/model.joblib")

app.mount("/static", StaticFiles(directory="../static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Only for developing. Specific domains for production
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

# Return site for interaction
@app.get("/", response_class=HTMLResponse)
async def serve_html():
    print("Loading site...")
    with open("../static/index.html", encoding="utf-8") as file:
        return file.read()


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