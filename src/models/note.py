from sqlalchemy import Column, Integer, ForeignKey, String

from src.config.database import Base

class Note(Base):
    __tablename__ = 'notes'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    description = Column(String, nullable=False)
    
    
