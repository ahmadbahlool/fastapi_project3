from fastapi_app import schemas
import pytest
from fastapi_app.models import Product,Vote,User
from .conftest import session as db
from typing import List
session=db()

@pytest.fixture
def test_voteauthorized(test_authorized,test_createproduct):

  resp=test_authorized.post("/vote/",json={"productid":2,"votedir":1})
  assert resp.json()["message"]=="successful"
  assert resp.status_code==201
  return 2
@pytest.fixture
def test_createproduct(test_authorized,test_authorized2,create_user2):
  products=[{"productname":"socks","productdescription":"good sock","owner":1},
            {"productname":"shirt","productdescription":"good shirt","owner":1},
            {"productname":"soap","productdescription":"soap","owner":2},
            ]
  
  session.add_all([Product(**product) for product in products])
  session.commit()
  
  #data=schemas.ProductOutput()

  # data=schemas.ProductOutput()
  # assert data.productname=="shampoo"
  # assert data.productdescription=="good shampoo"
  # assert data.owner_user.username=="rashid"
  # return data
  
def test_getproducts(client,test_createproduct,test_authorized):
  resp=test_authorized.get("/products/")
  

  def store(product):
    return schemas.ProductOut(**product)
    
  products=map(store,resp.json())
  products=list(products)
  assert len(resp.json())==len(products)
  assert products[0].product.productname==resp.json()[0]["product"]["productname"]
  
  assert resp.status_code==200

def test_getproduct(test_authorized,test_createproduct):
  resp=test_authorized.get("/products/3")
  product=schemas.ProductOut(**resp.json())
  assert product.product.productname=="soap"
  assert resp.status_code==200
 
def test_getproductunauthorized(client,test_createproduct):
  client.headers.pop("Authorization")


  resp=client.get("/products/")
  assert resp.status_code==401
def test_invalidproduct(test_authorized,test_createproduct):
  
  resp=test_authorized.get("/products/12")
  resp.status=404
@pytest.mark.parametrize("productname,productdescription,productdelivered",[
  ("firstproduct","firstproduct is good ",False),
    ("secondproduct","secondproduct is good ",True),
      ("thirdproduct","thirdproduct is good ",False)

])
def test_create_product(test_authorized,productname,productdescription,productdelivered,create_user):
  resp=test_authorized.post("/products/",json={"productname":productname,"productdescription":productdescription,"productdelivered":productdelivered})
  product=schemas.ProductOutput(**resp.json())
  assert product.productname ==productname
  assert product.productdescription==productdescription
  assert product.owner_user==schemas.UserOutput(username=create_user["username"],useremail=create_user["useremail"])

def test_default_delivered(test_authorized):
    resp=test_authorized.post("/products/",json={"productname":"dummy product","productdescription":"checking deliver property"})
    assert resp.json()["productdelivered"]==False

def test_createpostunauthorized(client):
   
    resp=client.post("/products/",json={"productname":"dummy product2","productdescription":"checking deliver property3"})
    assert resp.status_code==401

def test_deleteauthorized(test_authorized,test_createproduct,create_user):

  print("should be header for the user 1")
  print(test_authorized.headers["Authorization"])
  resp=test_authorized.delete("/products/2")
  assert resp.status_code==204
def test_deleteunauthorized(client,test_createproduct):
  client.headers.pop("Authorization")
  resp=client.delete("/products/2")
  assert resp.status_code==401
def test_updateauthorized(test_authorized,test_createproduct,create_user):
  resp=test_authorized.put("/products/2",json={"productname":"updated product","productdescription":"this product is updated"})
  data=schemas.ProductOutput(**resp.json())
  assert data.productname=='updated product'
  assert data.productdescription== "this product is updated"
  assert data.owner_user==schemas.UserOutput(username=create_user["username"],useremail=create_user["useremail"])

def test_updateunauthorized(client,test_createproduct):
  # client.headers.pop("Authorization",None)
  client.headers["Authorization"]="Bearer 3232"
  resp=client.put("/products/2",json={"productname":"updated product is this","productdescription":"this product is updated"})
  print(resp.json())
  assert resp.status_code==401
  assert resp.json()["detail"]=="could not validate credential"  


# def test_voteauthorizedvalid(test_authorized,test_createproduct,create_user):
#     resp=test_authorized.post("/vote/",json={"productid":3,"votedir":1})
#     print(resp.json())
#     user=session.query(User).filter(User.username==create_user["username"]).first()
    
#     vote=session.query(Vote).filter(Vote.productid==3,Vote.userid==user.userid).first()
#     print(vote)

#     assert vote is not None
#     # assert resp.json()["detail"]=="No product found"
#     assert resp.status_code==201
def test_unvoteauthorized(test_voteauthorized,test_authorized,create_user,database):
  resp=test_authorized.post("/vote/",json={"productid":2,"votedir":0})
  user=database.query(User).filter(User.username==create_user["username"]).first()
    
  vote=database.query(Vote).filter(Vote.productid==2,Vote.userid==user.userid).first()
  assert vote is None
  assert resp.status_code==204
def test_votetwice(test_voteauthorized,test_authorized,create_user,database):
    
    resp=test_authorized.post("/vote/",json={"productid":test_voteauthorized,"votedir":1})
    user=database.query(User).filter(User.username==create_user["username"]).first()
    vote=database.query(Vote).filter(Vote.productid==test_voteauthorized,Vote.userid==user.userid).count()
    assert vote==1
    assert resp.status_code==409
    assert resp.json()["detail"]=="cannot like twice"
def test_voteunauthorized(client,test_createproduct):
    client.headers.pop("Authorization",None)
    resp=client.post("/vote/",json={"productid":1,"votedir":1})
    assert resp.status_code==401
    assert resp.json()["detail"]=="Not authenticated"
def test_delete_otherpost(test_authorized2,test_createproduct,create_user2):
  print(create_user2)
  resp=test_authorized2.delete("/products/3")
  assert resp.status_code==403
  assert resp.json()["detail"]=="you are not allowed to delete this product"
def  test_deleteown(test_authorized2,test_createproduct):

  response=test_authorized2.delete("/products/2")
  assert response.status_code==204


def test_updateother(test_authorized2,test_createproduct):

  
  resp=test_authorized2.put("/products/3",json={"productname":"updated by user2","productdescription":"this product is updated"})
  assert resp.status_code==403
  assert resp.json()["detail"]=="you are not allowed to update this product"






  


