from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from fastapi.staticfiles import StaticFiles
import os
import io
from config import ACCESS_TOKEN_EXPIRE_MINUTES
from database_conn import database
from helper import authenticate_user, create_access_token, get_current_active_user
from custom_data_type import Token, User, UserInput

from subprocess import STDOUT, check_call , call,run



from app_func import predict

#import torch

app = FastAPI()
app.mount("/files", StaticFiles(directory="files"), name="files")

# def runandget():
#     run(['apt-get', 'update']) 
#     run(['apt-get', 'install', '-y', 'libgl1'])
#     run(['apt-get', 'install', '-y', 'libglib2.0-0'])
#     run(['apt-get', 'install' ,'-y','abiword']) 
   # check_call(['apt-get', 'update'], stdout=open(os.devnull,'wb'), stderr=STDOUT)
   # check_call(['apt-get', 'install', '-y', 'libgl1'], stdout=open(os.devnull,'wb'), stderr=STDOUT)
    #check_call(['apt-get', 'install', '-y', 'libglib2.0-0'], stdout=open(os.devnull,'wb'), stderr=STDOUT)

   # check_call([ 'apt-get', 'update','-y'], stdout=open(os.devnull,'wb'), stderr=STDOUT)
   # check_call([ 'apt-get', 'install' ,'-y','abiword'], stdout=open(os.devnull,'wb'), stderr=STDOUT)
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def database_connect():
    run(['apt-get', 'update']) 
    run(['apt-get', 'install', '-y', 'libgl1'])
    run(['apt-get', 'install', '-y', 'libglib2.0-0'])
    run(['apt-get', 'install' ,'-y','abiword']) 
    await database.connect()
@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()


# Authentication
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/predict")
async def fetch_data(userinput: UserInput, current_user: User = Depends(get_current_active_user)):
    #print(userinput.dict())
    #runandget()
    pred = predict(userinput.dict())
    print(pred)
    return pred
