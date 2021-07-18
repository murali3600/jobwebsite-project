from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    qualification: Optional[str] = None
    

class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    role: str
    location: str
    salary: int
   



class UserCreate(UserBase):
   qualification: str


class User(UserBase):
    id: int
    is_active: bool
    ##items: List[Item] = []

    class Config:
        orm_mode = True


class applyBase(BaseModel):
    ##job : List[User] = []
    name: str
    
class applyCreate(applyBase):
    role: str
    mailid: str    


class apply(applyBase):
    id: int
    owner_id: int
    user_id: int
    class Config:
        orm_mode = True