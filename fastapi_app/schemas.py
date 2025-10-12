from pydantic import BaseModel,EmailStr
from typing import Optional


class UserBase(BaseModel):
  username:str


class UserCreate(UserBase):
  userpassword:str
  useremail:EmailStr


class UserOutput(UserBase):
  useremail:EmailStr

  class Config:
    from_attribute=True
  pass
class UserLogin(UserBase):
    userpassword:str
class Token(BaseModel):
  access_token:str
  token_type:str
class ProductsBase(BaseModel):
  productname:str
  productdescription:str
  

class ProductCreate(ProductsBase):
  productdelivered:Optional[bool] =False

class ProductsVote(BaseModel):
  productid:int
  votedir:bool
class ProductsVoteOutput(BaseModel):
  productid:int
  userid:int 
class ProductOutput(ProductsBase):
  owner_user:UserOutput

  class Config:
    from_attribute=True
  pass
class ProductOut(BaseModel):
  product:ProductOutput
  likes:int 
  class Config:
    from_attribute=True


