from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from .schemas import UserLogin,Token
from .utils import validpassword
from sqlalchemy.orm import Session
from .models import User
from .o2auth import create_jwt_token,verify_jwt_token
from .database import get_db
router=APIRouter(tags=["Authentication"])
@router.post("/user/login/",response_model=Token)
def login_user(data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
  print(data)
  username=data.username
  password=data.password
  user=db.query(User).filter(User.username==username).first()
  if user is not None:
    if validpassword(password,user.userpassword):
      token=create_jwt_token({"userid":user.userid})
      return {"access_token":token,"token_type":"bearer"}
    else:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid credentials")
  else:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid credentials")
