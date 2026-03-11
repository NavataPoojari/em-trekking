from fastapi import FastAPI
from app.database import Base, engine

from app.routers import auth_router
from app.routers import user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TreekyHub Backend"
)

# app.include_router(auth_router.router)
app.include_router(user_router.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}