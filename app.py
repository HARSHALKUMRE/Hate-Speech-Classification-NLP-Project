from src.hatespeechClassifier.pipeline.training_pipeline import TrainingPipeline
from fastapi import FastAPI
import uvicorn
import sys
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from src.hatespeechClassifier.pipeline.prediction_pipeline import PredictionPipeline
from src.hatespeechClassifier.exception import CustomException
from src.hatespeechClassifier.constants import *

text: str = "What is machine learning?"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        training_pipeline = TrainingPipeline()

        training_pipeline.run_pipeline()

        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")

@app.post("/predict")
async def predict_route(text):
    try:

        obj = PredictionPipeline()
        text = obj.run_pipeline(text)
        return text
    except Exception as e:
        raise CustomException(e, sys) from e


if __name__=="__main__":
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)