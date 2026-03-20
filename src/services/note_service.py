from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from src.config.logger import logger
from src.models.note import Note
from src.schemas.note_schema import *

def create_note(db: Session, note: NoteCreate) -> Note:
    
    try:
        logger.info("Creating note")

        new_note = Note(**note.model_dump())
        
        db.add(new_note)
        db.commit()
        db.refresh(new_note)
        
        logger.bind(
            note_id=new_note.id,
            user_id=new_note.user_id
        ).info("Note created successfully")
        
        return new_note
    
    except IntegrityError:
        db.rollback()
        
        logger.bind(
            user_id=note.user_id
        ).error("Integrity error creating note")
        
        raise HTTPException(
            status_code=400,
            detail="Invalid user_id"
        )
    
    except SQLAlchemyError:
        db.rollback()
        
        logger.bind(
            user_id=note.user_id
        ).exception("Database error creating note")
        
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    
def get_note(db: Session, user_id: int) -> list[Note]:
    try:
        logger.bind(user_id=user_id).info("Fetching all notes")
        
        notes = db.query(Note).filter(Note.user_id == user_id).all()
        
        if not notes:
            logger.bind(user_id=user_id).warning(
                "No notes found for the given user id"
            )
        
        return notes
    
    except SQLAlchemyError:
        logger.bind(user_id=user_id).error(
            "Database error fetching notes"
        )
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
   
def update_note(db: Session, current_note: NoteUpdate) -> Note:
    try:
        logger.bind(note_id=current_note.id).info("Updating note")
        
        note = db.query(Note).filter(Note.id == current_note.id).first()
        
        if not note:
            logger.bind(note_id=current_note.id).warning(
                "Note not found"
            )
            raise HTTPException(status_code=404, detail="Note not found")
        
        note.description = current_note.description
        
        db.commit()
        db.refresh(note)
        
        logger.bind(note_id=note.id).info("Note updated successfully")
        
        return note
    
    except SQLAlchemyError:
        db.rollback()
        logger.bind(note_id=current_note.id).error(
            "Database error updating note"
        )
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
def delete_note(db: Session, note_id: int) -> dict:
    try:
        logger.bind(note_id = note_id).info("Deleting note")
        
        note = db.query(Note).filter(Note.id == note_id).first()
        
        if not note:
            logger.bind(note_id = note_id).warning(
                "Note not found"
            )
            raise HTTPException(
                status_code=404,
                detail="Note not found"
            )
        
        db.delete(note)
        db.commit()
        
        logger.bind(note_id = note_id).info("Note deleted successfully")
        return {"message": f"Note {note_id} deleted successfully"}
    
    except IntegrityError as e:
        db.rollback()
        logger.bind(note_id = note_id).error(
            "Integrity error deleting note"
        )
        raise HTTPException(
            status_code=400, 
            detail="Cannot delete note: linked records exist"
        )
        
    except SQLAlchemyError as e:
        logger.bind(note_id = note_id).error(
            "Database error deleting note"
        )
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")