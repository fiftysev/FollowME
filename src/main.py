from fastapi import FastAPI, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import schemas, crud, models, database


class Settings(BaseModel):
    authjwt_secret_key: str = "secret"


app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@AuthJWT.load_config
def get_config():
    return Settings()


@app.post("/auth/signup/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)


@app.get("/place/{tag}/")
def get_place(tag: str, db: Session = Depends(get_db)):
    db_place = crud.get_place(db, tag=tag)
    if db_place is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_place
