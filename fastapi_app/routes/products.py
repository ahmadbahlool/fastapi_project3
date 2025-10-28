from .. schemas import UserOutput,UserCreate,ProductCreate,ProductOutput,ProductOut
from fastapi import status
from ..o2auth import get_user
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import Depends,HTTPException,APIRouter
from ..utils import hashpassword
from ..models import User,Product,Vote
from ..database import get_db
router=APIRouter(prefix="/products",tags=["Products"])
@router.post("/",response_model=ProductOutput,status_code=status.HTTP_201_CREATED)
def create_product(updatedata:ProductCreate,db:Session=Depends(get_db),user:int=Depends(get_user)):
  
  product=Product(**updatedata.model_dump(),owner=user.userid)
  
  db.add(product)
  db.commit()
  db.refresh(product)
  return product

@router.get("/{id}",response_model=ProductOut)
def get_product(id:int,db:Session=Depends(get_db),user:int=Depends(get_user)):
  singleproduct=db.query(Product,func.count(Vote.productid)).join(Vote,Vote.productid==Product.productid,full=True).group_by(Product.productid).having(Product.productid==id).first()

  if singleproduct==None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="product not found")  

  return {"product":singleproduct[0],"likes":singleproduct[1]}
@router.put("/{id}",response_model=ProductOutput)
def update_product(updatedata:ProductCreate,id:int,db:Session=Depends(get_db),user:int=Depends(get_user)):

  singleproduct=db.query(Product).filter(Product.productid==id)
  if singleproduct.first()==None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="your product not found")
  if singleproduct.first().owner!=user.userid:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="you are not allowed to update this product")


  singleproduct.update(updatedata.model_dump())
  db.commit()
  return singleproduct.first()
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id:int,db:Session=Depends(get_db),user:int=Depends(get_user)):
  product=db.query(Product).filter(Product.productid==id)
  
  if product.first()==None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Your product not found")
  if product.first().owner!=user.userid:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="you are not allowed to delete this product")



  product.delete()
  db.commit()
  return {"detail":"deleted"}
@router.get("/",response_model=List[ProductOut])
def get_products(search:str="",limit:int=0,offset:int=0,db:Session=Depends(get_db),user:int=Depends(get_user)):
  if offset:
    all_products=db.query(Product).offset(offset=offset).limit(limit=limit if limit else None)
    return all_products
  elif limit:
        all_products=db.query(Product).limit(limit=limit)
        return all_products


 
  if not search=="":
    print(search)
    all_products=db.query(Product,func.count(Vote.productid)).join(Vote,Vote.productid==Product.productid,isouter=True).group_by(Product.productid).filter(Product.productname.icontains(search)).union(db.query(Product,func.count(Vote.productid)).join(Vote,Vote.productid==Product.productid,isouter=True).group_by(Product.productid).filter(Product.productdescription.icontains(search))).all()
  else:
    all_products=db.query(Product,func.count(Vote.productid)).join(Vote,Vote.productid==Product.productid,isouter=True).group_by(Product.productid).all()
  
  for i,product in enumerate(all_products,0):
      all_products[i]={"product":product[0],"likes":product[1]} 
    
  return all_products
