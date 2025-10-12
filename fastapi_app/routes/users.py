from .. schemas import UserOutput,UserCreate,ProductCreate,ProductOutput
from fastapi import status,APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException
from ..utils import hashpassword
from ..models import User,Product
from ..database import get_db
router=APIRouter(prefix="/users",tags=["Users"])

@router.post("/",response_model=UserOutput,status_code=status.HTTP_201_CREATED)
def create_user(userdata:UserCreate,db:Session=Depends(get_db)):
  
  userdata=userdata.model_dump()
  password=userdata["userpassword"]
  userdata["userpassword"]=hashpassword(password)
  print(password)
  user=User(**userdata)
  db.add(user)

  db.commit()
  return user
@router.get("/{id}",response_model=UserOutput)
def get_user(id:int,db:Session=Depends(get_db)):
  user=db.query(User).get({"userid":id})
  if user is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
  return user
