from fastapi import FastAPI
from app.api import routes

# Create the app
app = FastAPI()

# Connect the routes
app.include_router(routes.router)