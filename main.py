from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.authorization.router import authorization_router
from src.registration.router import register_router

authorization = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:7000",
    "http://localhost:6000",
    "http://localhost:5000",
]

authorization.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


authorization.include_router(authorization_router)
authorization.include_router(register_router)
