
from pydantic.typing import resolve_annotations
from sqlalchemy.orm import Session, session
from sqlalchemy.sql.operators import from_
from sqlalchemy.sql.sqltypes import Time

from . import models, schemas


def get_job(db: Session, job_id: int):

    
    return  db.query(models.User).filter(models.User.id == job_id).first()

def get_user_by_id(db: Session, id: int):

    return  db.query(models.Item).filter(models.Item.id == id).first()


def get_user(db: Session, user_id: int):
    return db.query(models.Item).filter(models.Item.id == user_id).first()


def get_job_by_id(db: Session, role: str):
    return db.query(models.User).filter(models.User.role == role).first()

def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_job(db: Session, user: schemas.UserCreate):
    db_user = models.User(role=user.role, qualification = user.qualification, location = user.location, salary = user.salary)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



def apply( db: Session, apply: schemas.applyCreate, job_id: int, user_id: int):
    db_apply = models.apply(**apply.dict(), owner_id=job_id, user_id=user_id)
    if job_id == models.User.id:
        return db.query(models.User).filter(models.User.id == job_id).first()
    db.add(db_apply)
    db.commit()
    db.refresh(db_apply)
    return  db_apply 

def get_response(db: Session, apply_id: int):

    
    return  db.query(models.apply).filter(models.apply.id == apply_id).first()




