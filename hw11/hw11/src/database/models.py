from sqlalchemy import Column, Date, DateTime, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class Contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, nullable=False)
    born_date = Column(Date)   
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
