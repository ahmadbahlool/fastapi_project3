import pytest
from fastapi import HTTPException,status
from fastapi_app import schemas
from fastapi_app.schemas import Token,ProductOutput
from fastapi_app.config import env_variables

from fastapi_app.o2auth import verify_jwt_token,oauth2_scheme

def test_getuser(client,create_user):
  # client.post("/users/",json={"username":"rashid","userpassword":"rashi","useremail":"rashi@gmail.com"})
  response=client.get("/users/1")
  assert response.json().get("username")=="rashid"

def test_login(client,create_user):
  # client.post("/users/",json={"username":"rashid","userpassword":"rashi","useremail":"rashi@gmail.com"})
  # header={
  #   "username":"rashid",
  #   "password":"rashi"
  # }
  response=client.post("/user/login",data=create_user)
  token=Token(**response.json())
  validation=verify_jwt_token(token=token.access_token,credentialexception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED))
  assert response.status_code==200
@pytest.mark.parametrize("username,password,code,details",
                         [("rashid","rashid",403,"invalid credentials"),("rashi","rashid",403,"invalid credentials"),
                          (None,"rashi",403,"invalid credentials"),
                          ("rashid",None,403,"invalid credentials")])
def test_loginfail(client,create_user,username,password,code,details):
  response=client.post("/user/login",data={"username":username,"password":password})
  assert response.status_code==code
  assert response.json().get("detail")==details
