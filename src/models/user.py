from sqlalchemy import Column, Integer, String, CHAR, Boolean

from src.config.database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    contact_no = Column(String(15))
    is_active = Column(Boolean, default=False)
    
    