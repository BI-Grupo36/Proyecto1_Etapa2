from io import BytesIO
from fastapi import UploadFile
from pandas import read_csv, DataFrame
from sqlalchemy.orm import Session
from src.services.classifier_model import classify_review, classify_reviews
from src.models.review import Review as ReviewModel
from src.schemas.review import ReviewCreate, ReviewResponse
from typing import List
from uuid import uuid4


def get_review(db: Session, id: str) -> ReviewModel:
    return (
        db.query(ReviewModel)
        .filter(ReviewModel.id == id)
        .first()
    )


def get_review_by_text(db: Session, text: str) -> ReviewModel:
    return (
        db.query(ReviewModel)
        .filter(ReviewModel.text == text)
        .first()
    )


def get_reviews_by_category(db: Session, category: int) -> List[ReviewModel]:
    return (
        db.query(ReviewModel)
        .filter(ReviewModel.category == category)
        .all()
    )


def get_reviews(db: Session) -> List[ReviewModel]:
    return db.query(ReviewModel).all()



def create_review(db: Session, review: ReviewCreate) -> ReviewModel:
    predicted_category, preprocessed_text = classify_text(review.text)
    db_review = ReviewModel(
        id=str(uuid4()),
        text=review.text,
        category=predicted_category,
        preprocessed_text=preprocessed_text
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def classify_text(text: str) -> int:
    return classify_review(text)


def read_reviews_from_csv(db: Session, file: UploadFile) -> (bool, str): # type: ignore
    df = read_csv(BytesIO(file.file.read()))

    if len(df.columns) > 1:
        return (False, "The dataframe must have only one column, the reviews you want to load")
    elif len(df.columns) < 1:
        return (False, "The dataframe must have at least one column, the reviews you want to load")
    
    # Check if the reviews already exist in the database
    for index, row in df.iterrows():
        if get_review_by_text(db, row[df.columns[0]]):
            df.drop(index=index, inplace=True)

    if df.empty:
        return (True, "All reviews already exist in the database")

    answ_df = classify_reviews(df)

    reviews = []
    for _, row in answ_df.iterrows():
        db_review = ReviewModel(
            id=str(uuid4()),
            text=row["Review"],
            score=row["Score"]
        )
        db.add(db_review)
        db.commit()
        db.refresh(db_review)
        reviews.append(db_review)

    return (True, "Reviews created and classified successfully")



def delete_review(db: Session, id: str) -> None:
    db_review = get_review(db, id)
    db.delete(db_review)
    db.commit()