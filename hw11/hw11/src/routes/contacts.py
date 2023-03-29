from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from sqlalchemy.orm import Session
from src.database.connect import get_db
from src.database.models import Contact

from src.schemas import ContactResponse, ContactModel

router = APIRouter(prefix='/contacts', tags=['contacts'])

@router.get("/contacts", response_model=List[ContactResponse])
async def get_contacts(limit: int = Query(10, le=500), offset: int = 0, db: Session = Depends(get_db)):
    contacts = db.query(Contact).limit(limit).offset(offset).all()
    return contacts


@router.get("/{contact_id}", response_model=ContactResponse)
async def get_contact(contact_id: int = Path(ge=1), db: Session = Depends(get_db)):
    contact = db.query(contact).filter_by(id=contact_id).first()
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contact


@router.post("", response_model=ContactResponse)
async def create_contact(body: ContactModel, db: Session = Depends(get_db)):
    contact = contact(**body.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(body: ContactModel, contact_id: int = Path(ge=1), db: Session = Depends(get_db)):
    contact = db.query(contact).filter_by(id=contact_id).first()
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    contact.nickname = body.nickname
    contact.age = body.age
    contact.vaccinated = body.vaccinated
    contact.description = body.description
    contact.owner_id = body.owner_id
    db.commit()
    return contact


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_contact(contact_id: int = Path(ge=1), db: Session = Depends(get_db)):
    contact = db.query(contact).filter_by(id=contact_id).first()
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    db.delete(contact)
    db.commit()
    return contact
