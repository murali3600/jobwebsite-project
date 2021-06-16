from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "job"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String, unique=True, index=True)
    qualification = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
    jobapplication = relationship("apply", back_populates="owner")
    

class Item(Base):
    __tablename__ = "candidate"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    password = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("job.id"))

    owner = relationship("User", back_populates="items")

class apply(Base):
    __tablename__ = "jobapplication"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("job.id"))

    owner = relationship("User", back_populates="jobapplication")


