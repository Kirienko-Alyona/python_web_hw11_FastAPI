from datetime import datetime

from pydantic import BaseModel, Field, EmailStr

class ContactModel(BaseModel):
    name: str = Field('James', min_length=3, max_length=16)
    surname: str = Field('Cat', min_length=3, max_length=16)
    email: EmailStr
    phone: int = Field('0631111234')
    born_date: datetime = '12.12.1912'
    
    
class ContactResponse(BaseModel):
    id: int = 1
    name: str
    surname: str
    email: EmailStr
    phone: int
    born_date: datetime

    class Config:
        orm_mode = True    