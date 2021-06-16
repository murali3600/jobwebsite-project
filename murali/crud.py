
from sqlalchemy.orm import Session

from . import models, schemas


def get_job(db: Session, job_id: int):
    return db.query(models.User).filter(models.User.id == job_id).first()




def get_job_by_id(db: Session, role: str):
    return db.query(models.User).filter(models.User.role == role).first()


def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_job(db: Session, user: schemas.UserCreate):
    db_user = models.User(role=user.role, qualification = user.qualification)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



def apply(db: Session, apply: schemas.applyCreate, job_id: int):
    db_apply = models.apply(**apply.dict(), owner_id=job_id)
    db.add(db_apply)
    db.commit()
    db.refresh(db_apply)
    return db_apply




