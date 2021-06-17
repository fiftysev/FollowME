from deta import Deta
from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, OAuth2PasswordBearer
from .auth import Auth
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import schemas, crud, models, database


deta = Deta("c04fkipu_emGgP1bWxRisPxxQQrTfnfkEPSazUAjg")
users_db = deta.Base('users')


class Settings(BaseModel):
    authjwt_secret_key: str = "secret"


app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

security = HTTPBearer()
auth_handler = Auth()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@AuthJWT.load_config
def get_config():
    return Settings()


@app.get("/place/{tag}/")
def get_place(tag: str, db: Session = Depends(get_db)):
    db_place = crud.get_place(db, tag=tag)
    if db_place is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_place


@app.post('/signup')
def signup(user_details: schemas.AuthModel):
    if users_db.get(user_details.username) is not None:
        return 'Account already exists'
    try:
        hashed_password = auth_handler.encode_password(user_details.password)
        user = {'username': user_details.username, 'first_name': user_details.first_name,
                'last_name': user_details.last_name, 'password': hashed_password}
        return users_db.put(user)
    except Exception:
        error_msg = 'Failed to signup user'
        return error_msg


@app.post('/login')
def login(user_details: schemas.AuthModel):
    user = users_db.get(user_details.username)
    if (user is None):
        return HTTPException(status_code=401, detail='Invalid username')
    if (not auth_handler.verify_password(user_details.password, user['password'])):
        return HTTPException(status_code=401, detail='Invalid password')

    access_token = auth_handler.encode_token(user['key'])
    refresh_token = auth_handler.encode_refresh_token(user['key'])
    return {'access_token': access_token, 'refresh_token': refresh_token}


@app.get('/refresh_token')
def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    refresh_token = credentials.credentials
    new_token = auth_handler.refresh_token(refresh_token)
    return {'access_token': new_token}

# @app.post('/secret')
# def secret_data(credentials: HTTPAuthorizationCredentials = Security(security)):
#     token = credentials.credentials
#     if(auth_handler.decode_token(token)):
#         return 'Top Secret data only authorized users can access this info'
#
# @app.get('/notsecret')
# def not_secret_data():
#     return 'Not secret data'
