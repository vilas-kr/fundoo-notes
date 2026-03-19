from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.util.dependencies import get_db
from src.schemas.user_schema import *
from src.services.user_service import *

router = APIRouter(prefix="/users", tags=["Users"])

@router.post('/', response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/all", response_model=list[UserResponse])
def all_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.get("/{user_id}", response_model=UserResponse)
def search(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)

@router.put("/", response_model=UserResponse)
def update(user: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, user)

@router.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)

