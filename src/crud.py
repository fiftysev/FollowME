from hashlib import sha256
from sqlalchemy.orm import Session
from . import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = sha256(user.password.encode("utf-8")).hexdigest()
    db_user = models.User(username=user.username, password=hashed_password)
    db.ad(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
