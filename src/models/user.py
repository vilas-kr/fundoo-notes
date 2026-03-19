from sqlalchemy import Column, Integer, String, CHAR, Boolean

from src.config.database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    contact_no = Column(CHAR(10))
    is_active = Column(Boolean, default=False)
    
    