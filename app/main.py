from fastapi import FastAPI
from app.routes.authroutes import router as authroutes


app = FastAPI()

app.include_router(authroutes)