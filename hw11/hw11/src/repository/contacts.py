from typing import List
from sqlalchemy.orm import Session

from src.schemas.contacts import ContactModel, ContactUpdate
from src.database.models import Contact


async def get_contacts(limit: int, offset: int, db: Session) -> List[Contact]:
    contacts = db.query(Contact).limit(limit).offset(offset).all()
    return contacts

async def get_contact(contact_id: int, db: Session) -> Contact:
    contact = db.query(Contact).filter_by(id=contact_id).first()
    return contact

async def create_contact(body: ContactModel, db: Session) -> Contact:
    contact = Contact(name = body.name, surname = body.surname, email = body.email, phone = body.phone, born_date = body.born_date)
    #contact = Contact(**body.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

async def update_contact(body: ContactUpdate, contact_id: int, db: Session) -> Contact| None:
    contact = db.query(Contact).filter_by(id=contact_id).first()
    if contact:
        contact.name = body.name,
        contact.surname = body.surname, 
        contact.email = body.email, 
        contact.phone = body.phone, 
        contact.born_date = body.born_date
        db.commit()
    return contact    

async def remove_contact(contact_id: int, db: Session) -> Contact| None:
    contact = db.query(Contact).filter_by(id=contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact    

async def search_contact(contact_name: str, db: Session) -> List[Contact]:
    contact = db.query(Contact).filter(name=contact_name).all()  #.like(contact_name)
    return contact
