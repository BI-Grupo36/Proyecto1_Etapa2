from msilib.schema import File
from typing import List
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from src.schemas.review import ReviewResponse, ReviewCreate
import src.services.review as service
from src.config.db_settings import get_db

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"],
    responses={
        404: {"description": "The requested resource was not found."},
        500: {"description": "Internal server error. Please try again later."}
    },
)

@router.get("/score/{score}", response_model=List[ReviewResponse], status_code=200)
def get_reviews_by_score(score: int, db: Session = Depends(get_db)) -> List[ReviewResponse]:
    """
    Retrieve reviews based on their score.

    Args:
        score (int): The score to filter reviews by.

    Returns:
        List[ReviewResponse]: List of reviews matching the specified score.
    """
    if not 1 <= score <= 5:
        raise HTTPException(status_code=400, detail=f"Invalid score: {score}. Score must be between 1 and 5.")
    return service.get_reviews_by_score(db, score)

@router.get("/{id}", response_model=ReviewResponse, status_code=200)
def get_review_by_id(id: str, db: Session = Depends(get_db)) -> ReviewResponse:
    """
    Retrieve a single review by its ID.

    Args:
        id (str): The ID of the review to retrieve.

    Returns:
        ReviewResponse: Details of the retrieved review.
    """
    retrieved_review = service.get_review(db, id)
    if retrieved_review is None:
        raise HTTPException(status_code=404, detail=f"Review with id {id} not found")
    return retrieved_review

@router.get("/", response_model=List[ReviewResponse], status_code=200)
def get_all_reviews(db: Session = Depends(get_db)) -> List[ReviewResponse]:
    """
    Retrieve all reviews available in the database.

    Returns:
        List[ReviewResponse]: List of all reviews.
    """

    return service.get_reviews(db)

@router.post("/", response_model=ReviewResponse, status_code=201)
def classify_review(review: ReviewCreate, db: Session = Depends(get_db)) -> ReviewResponse:
    """
    Create a new review in the database.

    Args:
        review (ReviewCreate): Details of the review to create.

    Returns:
        ReviewResponse: Details of the newly created review.
    """
    existing_review = service.get_review_by_text(db, review.text)
    if existing_review:
        return existing_review
    return service.create_review(db=db, review=review)

@router.post("/file", status_code=201)
def load_reviews(db: Session = Depends(get_db), file: UploadFile =File(...)) -> str:
    """
    Load multiple reviews into the database.

    Args:
        reviews (List[ReviewCreate]): List of reviews to load.

    Returns:
        List[ReviewResponse]: List of newly created reviews.
    """
    if file.content_type != "text/csv":
        raise HTTPException(status_code=400, detail="Only CSV files are allowed.")
    response = service.read_reviews_from_csv(db=db,file=file)
    if not response[0]:
        raise HTTPException(status_code=400, detail="No reviews found in the CSV file.")
    return response[1]

@router.delete("/{id}", status_code=204)
def delete_review(id: str, db: Session = Depends(get_db)):
    """
    Delete a review from the database.

    Args:
        id (str): The ID of the review to delete.
    """
    service.delete_review(db, id)
    return None

@router.delete("/", status_code=204)
def delete_all_reviews(db: Session = Depends(get_db)):
    """
    Delete all reviews from the database.
    """
    service.delete_all_reviews(db)
    return None