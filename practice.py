# import requests
# url="http://localhost:8000/products"
# headers={
#   "Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOjksImV4cCI6MTc2MDA4OTAxMH0.i5OI8my0FeEi75HhecAHVU2JlnXctfD9dfUCaBnBZIU"
# }
# data=requests.get(url,params={"owner":"rashid"},headers=headers)
# import os
# from dotenv import load_dotenv
# load_dotenv()
# print(type(int(os.getenv("dbport"))))

# class InsufficientStudents(Exception):
#    pass
# def multiply(num1:int ,num2:int)->int:
#   return num1*num2
# class School():
#   def __init__(self,totalstudents):
#       self.totalstudents=totalstudents
#   def enroll(self,count):
#      self.totalstudents+=count
#   def withdraw(self,count):
#      if count>self.totalstudents:
#         raise InsufficientStudents("not enough students")
students={"name":"ahmad"}
try:
  del students["id"]
except KeyError:
  pass
print(students)