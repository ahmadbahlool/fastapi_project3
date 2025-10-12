from fastapi import APIRouter,Depends,status,Response,HTTPException
from ..o2auth import get_user
from ..database import get_db
from sqlalchemy.orm import Session
from ..schemas import ProductsVote
from ..models import Vote,Product,User
from sqlalchemy.exc import IntegrityError


router=APIRouter(tags=["Votes",])

@router.post("/vote")
def product_vote(votedata:ProductsVote,responseobject:Response,user=Depends(get_user),db:Session=Depends(get_db)):
  productid=votedata.productid
  userid=user.userid
  product=db.query(Product).get(productid)
  if product:
    
    if votedata.votedir:
      vote=db.query(Vote).get((productid,userid))
      if not vote:

    
        vote=Vote(productid=productid,userid=userid)
        
        
      
        db.add(vote)
        db.commit()
        db.refresh(vote)
        responseobject.status_code=status.HTTP_201_CREATED
        return {"message":"successful"}
      else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="cannot like twice")
    
    
    else:
    
      vote=db.query(Vote).filter(Vote.productid==productid,Vote.userid==userid)
      if vote.first() is not None:
        vote.delete()
        db.commit()
        responseobject.status_code=status.HTTP_204_NO_CONTENT
      else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No vote found")
  else:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid foreign key")

    
    
    
    



