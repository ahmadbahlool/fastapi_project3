from .database import Base
from sqlalchemy import Column,INTEGER,String,Boolean,TIMESTAMP,ForeignKey
from datetime import datetime as dt
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
class Product(Base):
  __tablename__="products"
  productid=Column(INTEGER,primary_key=True,nullable=False,index=True)
  productname=Column(String,nullable=False)
  productdescription=Column(String,nullable=True)
  productdelivered=Column(Boolean,server_default='False')
  productcreated=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
  owner=Column(INTEGER,ForeignKey("users.userid",ondelete="CASCADE"),nullable=False)
  owner_user=relationship("User")
class User(Base):
  __tablename__="users"
  userid=Column(INTEGER,primary_key=True,nullable=False,index=True)
  username=Column(String(length=30),nullable=False,unique=True)
  useremail=Column(String(length=30),nullable=False,unique=True)
  userpassword=Column(String,nullable=False)
  createdat=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
class Vote(Base):
  __tablename__="votes"
  productid=Column(INTEGER,ForeignKey("products.productid",ondelete="CASCADE"),nullable=False,primary_key=True)
  userid=Column(INTEGER,ForeignKey("users.userid",ondelete="CASCADE"),nullable=False,primary_key=True)
