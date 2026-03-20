from pydantic import BaseModel

class NoteCreate(BaseModel):
    user_id: int
    description: str
    
class NoteResponse(BaseModel):
    id: int
    user_id: int
    description: str

    class Config:
        from_attributes = True
        
class NoteUpdate(BaseModel):
    id: int
    description: str
