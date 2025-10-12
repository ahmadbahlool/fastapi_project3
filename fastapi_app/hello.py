from fastapi import FastAPI,APIRouter
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from .routes import users,products,votes
from . import authentication
from .models import Base
# Base.metadata.create_all(bind=engine)
from .config import env_variables
from alembic import command
from alembic.config import Config

command.upgrade(Config("alembic.ini"),revision="heads")


origins=[
"http://127.0.0.1:5500",
]
app=FastAPI()
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_methods=["GET"],
  allow_headers=["*"],
  allow_credentials=False
)
@app.get("/")
def returnst():
  return {"message":"success"}
router=APIRouter()
router.include_router(users.router)
router.include_router(products.router)
router.include_router(authentication.router)
router.include_router(votes.router)

app.include_router(router)
print(env_variables.dbhost)