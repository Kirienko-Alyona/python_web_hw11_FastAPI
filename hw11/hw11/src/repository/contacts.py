from datetime import date, timedelta
from typing import List, Optional

from sqlalchemy.orm import Session

from src.schemas.contacts import ContactModel, ContactUpdate
from src.database.models import Contact


async def get_contacts_search(count_days: int, search_name: str, search_surname: str, search_email: str, search_phone: str, limit: int, offset: int, db: Session) -> Optional[List[Contact]]:
    #if not input params - returned all list contacts 
    #else - search by parametrs: name, surname, email, phone - returned list contacts     
    #function returns a list of contacts whose birthday will be in the near future "count_days"
    contacts_list_obj = []
    contacts = db.query(Contact) 
    if count_days:
        today = date.today()
        for i in range(1, count_days+1):
            next_day = today + timedelta(days=i)
            contacts_obj = contacts.filter_by(born_date=next_day).first()
            if contacts_obj != None: 
                contacts_list_obj.append(contacts_obj)
            else: 
                continue
        return contacts_list_obj         
    if search_name:
        #contacts = contacts.filter(Contact.name.ilike(f'%{s_name}%')) - робить те ж саме, що і icontains
        contacts = contacts.filter(Contact.name.icontains(search_name))  
        print(type(contacts))
        print(contacts)
    if search_surname:   
        contacts = contacts.filter(Contact.surname.icontains(search_surname))
    if search_email:   
        contacts = contacts.filter(Contact.email.icontains(search_email))   
    if search_phone:
        contacts = contacts.filter(Contact.phone.icontains(search_phone)) 
    contacts.limit(limit).offset(offset).all()    
    return contacts 
        

async def get_contact_id(contact_id: int, db: Session) -> Contact:
    #search one contact by contact id - return only one contact
    contact = db.query(Contact).filter_by(id=contact_id).first()
    return contact

async def create_contact(body: ContactModel, db: Session) -> Contact:
    #create contact
    contact = Contact(**body.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

async def update_contact(body: ContactUpdate, contact_id: int, db: Session) -> Contact| None:
    #update contact
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
    #delete contact
    contact = db.query(Contact).filter_by(id=contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact     
