from fastapi import FastAPI
from app.routes.authroutes import router as authroutes
from app.routes.employeeroutes import router as employeeroutes


app = FastAPI()

app.include_router(authroutes)
app.include_router(employeeroutes)