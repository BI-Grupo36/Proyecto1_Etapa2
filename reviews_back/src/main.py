from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from src.routers import review

app = FastAPI(
    description="This API provides a straightforward solution for categorizing reviews into five distinct categories, each representing the score attributed to a particular hotel. ",
    title="Review Classifier",
)
app.include_router(review.router)

#Activaction of DataBase (config/db_settings.py)
# Base.metadata.create_all(bind=engine)

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

@app.get("/")
def root() -> RedirectResponse:
    return RedirectResponse(url="/docs")