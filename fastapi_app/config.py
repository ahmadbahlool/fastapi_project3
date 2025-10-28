from pydantic_settings import BaseSettings

class Env(BaseSettings):
 
  secretkey:str
  access_token_expires_minutes:int
  algorithm:str
  dburl:str
  class Config:
    env_file=".env"
  
env_variables=Env()
  
