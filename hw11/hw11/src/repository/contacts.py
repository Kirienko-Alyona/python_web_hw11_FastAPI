from typing import List, Optional

from sqlalchemy.orm import Session

from src.schemas.contacts import ContactModel, ContactUpdate
from src.database.models import Contact


async def get_contacts(search_name: str, search_surname: str, search_email: str, search_phone: str, limit: int, offset: int, db: Session) -> Optional[List[Contact]]:
    contacts = db.query(Contact)
    if search_name:
        #contacts = contacts.filter(Contact.name.ilike(f'%{s_name}%')) - робить те ж саме, що і icontains
        contacts = contacts.filter(Contact.name.icontains(search_name))
    if search_surname:   
        contacts = contacts.filter(Contact.surname.icontains(search_surname))
    if search_email:   
        contacts = contacts.filter(Contact.email.icontains(search_email))   
    if search_phone:
        contacts = contacts.filter(Contact.phone.icontains(search_phone)) 
    contacts = contacts.limit(limit).offset(offset).all()
    return contacts

async def get_contact(contact_id: int, db: Session) -> Contact:
    contact = db.query(Contact).filter_by(id=contact_id).first()
    return contact

async def create_contact(body: ContactModel, db: Session) -> Contact:
    contact = Contact(**body.dict())
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

async def search_by_name(search_name: str, db: Session):# -> Optional[Contact]:
    
    contact = db.query(Contact).filter_by(name=search_name).first()
    """To search for a record by a specific name."""
    # return db.query(Contact).filter(Contact.name == name).first()  # .all()
    return contact
