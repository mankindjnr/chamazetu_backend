from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from .. import schemas, database, utils, oauth2, models

router = APIRouter(
    prefix="/users",
    tags=["Authentication"]
)

@router.post("/login", response_model=schemas.Token)
async def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

    access_token = await oauth2.create_access_token(data={"sub": user.email})
    
    return {"access_token": access_token, "token_type": "bearer"}


# this is for logout, currently not working but everything else is working
@router.post("/logout")
async def logout(current_user: models.User = Depends(oauth2.get_current_user)):
    token_data = schemas.TokenData(username=current_user.email, expires=0)
    return {"token_data": token_data}