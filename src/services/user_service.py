from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from src.models.user import User
from src.schemas.user_schema import *
from src.config.logger import logger

def create_user(db: Session, user: UserCreate) -> User:
    '''
    Creates a new user in the database.
    
    Args:
        db (Session): Database session for performing operations.
        user (UserCreate): Pydantic model containing user details.
        
    Returns:
        User: The created user object.
    Raises:
        HTTPException: If there's an integrity error or database error.
    '''

    try:
        logger.info("Creating user")
        new_user = User(**user.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        logger.info(
            "User created successfully", 
            extra={"user_id": new_user.id, "email": new_user.email}
        )
        return new_user
    
    except IntegrityError as e:
        db.rollback()
        logger.error(
            "Integrity error creating user",
            extra={"email": user.email}
        )
        raise HTTPException(status_code=400, detail="User with given email already exists")
    except Exception as e:
        db.rollback()
        logger.error(
            "Database error creating user",
            extra={"email": user.email}
        )
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
def get_users(db: Session) -> list[User]:
    '''
    Fetches all users from the database.
    Args:
        db (Session): Database session for performing operations.
           
    Returns:
        list[User]: A list of user objects.
    Raises:
        HTTPException: If there's a database error.
    '''
    
    try:
        logger.info("Fetching All users")
        return db.query(User).all()
    except SQLAlchemyError as e:
        logger.error("Error fetching users")
        raise HTTPException(status_code=500, detail="Internal Server Error")

def get_user(db: Session, user_id: int) -> User:
    '''
    Fetches a user by their ID from the database.
    
    Args:
        db (Session): Database session for performing operations.
        user_id (int): The ID of the user to fetch.
        
    Returns:
        User: The fetched user object.
    Raises:
        HTTPException: If the user is not found or there's a database error.
    '''
    
    try:
        logger.info(f"Fetching user by ID: {user_id}")
        user = db.query(User).filter(User.id == user_id).first()
        
        if not user:
            logger.warning(
                "User not found",
                extra={"user_id": user_id}
            )
            raise HTTPException(status_code=404, detail="User not found")
        
        return user
    
    except SQLAlchemyError as e:
        logger.error(
            "Database error fetching user",
            extra={"user_id": user_id}
        )
        raise HTTPException(status_code=500, detail="Internal Server Error")
   

def update_user(db: Session, current_user: UserUpdate) -> User:
    '''
    Updates an existing user in the database.
    
    Args:
        db (Session): Database session for performing operations.
        current_user (UserUpdate): Pydantic model containing updated user details.
        
    Returns:
        User: The updated user object.
    Raises:
        HTTPException: If the user is not found or there's an integrity error.
    '''
    
    try:
        logger.info(f"Updating user {current_user.id}")
        
        user = db.query(User).filter(User.id == current_user.id).first()
        if not user:
            logger.warning(
                "User not found",
                extra={"user_id": current_user.id}
            )
            raise HTTPException(status_code=404, detail="User not found")
        
        user.name = current_user.name
        user.email = current_user.email
        user.contact_no = current_user.contact_no
        user.is_active = current_user.is_active
        user.password = current_user.password
        
        db.commit()
        db.refresh(user)
        logger.info(f"User updated successfully: {user.id}")
        return user
    
    except IntegrityError as e:
        db.rollback()
        logger.error(
            "Integrity error updating user",
            extra={"user_id": current_user.id, "email": current_user.email}
        )
        raise HTTPException(status_code=400, detail="Email already in use")
    except SQLAlchemyError as e:
        logger.error(
            "Database error updating user",
            extra={"user_id": current_user.id}
        )
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except Exception as e:
        logger.error(f"Some thing went wrong: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")
            
def delete_user(db: Session, user_id: int) -> Dict:
    '''
    Deletes a user from the database.
    
    Args:
        db (Session): Database session for performing operations.
        user_id (int): The ID of the user to delete.
        
    Returns:
        Dict: A dictionary containing a success message.
    Raises:
        HTTPException: If the user is not found or there's a database error.
    '''
    
    try:
        logger.info(f"Deleting user : {user_id}") 
        user = db.query(User).filter(User.id == user_id).first()
        
        if not user:
            logger.warning(f"User not found : {user_id}")
            raise HTTPException(status_code=404, detail="User Not Found")
        
        db.delete(user)
        db.commit()
        
        logger.info(f"User deleted successfully: {user.id}")
        return {"message": f"User {user_id} deleted successfully"}
        
    except IntegrityError as e:
        db.rollback()
        logger.error(
            "Integrity error deleting user",
            extra={"user_id": user_id}
        )
        raise HTTPException(
            status_code=400, 
            detail="Cannot delete user: linked records exist"
        )
        
    except SQLAlchemyError as e:
        logger.error(
            "Database error deleting user",
            extra={"user_id": user_id}
        )
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")
     
        
        
        