from jose import jwt,JWTError
from fastapi import HTTPException,status,Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .database import get_db
from .models import User
from datetime import datetime as dt,timedelta
import datetime
from .config import env_variables

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="user/login")
SECRET_KEY = env_variables.secretkey
ALGORITHM = env_variables.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = env_variables.access_token_expires_minutes

def create_jwt_token(userdata:dict):
  data=userdata.copy()
  data["exp"]=dt.now(datetime.timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  token=jwt.encode(claims=data,key=SECRET_KEY,algorithm=ALGORITHM)
  return token
def verify_jwt_token(token:str,credentialexception):
  try:
    userdata=jwt.decode(token=token,key=SECRET_KEY,algorithms=ALGORITHM)
    userid=userdata["userid"]
    print(type(userid))

    if userid is  None:
      raise credentialexception
    else:
      return userid
  except JWTError:
    raise credentialexception
  
def get_user(token:str,db:Session=Depends(get_db)):
  credentialexception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="could not validate credential",headers={"WWW-Authenticate":"Bearer"})
  
  userid=verify_jwt_token(token,credentialexception)
  user=db.query(User).get(userid)
  if user is None:
    raise credentialexception
  else:
    return user
  