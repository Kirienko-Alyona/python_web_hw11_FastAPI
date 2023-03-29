from datetime import date

from pydantic import BaseModel, Field, EmailStr

class ContactModel(BaseModel):
    name: str = Field('James', min_length=3, max_length=16)
    surname: str = Field('Cat', min_length=3, max_length=16)
    email: EmailStr = Field('user@example.com')
    phone: int = Field('380631234567')
    born_date: date = Field('2023-03-29')
    
    
class ContactResponse(BaseModel):
    id: int = 1
    name: str
    surname: str
    email: EmailStr
    phone: int = 1
    born_date: date

    class Config:
        orm_mode = True    
        
class ContactUpdate(BaseModel):
    id: int = 1
    name: str
    surname: str
    email: EmailStr
    phone: int = 1
    born_date: date        