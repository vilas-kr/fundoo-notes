from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    name: str
    password: str = Field(min_length=6)
    email: EmailStr
    contact_no: str = Field(max_length=15)
    
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    contact_no: str = Field(max_length=15)
    is_active: bool
    
    class Config:
        from_attributes = True
        
class UserUpdate(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str = Field(min_length=6)
    contact_no: str = Field(max_length=15)
    is_active: bool
    
    class Config:
        from_attributes = True
        

    
