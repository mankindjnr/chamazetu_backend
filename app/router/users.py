from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from .. import schemas, utils, oauth2, models
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResp)
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    user.password = utils.hash_password(user.password)
    new_user = models.User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"User": [{"email": new_user.email, "created_at": new_user.created_at}]}

@router.get("/me")
async def get_user(current_user: models.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    return {"email": current_user.email}

