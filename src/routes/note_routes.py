from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.util.dependencies import get_db
from src.schemas.note_schema import *
from src.services.note_service import *

router = APIRouter(prefix="/notes", tags=["Note"])

@router.post("/", response_model=NoteResponse)
def create(note: NoteCreate, db: Session = Depends(get_db)):
    return create_note(db, note)

@router.get("/{user_id}", response_model=list[NoteResponse])
def get(user_id: int, db: Session = Depends(get_db)):
    return get_note(db, user_id)

@router.put("/", response_model=NoteResponse)
def update(note: NoteUpdate, db: Session = Depends(get_db)):
    return update_note(db, note)

@router.delete("/{note_id}")
def delete(note_id: int, db: Session = Depends(get_db)):
    return delete_note(db, note_id)