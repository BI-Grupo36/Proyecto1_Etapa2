from datetime import datetime
import unicodedata
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Counter, Optional
import pandas as pd
import numpy as np
import csv
import joblib
import os
import re
from sklearn.base import BaseEstimator, TransformerMixin
from nltk.corpus import stopwords
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi import HTTPException
from preprocessing import final_preprocessor
"""
    Functions needed for the preprocessing of the data in the pipeline
"""

"""
    Endpoint configuration
"""
class ReviewClassifier:
    def __init__(self):
        self.model = joblib.load(os.path.dirname(__file__) + '/../LinearSvmModel.joblib')
        print("Model loaded successfully")
    def predict(self, review):
        return self.model.predict(review)

review_classifier = ReviewClassifier()

app = FastAPI(
    description="This API provides a straightforward solution for categorizing reviews into five distinct categories, each representing the score attributed to a particular hotel. ",
    title="Review Classifier",
)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ReviewRequest(BaseModel):
    review: str
    file: Optional[str]

class ReviewsRequest(BaseModel):
    reviews: list
    file: Optional[str]  

@app.post("/reviews/")
async def classifyMultipleTexts(review_data: ReviewsRequest):
    try:
        reviews = review_data.reviews
        file = review_data.file
        results = []

        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        fieldnames = ["Review", "Class"]
        if not file:
            file = f"{current_datetime}.csv"
        with open(file, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for review in reviews:
                    data = {"Review": review}
                    df = pd.DataFrame(data)
                    df["Class"] = np.nan
                    pipeline_loaded = joblib.load(os.path.dirname(__file__) + '/../LinearSvmModel.pkl')
                    df['Class'] = pipeline_loaded.predict(df['Review'])
                    row = df[df['Review'] == review]
                    score = -1
                    if not row.empty:
                        score = row['Class'].iloc[0]

                    results.append({"Review": review, "Class": str(score)})
                    writer.writerow({"Review": review, "Class": str(score)})

        return {"processedReviews": str(len(results)), "file": file}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/history/{file_name}")
async def getHistoryIndividual(file_name: str):
    try:
        file = os.path.join("./reviews_back/history", file_name)
        results = []
        with open(file, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row != ["Review", "Class", "file"]:
                    results.append({"Review": row[0], "Class": row[1]})
        return results
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/history/")
async def getHistory():
    try:
        results = []
        files = os.listdir("./reviews_back/history")
        for file in files:
            with open(os.path.join("./reviews_back/history", file), 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                first_row = next(reader)
                results.append({"Review": first_row[0][0:50], "file": file})
        return results
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Directory not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


# Run the API with uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)