import datetime
from fastapi import applications

import sqlalchemy
#from open.schemas import applyBase
from pydantic.errors import EmailError

from pydantic.networks import import_email_validator
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, query
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy_utils.types.email import EmailType 
from sqlalchemy_utils import EmailType

from .database import Base


class User(Base):
    __tablename__ = "job"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String, unique=True, index=True)
    qualification = Column(String, index=True)
    salary = Column(Integer, index=True)
    location =Column(String,index=True)
    is_active = Column(Boolean, default=True)
    ##res = db.session.query(User, applyBase).join(apply).all()

    items = relationship("Item", back_populates="owner")
    jobapplication = relationship("apply", back_populates="owner")
    

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    qualification = Column(String, index=True)
    
    owner_id = Column(Integer, ForeignKey("job.id"))

    owner = relationship("User", back_populates="items")

class apply(Base):
    __tablename__ = "jobapplication"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role = Column(String, index=True)
    mailid = Column(EmailType)
    time = Column(DateTime, default=datetime.datetime.utcnow)
    

    owner_id = Column(Integer, ForeignKey("job.id"))
    user_id = Column(Integer,ForeignKey("items.id"))
       
    owner = relationship("User", back_populates="jobapplication")



