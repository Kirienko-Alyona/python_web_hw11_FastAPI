from sqlalchemy import Column, Date, Integer, String
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
    
    
    # def __repr__(self):
    #     return "<name={}, surname={}, email={}, phone={}, born_date={}>".format(self.name, self.surname, self.email, self.phone, self.born_date)

    # @property
    # def serialize(self):
    #     return {
    #         'name': self.name,
    #         'surname': self.surname,
    #         'email': self.email,
    #         'phone': self.phone,
    #         'born_date': self.born_date,
    #     }
