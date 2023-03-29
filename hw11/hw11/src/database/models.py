from sqlalchemy import Column, Date, Integer, String

from src.database.connect import Base



class Contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, nullable=False)
    born_date = Column(Date)   
