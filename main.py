from fastapi import FastAPI

from motor.motor_asyncio import AsyncIOMotorClient

from middleware.error_handler import ErrorHandler

from routers.user import user_router

# APP_INFO
app = FastAPI()
app.title = "Match"
app.version = "0.0.1"

# MIDDLEWARE
# app.add_middleware(ErrorHandler)

# ROUTERS
app.include_router(user_router)

# async def start_db_client(app: FastAPI):
#     # Replace the connection string, database name, and collection name with your own values
#     connection_string = "mongodb://localhost:27017"
#     database_name = "match"
#     collection_name = "users"

#     # Connect to MongoDB using the connection string
#     app.mongodb_client = AsyncIOMotorClient(connection_string)

#     # Set the database and collection
#     app.database = app.mongodb_client[database_name]
#     app.collection = app.database[collection_name]

# @app.on_event("startup")
# async def startup_event():
#     await start_db_client(app)
