from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from jose import jwt, JWTError

import models
import schemas

from database import SessionLocal, engine
from auth import create_access_token, SECRET_KEY, ALGORITHM

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="JWT Authentication API"
)

security = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    new_user = models.User(
        username=user.username,
        password=user.password
    )

    db.add(new_user)
    db.commit()

    return {"message":"User Registered"}


@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(models.User).filter(
        models.User.username==user.username,
        models.User.password==user.password
    ).first()

    if not db_user:
        raise HTTPException(status_code=401,detail="Invalid Credentials")

    token = create_access_token(
        {"sub":db_user.username}
    )

    return {"access_token":token}


@app.get("/profile")
def profile(credentials: HTTPAuthorizationCredentials = Depends(security)):

    token = credentials.credentials

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return {
            "message":"Protected Route",
            "user":payload["sub"]
        }

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )


@app.post("/logout")
def logout():

    return {
        "message":"Logout Successful"
    }