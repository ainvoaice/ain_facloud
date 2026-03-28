from fastapi import APIRouter, Depends
from app.api.sanity import sanRou

rou = APIRouter()

rou.include_router(sanRou, tags=["Sanity Test"])    


